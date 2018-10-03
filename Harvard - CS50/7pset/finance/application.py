import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    sumtot = 0;
    portfo = db.execute("SELECT symbol, shares, price FROM transactions WHERE buyerid = :id GROUP BY symbol HAVING SUM(shares) > 0", id = session.get("user_id") )
    for ports in portfo:
        numshare = db.execute("SELECT SUM(shares) FROM transactions WHERE symbol=:symbol", symbol=ports["symbol"])
        ports["shares"] = numshare[0]["SUM(shares)"]
        stock = lookup(ports["symbol"])
        curtot = stock["price"] * ports["shares"]
        sumtot += curtot
        ports["name"] = stock["name"]
        ports["curtot"] = usd(curtot)
        ports["price"] = usd(stock["price"])

    pocket = db.execute("SELECT cash FROM users WHERE id = :id", id = session.get("user_id"))
    sumtot += pocket[0]["cash"]
    return render_template("index.html", portfo = portfo, sumtot = usd(sumtot), cash = usd(pocket[0]["cash"]))

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        if not stock:
            return apology("Symbol stock not found", 400)
        if not request.form.get("shares"):
            return apology("Missing Shares", 400)
        try:
            int(request.form.get("shares"))
        except:
            return apology("Must input positive integer", 400)

        if int(request.form.get("shares")) < 1:
            return apology("Must input positive integer", 400)

        shares = int(request.form.get("shares"))
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id = session.get("user_id") )
        price = stock["price"]


        if float(cash[0]["cash"]) < float(price * shares):
            return apology("Not enough cash")
        else:
            insert = db.execute("INSERT INTO transactions(buyerid, symbol, shares, price) VALUES(:id, :symbol, :shares, :price)", id = session.get("user_id"), symbol= stock["symbol"], shares=shares, price=usd(price))
            update = db.execute("UPDATE users SET cash = :money WHERE id = :id", money = float(cash[0]["cash"]) - (shares * price), id = session.get("user_id"))
            flash('Bought!')
            return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history", methods=["GET"])
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE buyerid = :id", id = session.get("user_id"))
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        quotes = lookup(request.form.get("symbol"))
        if not quotes:
            return apology("Symbol error", 400)
        quotes["price"] = usd(quotes["price"])
        return render_template("quoted.html", quotes=quotes)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Password and Confirmation password do not match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if len(rows) > 0:
            return apology("Username taken", 400)

        rows = db.execute("INSERT INTO users(username,hash) VALUES(:username, :hashpass)",
                        username=request.form.get("username"),
                        hashpass=generate_password_hash(request.form.get("password")))
        session["user_id"] = rows

        # # Redirect user to home page
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        sellreq = int(request.form.get("shares"))

        rows = db.execute("SELECT SUM(shares), price FROM transactions WHERE buyerid = :id and symbol = :symbol GROUP BY symbol", id = session.get("user_id"), symbol=symbol)
        if rows[0]["SUM(shares)"] < sellreq:
            return apology("You do not own that many shares")
        else:
            stock = lookup(symbol)

            cash = db.execute("SELECT cash FROM users WHERE id = :id", id = session.get("user_id") )
            price = stock["price"]

            newcash = float(cash[0]["cash"]) + (float(price * sellreq))

            db.execute("UPDATE users SET cash=:newcash WHERE id=:id", newcash = newcash, id = session.get("user_id"))
            db.execute("INSERT INTO transactions(buyerid, symbol, shares, price) VALUES(:id, :symbol, :shares, :price)", id = session.get("user_id"), symbol= stock["symbol"], shares=-(sellreq), price=usd(price))
            flash('Sold!')
            return redirect("/")
    else:
        portfo = db.execute("SELECT symbol FROM transactions WHERE buyerid = :id GROUP BY symbol", id = session.get("user_id") )
        return render_template("sell.html", portfo = portfo)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

@app.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    if request.method == "POST":
        password = request.form.get("password")
        newpassword = request.form.get("newpassword")
        confirmation = request.form.get("confirmation")

        if (newpassword != confirmation):
            return apology("new password and confirmation do not match", 400)

        valid = db.execute("SELECT * FROM users WHERE id = :id",
                          id = session.get("user_id"))

        # Ensure username exists and password is correct
        if not check_password_hash(valid[0]["hash"], request.form.get("password")):
            return apology("invalid password", 400)

        run = db.execute("UPDATE users SET hash=:hash WHERE id=:id", hash = generate_password_hash(request.form.get("newpassword")), id = session.get("user_id"))
        flash('Your password has been reset')
        return redirect("/")
    else:
        return render_template("settings.html")