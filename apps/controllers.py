# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import desc
from apps import app, db
from apps.forms import ArticleForm, CommentForm

from apps.models import (
	User,
	Article,
	Process,
	Inspire,
	Comment
)

"""
#
# @index & article list
#
@app.route('/', methods=['GET'])
def article_list():
	# html 파일에 전달할 데이터 Context
	context = {}

	# 현재 모든 글의 갯수를 DB에서 가져와 rows에 저장한다.
	rows = Article.query.count()
	#5개의 글을 가져오기 위해 rows에서 5개의 글을 빼준다.
	rows = rows - 5

	# Article 데이터 전부를 받아와서 최신글 순서대로 정렬하여 'article_list' 라는 key값으로 context에 저장한다.
	# id는 입력된 순서대로 저장되므로 아이디가 rows보다 큰 5개의 글만 가져온다.
	context['article_list'] = Article.query.order_by(desc(Article.date_created)).filter(Article.id > rows)


	return render_template('home.html', context=context, active_tab='timeline')


#
# @article controllers
#
@app.route('/article/create/', methods=['GET', 'POST'])
def article_create():
	form = ArticleForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			# 사용자가 입력한 글 데이터로 Article 모델 인스턴스를 생성한다.
			article = Article(
				title=form.title.data,
				author=form.author.data,
				category=form.category.data,
				content=form.content.data
			)

			# 데이터베이스에 데이터를 저장할 준비를 한다. (게시글)
			db.session.add(article)
			# 데이터베이스에 저장하라는 명령을 한다.
			db.session.commit()

			flash(u'게시글을 작성하였습니다.', 'success')
			return redirect(url_for('article_list'))

	return render_template('article/create.html', form=form, active_tab='article_create')


@app.route('/article/detail/<int:id>', methods=['GET'])
def article_detail(id):
	article = Article.query.get(id)
	# comments = Comment.query.order_by(desc(Comment.date_created)).filter_by(article=article)

	# relationship을 활용한 query
	comments = article.comments.order_by(desc(Comment.date_created)).all()


	return render_template('article/detail.html', article=article, comments=comments)




@app.route('/article/update/<int:id>', methods=['GET', 'POST'])
def article_update(id):
	article = Article.query.get(id)
	form = ArticleForm(request.form, obj=article)
	if request.method == 'POST':
		if form.validate_on_submit():
			form.populate_obj(article)
			db.session.commit()
		return redirect(url_for('article_detail', id=id))

	return render_template('article/update.html', form=form)


@app.route('/article/delete/<int:id>', methods=['GET', 'POST'])
def article_delete(id):
	if request.method == 'GET':
		return render_template('article/delete.html', article_id=id)
	elif request.method == 'POST':
		article_id = request.form['article_id']
		article = Article.query.get(article_id)
		db.session.delete(article)
		db.session.commit()

		flash(u'게시글을 삭제하였습니다.', 'success')
		return redirect(url_for('article_list'))


#
# @comment controllers
#
@app.route('/comment/create/<int:article_id>', methods=['GET', 'POST'])
def comment_create(article_id):
	form = CommentForm()
	if request.method == 'POST':
		if form.validate_on_submit():
			# comment = Comment(
			#     author=form.author.data,
			#     email=form.email.data,
			#     content=form.content.data,
			#     password=form.password.data,
			#     article_id=article_id
			# )
			comment = Comment(
				author=form.author.data,
				email=form.email.data,
				content=form.content.data,
				password=form.password.data,
				article=Article.query.get(article_id)
			)

			db.session.add(comment)
			db.session.commit()

			flash(u'댓글을 작성하였습니다.', 'success')
		return redirect(url_for('article_detail', id=article_id))
	return render_template('comment/create.html', form=form)


#
# @error Handlers
#
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

"""