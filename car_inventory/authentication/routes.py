from flask import Blueprint, render_template, request, flash, redirect, url_for
from car_inventory.forms import UserLoginForm
from car_inventory.models import User, db

auth = Blueprint('auth',__name__,template_folder='auth_templates')

@auth.route('/signup',methods=['GET','POST'])
def signup():
    form = UserLoginForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)

            user = User(email, password = password)

            db.session.add(user)
            db.session.commit()
            
            flash(f'You have successfully created a user account: {email}', 'user-created')

            return redirect(url_for('site.index'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form Inputs')
    
    return render_template('signup.html', form = form)


@auth.route('/signin',methods=['GET','POST'])
def signin():
    return render_template('signin.html')

@auth.route('/checkout')
def checkout():
    return render_template('checkout.html')