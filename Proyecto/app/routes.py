from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import Inventory
from app.forms import AddItemForm, EditItemForm  # Importar los formularios

@app.route('/')
def index():
    items = Inventory.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddItemForm()  
    if form.validate_on_submit():
        new_item = Inventory(
            name=form.name.data,
            price=form.price.data,
            mac_address=form.mac_address.data,
            serial_number=form.serial_number.data,
            manufacturer=form.manufacturer.data,
            description=form.description.data
        )
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)  

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = Inventory.query.get_or_404(id)
    form = EditItemForm(obj=item)  
    if form.validate_on_submit():  
        item.name = form.name.data
        item.price = form.price.data
        item.mac_address = form.mac_address.data
        item.serial_number = form.serial_number.data
        item.manufacturer = form.manufacturer.data
        item.description = form.description.data
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', form=form, item=item)  

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    item = Inventory.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('index'))
