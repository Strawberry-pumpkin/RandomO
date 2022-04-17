from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    Flask,
    flash,
)
from random import randrange
import os
from os.path import exists

from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

UPLOAD_FOLDER = "/home/RandomO/mysite/profile-pics"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


views = Flask(__name__)
views.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
views.secret_key = b'_5#y2L"F4Q8z\n\xec]ewrfgthyju//'


def allowed_file(filename):
    if "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


@views.route("/", methods=["GET", "POST"])
def home():
    # profile pic upload
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):

            with open("/home/RandomO/mysite/static/users.txt", "r") as us:
                users = us.read().splitlines()
                if session.get("username") in users:

                    filename = secure_filename(
                        session.get("username")
                        + f'.{file.filename.rsplit(".",1)[1].lower()}'
                    )

                    file.save(os.path.join(views.config["UPLOAD_FOLDER"], filename))

    profile_picture = ""
    if "username" in session:
        if exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpg'):
            profile_picture = session.get("username") + ".jpg"

        elif exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.png'):
            profile_picture = session.get("username") + ".png"

        elif exists(
            f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpeg'
        ):
            profile_picture = session.get("username") + ".jpeg"
        elif "guest" in session.get("username").lower():
            profile_picture = "guest.png"
        else:
            profile_picture = "default.png"

    # search bar
    if request.method == "GET":
        query = request.args.get("search")
        if query != "" and query is not None:
            with open("/home/RandomO/mysite/static/keywords.txt", "r") as keys:
                keywords = keys.read().splitlines()
                for i in keywords:
                    if i in query:
                        redirect_to = keywords[keywords.index(i) - 1]
                        return redirect(redirect_to)

    player_data = []
    alld = []

    if "username" in session:
        log_status = "ogout"  # "L" is not included bcz it's in the HTML file

        with open("/home/RandomO/mysite/static/users.txt", "r+") as us:
            users = us.read().splitlines()
            for i in range(0, len(users), 3):
                alld.append((users[i], int(users[i + 1]), users[i + 2]))
            alld.sort(key=lambda x: x[1], reverse=True)
            for item in alld:
                if session.get("username") in item:
                    player_data.append(alld.index(item) + 1)
                    player_data.append(item[0])
                    player_data.append(item[1])
                    player_data.append(item[2])

    else:
        log_status = "ogin"  # "L" is not included bcz it's in the HTML file

    # for the contact us element #

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))
    return render_template(
        "home.html",
        log_status=log_status,
        player_data=player_data,
        profile_picture=profile_picture,
    )


@views.route("/random-tasks", methods=["GET", "POST"])
def random_tasks():
    # profile pic upload
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):

            with open("/home/RandomO/mysite/static/users.txt", "r") as us:
                users = us.read().splitlines()
                if session.get("username") in users:

                    filename = secure_filename(
                        session.get("username")
                        + f'.{file.filename.rsplit(".",1)[1].lower()}'
                    )

                    file.save(os.path.join(views.config["UPLOAD_FOLDER"], filename))

    profile_picture = ""
    if "username" in session:
        if exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpg'):
            profile_picture = session.get("username") + ".jpg"

        elif exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.png'):
            profile_picture = session.get("username") + ".png"

        elif exists(
            f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpeg'
        ):
            profile_picture = session.get("username") + ".jpeg"
        elif "guest" in session.get("username").lower():
            profile_picture = "guest.png"
        else:
            profile_picture = "default.png"

    if request.method == "POST":

        add = request.form["add"]
        user = request.form["username"]
        count = request.form["count"]
        with open("/home/RandomO/mysite/static/users.txt", "r+") as us:
            all_users = us.read().splitlines()
            user_index = all_users.index(user)
            all_users[user_index + 1] = str(int(all_users[user_index + 1]) + int(add))
            all_users[user_index + 2] = str(int(all_users[user_index + 2]) + int(count))
            us.seek(0)
            us.writelines("\n".join(all_users))

    player_data = []
    alld = []
    if "username" in session:
        log_status = "ogout"  # "L" is not included bcz it's in the HTML file

        with open("/home/RandomO/mysite/static/users.txt", "r+") as us:
            users = us.read().splitlines()
            for i in range(0, len(users), 3):
                alld.append((users[i], int(users[i + 1]), users[i + 2]))
            alld.sort(key=lambda x: x[1], reverse=True)
            for item in alld:
                if session.get("username") in item:
                    player_data.append(alld.index(item) + 1)
                    player_data.append(item[0])
                    player_data.append(item[1])
                    player_data.append(item[2])

    else:
        log_status = "ogin"  # "L" is not included bcz it's in the HTML file

    user = ""
    task1 = []
    task2 = []
    task3 = []
    with open("/home/RandomO/mysite/static/tasks.txt", "r") as ts:
        tasks = ts.read().splitlines()
        r1 = randrange(0, int(len(tasks) / 5)) * 5
        r2 = randrange(0, int(len(tasks) / 5)) * 5
        r3 = randrange(0, int(len(tasks) / 5)) * 5
        task1.append(
            (tasks[r1], tasks[r1 + 1], tasks[r1 + 2], tasks[r1 + 3], tasks[r1 + 4])
        )
        task2.append(
            (tasks[r2], tasks[r2 + 1], tasks[r2 + 2], tasks[r2 + 3], tasks[r2 + 4])
        )
        task3.append(
            (tasks[r3], tasks[r3 + 1], tasks[r3 + 2], tasks[r3 + 3], tasks[r3 + 4])
        )

    # for the contact us element #

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))
    if request.method == "GET":
        query = request.args.get("search")
        if query != "" and query is not None:
            with open("/home/RandomO/mysite/static/keywords.txt", "r") as keys:
                keywords = keys.read().splitlines()
                for i in keywords:
                    if i in query:
                        redirect_to = keywords[keywords.index(i) - 1]
                        return redirect(redirect_to)

    return render_template(
        "random.html",
        t1=task1,
        t2=task2,
        t3=task3,
        user=user,
        player_data=player_data,
        log_status=log_status,
        profile_picture=profile_picture,
    )


@views.route("/leaderboard")
def leaderboard():
    # profile pic upload
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):

            with open("/home/RandomO/mysite/static/users.txt", "r") as us:
                users = us.read().splitlines()
                if session.get("username") in users:

                    filename = secure_filename(
                        session.get("username")
                        + f'.{file.filename.rsplit(".",1)[1].lower()}'
                    )

                    file.save(os.path.join(views.config["UPLOAD_FOLDER"], filename))

    profile_picture = ""
    if "username" in session:
        if exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpg'):
            profile_picture = session.get("username") + ".jpg"

        elif exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.png'):
            profile_picture = session.get("username") + ".png"

        elif exists(
            f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpeg'
        ):
            profile_picture = session.get("username") + ".jpeg"
        elif "guest" in session.get("username").lower():
            profile_picture = "guest.png"
        else:
            profile_picture = "default.png"

    player_data = []
    data_table = []
    alld = []
    if "username" in session:
        log_status = "ogout"  # "L" is not included bcz it's in the HTML file

        with open("/home/RandomO/mysite/static/users.txt", "r+") as us:
            users = us.read().splitlines()
            for i in range(0, len(users), 3):
                alld.append((users[i], int(users[i + 1]), users[i + 2]))
            alld.sort(key=lambda x: x[1], reverse=True)
            for item in alld:
                if session.get("username") in item:
                    player_data.append(alld.index(item) + 1)
                    player_data.append(item[0])
                    player_data.append(item[1])
                    player_data.append(item[2])

    else:
        log_status = "ogin"  # "L" is not included bcz it's in the HTML file

    # for the contact us element #

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))
    with open("/home/RandomO/mysite/static/users.txt", "r+") as us:

        users = us.read().splitlines()
        for i in range(0, len(users), 3):
            data_table.append((users[i], int(users[i + 1]), users[i + 2]))
            data_table.sort(key=lambda x: x[1], reverse=True)
    if request.method == "GET":
        query = request.args.get("search")
        if query != "" and query is not None:
            with open("/home/RandomO/mysite/static/keywords.txt", "r") as keys:
                keywords = keys.read().splitlines()
                for i in keywords:
                    if i in query:
                        redirect_to = keywords[keywords.index(i) - 1]
                        return redirect(redirect_to)

    return render_template(
        "leaderboard.html",
        data_table=data_table,
        player_data=player_data,
        log_status=log_status,
        profile_picture=profile_picture,
    )


@views.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        with open("/home/RandomO/mysite/static/confid.txt", "r") as log:
            login_details = log.read().splitlines()
            if username in login_details:
                user_index = login_details.index(username)
                if check_password_hash(login_details[user_index + 1], password):
                    session["username"] = username
                    return redirect("/")
                else:
                    error = "Incorrect Password, Please try again"
            else:
                error = f"No such player : {username} "
                return render_template("login.html", error=error)

    # for the contact us element #

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))
    return render_template("login.html", error=error)


@views.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # profile pic upload
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            with open("/home/RandomO/mysite/static/confid.txt", "r+") as sh:
                shh = sh.read().splitlines()
                if username not in shh:
                    shh.append(username)
                    shh.append(generate_password_hash(password))
                    sh.seek(0)
                    sh.writelines("\n".join(shh))
                    return redirect("/signup-success")
                elif username in shh:
                    error = "User name already exists."
                    return render_template("sign-up.html", error=error)
        except:
            error = "Something went wrong :( Please try again"
            return render_template("sign-up.html", error=error)

    # for the contact us element #

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))
    if request.method == "GET":
        query = request.args.get("search")
        if query != "" and query is not None:
            with open("/home/RandomO/mysite/static/keywords.txt", "r") as keys:
                keywords = keys.read().splitlines()
                for i in keywords:
                    if i in query:
                        redirect_to = keywords[keywords.index(i) - 1]
                        return redirect(redirect_to)

    return render_template("sign-up.html")


@views.route("/signup-success")
def success():

    # for the contact us element #

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))
    if request.method == "GET":
        query = request.args.get("search")
        if query != "" and query is not None:
            with open("/home/RandomO/mysite/static/keywords.txt", "r") as keys:
                keywords = keys.read().splitlines()
                for i in keywords:
                    if i in query:
                        redirect_to = keywords[keywords.index(i) - 1]
                        return redirect(redirect_to)

    return render_template("sign-up-successful.html")


@views.route("/logout")
def logged_out():
    if "username" in session:
        session.pop("username")
    return redirect("/")


@views.route("/guest")
def guest():

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))
    with open("/home/RandomO/mysite/static/users.txt", "r+") as us:
        users = us.read().splitlines()
        username = "Guest001"
        count = 0
        while username in users:
            username = "Guest" + str(count)
            count += 1
        users.append(username)
        users.append("0")
        users.append("0")
        us.seek(0)
        us.writelines("\n".join(users))
        session["username"] = username

    if request.method == "GET":
        query = request.args.get("search")
        if query != "" and query is not None:
            with open("/home/RandomO/mysite/static/keywords.txt", "r") as keys:
                keywords = keys.read().splitlines()
                for i in keywords:
                    if i in query:
                        redirect_to = keywords[keywords.index(i) - 1]
                        return redirect(redirect_to)

        return render_template("guest.html", username=username)


@views.route("/unbelievable")
def unbelievable():
    # profile pic upload
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):

            with open("/home/RandomO/mysite/static/users.txt", "r") as us:
                users = us.read().splitlines()
                if session.get("username") in users:

                    filename = secure_filename(
                        session.get("username")
                        + f'.{file.filename.rsplit(".",1)[1].lower()}'
                    )

                    file.save(os.path.join(views.config["UPLOAD_FOLDER"], filename))

    profile_picture = ""
    if "username" in session:
        if exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpg'):
            profile_picture = session.get("username") + ".jpg"

        elif exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.png'):
            profile_picture = session.get("username") + ".png"

        elif exists(
            f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpeg'
        ):
            profile_picture = session.get("username") + ".jpeg"
        elif "guest" in session.get("username").lower():
            profile_picture = "guest.png"
        else:
            profile_picture = "default.png"

    alld = []
    player_data = []
    if request.method == "GET":
        query = request.args.get("search")
        if query != "" and query is not None:
            with open("/home/RandomO/mysite/static/keywords.txt", "r") as keys:
                keywords = keys.read().splitlines()
                for i in keywords:
                    if i in query:
                        redirect_to = keywords[keywords.index(i) - 1]
                        return redirect(redirect_to)

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))

    if "username" in session:
        log_status = "ogout"  # "L" is not included bcz it's in the HTML
        with open("/home/RandomO/mysite/static/users.txt", "r+") as us:
            users = us.read().splitlines()
            for i in range(0, len(users), 3):
                alld.append((users[i], int(users[i + 1]), users[i + 2]))
            alld.sort(key=lambda x: x[1], reverse=True)
            for item in alld:
                if session.get("username") in item:
                    player_data.append(alld.index(item) + 1)
                    player_data.append(item[0])
                    player_data.append(item[1])
                    player_data.append(item[2])

    else:
        log_status = "ogin"

    return render_template(
        "unbelievable.html",
        player_data=player_data,
        log_status=log_status,
        profile_picture=profile_picture,
    )


@views.route("/tips")
def emulator():
    # profile pic upload
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if file and allowed_file(file.filename):

            with open("/home/RandomO/mysite/static/users.txt", "r") as us:
                users = us.read().splitlines()
                if session.get("username") in users:

                    filename = secure_filename(
                        session.get("username")
                        + f'.{file.filename.rsplit(".",1)[1].lower()}'
                    )

                    file.save(os.path.join(views.config["UPLOAD_FOLDER"], filename))

    profile_picture = ""
    if "username" in session:
        if exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpg'):
            profile_picture = session.get("username") + ".jpg"

        elif exists(f'/home/RandomO/mysite/profile-pics/{session.get("username")}.png'):
            profile_picture = session.get("username") + ".png"

        elif exists(
            f'/home/RandomO/mysite/profile-pics/{session.get("username")}.jpeg'
        ):
            profile_picture = session.get("username") + ".jpeg"
        elif "guest" in session.get("username").lower():
            profile_picture = "guest.png"
        else:
            profile_picture = "default.png"

    alld = []
    player_data = []
    if request.method == "GET":
        query = request.args.get("search")
        if query != "" and query is not None:
            with open("/home/RandomO/mysite/static/keywords.txt", "r") as keys:
                keywords = keys.read().splitlines()
                for i in keywords:
                    if i in query:
                        redirect_to = keywords[keywords.index(i) - 1]
                        return redirect(redirect_to)

    if request.method == "POST":
        contact_email = request.form.get("contact_sender")
        description = request.form.get("description")
        if contact_email != None and description != None:
            with open("/home/RandomO/mysite/static/contact.txt", "r+") as cnt:
                contact = cnt.read().splitlines()
                contact.append(contact_email + "\n")
                contact.append(description + "\n")
                cnt.seek(0)
                cnt.writelines("\n".join(contact))

    if "username" in session:
        log_status = "ogout"  # "L" is not included bcz it's in the HTML
        with open("/home/RandomO/mysite/static/users.txt", "r+") as us:
            users = us.read().splitlines()
            for i in range(0, len(users), 3):
                alld.append((users[i], int(users[i + 1]), users[i + 2]))
            alld.sort(key=lambda x: x[1], reverse=True)
            for item in alld:
                if session.get("username") in item:
                    player_data.append(alld.index(item) + 1)
                    player_data.append(item[0])
                    player_data.append(item[1])
                    player_data.append(item[2])

    else:
        log_status = "ogin"

    return render_template(
        "tips.html",
        player_data=player_data,
        log_status=log_status,
        profile_picture=profile_picture,
    )


@views.before_request
def make_session_permanent():
    session.permanent = True
