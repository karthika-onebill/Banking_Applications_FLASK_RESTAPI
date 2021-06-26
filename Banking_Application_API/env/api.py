'''  Banking Applications - Perform CRUD operations on Customer Details using REST API  '''

from flask import Flask,jsonify,render_template,request

app = Flask(__name__) #loading app into flask


#customer details - (information) (for dummy purpose)
Customer_Details = [
    {
        'customer_name':'karthika',
        'account_number':'ACC323501',
        'account_type' :'Saving',
        'available_balance':30000
    },
     {
        'customer_name':'Divya',
        'account_number':'ACC323502',
        'account_type' :'Saving',
        'available_balance':10000
    }

]

#CRUD OPERATIONS

#index page : home page
@app.route('/')
def index() :
    return render_template('index.html',msg="Information about All Customers")
   

# get - all customer details
@app.route('/get',methods=['GET'])
def getAllDetails() :

    return render_template('getallcustomer.html',account=Customer_Details,n=len(Customer_Details))
 

#get - particular customer details
@app.route('/getc',methods=['GET','POST'])
def getParticularDetails() :
    temp=-1
    if(request.method=='POST') :
        acc_no = request.form['account_no']
        for i in range(len(Customer_Details)) :
            if(Customer_Details[i]['account_number']==acc_no) :
                temp=i
    if(temp!=-1) :
        return render_template('getparticularcustomer.html',account=Customer_Details[temp])
    else :
        return render_template('getparticularcustomer.html',account=[])
       


#post - insert new customer details

@app.route('/post',methods=['GET','POST'])
def postData() :
    #creating account_no automatically try to insert new data
    acc_no = int(Customer_Details[len(Customer_Details)-1]['account_number'].lstrip('ACC3235'))+1
    if(len(str(acc_no))>1) :
        acc_no = 'ACC3235%i' % acc_no       #for adding single digit account_number at end (00to 09)
    else :
        acc_no = 'ACC32350%i' % acc_no      #for adding double digit account_number at end (10to 99)
    if(request.method=='POST') :
        customer_data =  {
        'customer_name':request.form['customer_name'],
        'account_number':acc_no,
        'account_type' :request.form['account_type'],
        'available_balance':0
        }
        Customer_Details.append(customer_data)
    return render_template('newcustomer.html')
    #return jsonify({'Results':'Successfully inserted!'})


# put - update data based on account_number

@app.route('/put',methods=['GET','POST'])
def update() :
    temp=-1
    if(request.method=='POST') :
        account_no = request.form['account_no']
        up_customer_name = request.form['customer_name']
        up_account_type = request.form['account_type']
        
       
        for i in range(len(Customer_Details)) :
            if(Customer_Details[i]['account_number']==account_no) :
                temp=i
    if(temp!=-1) :
        Customer_Details[temp]['customer_name'] = up_customer_name
        Customer_Details[temp]['account_type'] = up_account_type
        return render_template('update.html',msg="Your data updated Succssfully!")
    else :
        return render_template('update.html',msg="")





# delete - delete customer data based on account_number

@app.route('/delete',methods=['GET','POST'])
def delete() :
        
    temp=-1
    if(request.method=='POST') :
        for i in range(len(Customer_Details)) :
            if(Customer_Details[i]['account_number']==request.form['account_no']) :
                temp=i
    if(temp!=-1) :
        del Customer_Details[temp]
        return render_template('delete.html',msg="Your data deleted Succssfully!")
    else :
        return render_template('delete.html',msg="")


#Banking Operations 

#Depsit - deposit the amount based on particular account_number


@app.route('/deposit',methods=['GET','POST'])
def deposit() :
        
    temp=-1
    if(request.method=='POST') :
        for i in range(len(Customer_Details)) :
            if(Customer_Details[i]['account_number']==request.form['account_no']) :
                temp=i
    if(temp!=-1) :
        deposit_amount = int(request.form['amount'])
        Customer_Details[temp]['available_balance']+=deposit_amount
        return render_template('deposit.html',msg="Your amount credited Succssfully!")
    else :
        return render_template('deposit.html',msg="")



#Withdraw - withdraw the amount based on particular account_number (condition : availablebalance - amount can't goes <0)


@app.route('/withdraw',methods=['GET','POST'])
def withdraw() :
    temp=-1
    if(request.method=="POST") :
        
        for i in range(len(Customer_Details)) :
            if(Customer_Details[i]['account_number']==request.form['account_no']) :
                temp=i
    if(temp!=-1) :
        withdraw_amount = int(request.form['amount'])
        #checking withdraw constraints

        if(Customer_Details[temp]['available_balance']-withdraw_amount>0) :
            Customer_Details[temp]['available_balance']-=withdraw_amount
            return render_template('withdraw.html',msg="Your amount debited Succssfully!")
        else :
            return render_template('withdraw.html',msg="Your amount was insufficient")
    else :
        return render_template('withdraw.html',msg="")



#balace enquiry

@app.route('/balance',methods=['GET','POST'])
def balance() :
    temp=-1
    if(request.method=="POST") :
        
        for i in range(len(Customer_Details)) :
            if(Customer_Details[i]['account_number']==request.form['account_no']) :
                temp=i
    if(temp!=-1) :
        return render_template('balance.html',balance=Customer_Details[temp]['available_balance'])
    else :
        return render_template('balance.html',msg="")

#running tha application on local server
app.run(host="127.0.0.1",port=5000,debug=True)







