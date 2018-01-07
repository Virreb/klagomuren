from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login')
def login_user():

    # show login page and get user credentials

    return render_template('login.html')


@app.route('/categories')
def show_categories():

    # get credentials and show available categories for that user

    return render_template('categories.html')


@app.route('/article_summaries')
def show_article_summaries():

    # Show titles of texts for the given wanted category

    return render_template('article_summaries.html')


@app.route('/article')
def show_article():

    # Show full wanted article

    return render_template('article.html')


if __name__ == "__main__":
    app.run()
