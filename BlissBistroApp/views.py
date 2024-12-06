import json, requests
from django.shortcuts import render, redirect, get_object_or_404
from BlissBistroApp.models import Booking, Contact, User, FoodItem, Order, ImageModel, Subscriber
from BlissBistroApp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from BlissBistroApp.forms import BookingForm, OrderForm, ImageUploadForm, SubscriberForm
from django.http import Http404, HttpResponse
from requests.auth import HTTPBasicAuth
from django.contrib import messages
from decimal import Decimal, InvalidOperation
from collections import defaultdict
from django.db.models import Sum, Value
from django.db.models.functions import Concat
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
# def index(request):
#     return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')
def starter(request):
    return render(request, 'starter-page.html')
def about(request):
    return render(request, 'about.html')
def menu(request):
    return render(request, 'menu.html')
def specials(request):
    return render(request, 'specials.html')
def events(request):
    return render(request, 'events.html')
def gallery(request):
    return render(request, 'gallery.html')


def chefs(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            return render(request, 'chefs.html')
        else:
            # Display an error message for invalid credentials
            messages.error(request, "Invalid Login Credentials. Please Try Again.")
            return render(request, 'login.html')  # Show the login page again

    # Render login page if the request method is GET
    return render(request, 'login.html')
def booking(request):
    if request.method == "POST":
        BookaTable=Booking(
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            date=request.POST["date"],
            time=request.POST["time"],
            people=request.POST["people"],
            message=request.POST["message"],
        )
        BookaTable.save()
        return redirect("/booking")
    else:
        return render(request, 'booking.html')
def contact(request):
    if request.method == "POST":
        MyContact=Contact(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"],
        )
        MyContact.save()
        return redirect("/contact")
    else:
        return render(request, 'contact.html')
def testimonials(request):
    return render(request, 'testimonials.html')
def showB(request):
    allBookings = Booking.objects.all()
    return render(request, 'show.html', {'bookings': allBookings})
def showC(request):
    allContacts = Contact.objects.all()
    return render(request, 'showcontacts.html', {'contacts': allContacts})
def delete(request,id):
    delBooking = Booking.objects.get(id=id)
    delBooking.delete()
    return redirect('/showb')
def edit(request,id):
    editBooking = Booking.objects.get(id=id)
    return render(request, 'edit.html', {'editbookings': editBooking})
def update(request,id):
    updateBooking = Booking.objects.get(id=id)
    BForm = BookingForm(request.POST, instance=updateBooking)
    if BForm.is_valid():
        BForm.save()
        return redirect('/showb')
    else:
        return render(request, 'edit.html')

def register(request):
    if request.method == "POST":
        users = User(
            name=request.POST["name"],
            email=request.POST["email"],
            username=request.POST["username"],
            password=request.POST["password"],
        )
        users.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
def subscribe(request):
    return render(request, 'starter-page.html')
# def order(request):
#     return render(request, 'order.html')
# def summary(request):
#     return render(request, 'summary.html')

def order_view(request):
    food_items = FoodItem.objects.all()

    if request.method == "POST":
        # Retrieve session orders or initialize an empty dictionary
        session_orders = request.session.get('orders', {})

        for key, value in request.POST.items():
            if key.startswith("quantity_") and value.isdigit() and int(value) > 0:
                food_id = key.split("_")[1]
                quantity = int(value)

                try:
                    food_item = FoodItem.objects.get(id=food_id)
                    price = Decimal(food_item.price)

                    # Save the order to the database
                    Order.objects.create(
                        session_key=request.session.session_key,  # Associate with session
                        item=food_item,
                        quantity=quantity,
                        total_price=price * quantity
                    )

                    # Update session orders for display
                    if food_id in session_orders:
                        session_orders[food_id]['quantity'] += quantity
                        session_orders[food_id]['total_price'] = str(
                            Decimal(session_orders[food_id]['price']) * session_orders[food_id]['quantity']
                        )
                    else:
                        session_orders[food_id] = {
                            'name': food_item.name,
                            'price': str(price),  # Save price as a string to avoid serialization issues
                            'quantity': quantity,
                            'total_price': str(price * quantity),
                        }
                except FoodItem.DoesNotExist:
                    messages.error(request, f"Food item with ID {food_id} does not exist.")
                    return redirect('order')

        # Save updated orders back to the session
        request.session['orders'] = session_orders
        request.session.modified = True
        messages.success(request, "Order submitted successfully!")
        return redirect('summary')

    return render(request, 'order.html', {'food_items': food_items})





def summary_view(request):
    session_orders = request.session.get('orders', {})

    if not session_orders:
        return render(request, 'summary.html', {'combined_order': None})

    # Use defaultdict to store aggregated data for food items
    aggregated_orders = defaultdict(lambda: {'quantity': 0, 'total_price': Decimal(0)})

    # Aggregate orders from the session
    for food_id, order_data in session_orders.items():
        quantity = order_data['quantity']
        total_price = Decimal(order_data['total_price'])  # Convert back to Decimal
        name = order_data['name']

        aggregated_orders[name]['quantity'] += quantity
        aggregated_orders[name]['total_price'] += total_price

    # Prepare combined data for display
    combined_food = ", ".join([food for food in aggregated_orders])  # Combined food names
    total_quantity = sum(aggregated_orders[food]['quantity'] for food in aggregated_orders)  # Total quantity
    total_price = sum(aggregated_orders[food]['total_price'] for food in aggregated_orders)  # Total price

    combined_order = {
        "combined_food": combined_food,
        "total_quantity": total_quantity,
        "total_price": total_price,
    }

    return render(request, 'summary.html', {'combined_order': combined_order})

def deleteorder(request, id):
    try:
        # Try to fetch the object; this will raise Order.DoesNotExist if not found
        delOrder = Order.objects.get(id=id)
        delOrder.delete()
        messages.success(request, "Order has been successfully deleted.")
    except Order.DoesNotExist:
        # Handle the case where the object does not exist
        messages.error(request, "Order not found. Unable to delete.")
    return redirect('/summary')

def editorder(request, id):
    from BlissBistroApp.models import FoodItem, Order
    # Get the specific order to edit
    editOrder = get_object_or_404(Order, id=id)
    # Get all available food items
    food_items = Order.objects.all()
    return render(request, 'editorder.html', {
        'editorders': editOrder,
        'food_items': food_items
    })

def updateorder(request,id):
    updateOrder = Order.objects.get(id=id)
    OForm = OrderForm(request.POST, instance=updateOrder)
    if OForm.is_valid():
        OForm.save()
        return redirect('/summary')
    else:
        return render(request, 'editorder.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'uploadimage.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'showimage.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

def token(request):
    consumer_key = 'xOG0vx0U6V0A2PzSdrvLRY8cAXb4uJkOECSPct1BCLU5J7vo'
    consumer_secret = '15KMsQZWfHeM6mWTjGVES9mibdGNmhKosfqp7W10Av1WavhbkGjmEkPcAVGYqGnI'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]
    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Bliss Bistro Essence",
            "TransactionDesc": "Meal Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment Successful!!! Thank you for dining with us!!! 😁😉")


def delete_all_orders_view(request):
    # Delete orders from the session
    if 'orders' in request.session:
        del request.session['orders']  # Clear orders from session
        messages.success(request, "All session orders have been cleared.")
    else:
        messages.error(request, "No session orders to delete.")

    # Delete all orders from the database
    deleted_count, _ = Order.objects.all().delete()  # Adjust this query to target only relevant orders
    if deleted_count > 0:
        messages.success(request, f"{deleted_count} orders have been deleted from the database.")
    else:
        messages.error(request, "No orders found in the database to delete.")

    return redirect('summary')

def edit_all_orders_view(request):
    # Retrieve orders from the session
    session_orders = request.session.get('orders', {})

    if not session_orders:
        messages.error(request, "No orders to edit.")
        return redirect('summary')

    if request.method == "POST":
        updated_orders = {}
        for food_id, details in session_orders.items():
            # Retrieve new quantity from the form
            quantity_key = f"quantity_{food_id}"
            new_quantity = request.POST.get(quantity_key)

            if not new_quantity or not new_quantity.isdigit():
                messages.error(request, f"Invalid quantity for {details['name']}.")
                continue

            new_quantity = int(new_quantity)

            if new_quantity > 0:
                # Update order details
                updated_orders[food_id] = {
                    'name': details['name'],
                    'price': details['price'],  # Preserve price from session
                    'quantity': new_quantity,
                    'total_price': str(Decimal(details['price']) * new_quantity)
                }
            else:
                # Remove items with zero quantity
                messages.info(request, f"{details['name']} was removed from your order.")

        # Update session orders
        request.session['orders'] = updated_orders
        request.session.modified = True
        messages.success(request, "Your orders have been updated.")
        return redirect('summary')

    # Render the edit page with current session orders
    return render(request, 'editorder.html', {'session_orders': session_orders})




def update_all_orders_view(request, food_id):
    session_orders = request.session.get('orders', {})

    if request.method == "POST":
        updated_quantity = request.POST.get('quantity')

        if not updated_quantity or not updated_quantity.isdigit():
            messages.error(request, "Invalid quantity entered.")
            return redirect('edit_order', food_id=food_id)

        updated_quantity = int(updated_quantity)

        if food_id in session_orders:
            if updated_quantity > 0:
                # Calculate the new total price
                food_price = float(session_orders[food_id]['total_price']) / float(session_orders[food_id]['quantity'])
                session_orders[food_id]['quantity'] = updated_quantity
                session_orders[food_id]['total_price'] = str(food_price * updated_quantity)
            else:
                # Remove the order if quantity is set to 0
                del session_orders[food_id]

            request.session['orders'] = session_orders
            request.session.modified = True
            messages.success(request, "Order updated successfully!")
            return redirect('summary')
        else:
            messages.error(request, "Order not found.")
            return redirect('summary')

    # If it's a GET request, render the edit page
    if food_id in session_orders:
        order = session_orders[food_id]
        return render(request, 'edit_order.html', {'order': order})
    else:
        messages.error(request, "Order not found.")
        return redirect('summary')

def clear_session_view(request):
    if 'orders' in request.session:
        del request.session['orders']  # Remove session orders
        request.session.modified = True  # Mark the session as modified
        messages.success(request, "Session cleared. Ready for a new customer.")
    else:
        messages.warning(request, "No active session orders to clear.")
    return redirect('order')  # Redirect to the order page