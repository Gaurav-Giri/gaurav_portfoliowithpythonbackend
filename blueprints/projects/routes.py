from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from werkzeug.utils import secure_filename
from models import db, Project
from forms import ProjectForm
import os

projects_bp = Blueprint('projects', __name__)

@projects_bp.route('/projects')
def list_projects():
    projects = Project.query.order_by(Project.id.desc()).all()
    return render_template('projects/list.html', projects=projects)

@projects_bp.route('/projects/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('projects/detail.html', project=project)

@projects_bp.route('/projects/create', methods=['GET', 'POST'])
@login_required
def create_project():
    form = ProjectForm()
    if form.validate_on_submit():
        try:
            filename = None
            if form.image.data:
                file = form.image.data
                filename = secure_filename(file.filename)
                file.save(os.path.join('static/uploads', filename))
            
            project = Project(
                title=form.title.data,
                description=form.description.data,
                technologies=form.technologies.data,
                project_link=form.project_link.data,
                image_url=filename
            )
            db.session.add(project)
            db.session.commit()
            flash('Project created successfully!', 'success')
            return redirect(url_for('projects.list_projects'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating project: {str(e)}', 'error')
    return render_template('projects/create.html', form=form)

@projects_bp.route('/projects/<int:project_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    form = ProjectForm(obj=project)
    if form.validate_on_submit():
        try:
            if form.image.data:
                file = form.image.data
                filename = secure_filename(file.filename)
                file.save(os.path.join('static/uploads', filename))
                project.image_url = filename
            
            project.title = form.title.data
            project.description = form.description.data
            project.technologies = form.technologies.data
            project.project_link = form.project_link.data
            
            db.session.commit()
            flash('Project updated successfully!', 'success')
            return redirect(url_for('projects.project_detail', project_id=project.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating project: {str(e)}', 'error')
    return render_template('projects/edit.html', form=form, project=project)

@projects_bp.route('/projects/<int:project_id>/delete', methods=['POST'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    try:
        db.session.delete(project)
        db.session.commit()
        flash('Project deleted successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting project: {str(e)}', 'error')
    return redirect(url_for('projects.list_projects'))