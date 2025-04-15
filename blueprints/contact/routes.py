from flask import Blueprint, render_template, redirect, url_for, flash
from forms import ContactForm
from models import db, ContactMessage

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            message = ContactMessage(
                name=form.name.data,
                email=form.email.data,
                message=form.message.data
            )
            db.session.add(message)
            db.session.commit()
            flash('Your message has been sent!', 'success')
            return redirect(url_for('contact.contact'))
        except Exception as e:
            db.session.rollback()
            flash('Error sending message', 'error')
    return render_template('contact/index.html', form=form)