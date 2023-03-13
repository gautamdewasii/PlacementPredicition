import numpy as np
import pickle
import streamlit as stl
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()


# loading model file into program
loaded_model=pickle.load(open('Pmodel.sav','rb'))

# function for prediction
# 'input_data' is the data that we will input using web app
def placementPredicition(age,gender,stream,internships,cGPA,hostel,historyOfBacklogs):


    input_data=np.array([[age,gender,stream,internships,cGPA,hostel,historyOfBacklogs]])
    input_data=scalar.fit_transform(input_data)
    pred = loaded_model.predict(input_data)


    if(pred==1):
        return "You have high chances of getting placed😃"
    else:
        return "Needed more Hard Work... But I Believe in you😊"


# main() function for web app interface and input tasks

def main():

    # title
    stl.title('🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻')
    stl.title('Placement Predicition ML Model')
    stl.title('🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻🔻')

    # Getting input data from the users
    age=stl.text_input('Age',00)
    gender=stl.radio('Gender',('M','F'))
    stream=stl.selectbox('Stream',('EC','CS','IT','ME','Electrical','CE'))
    stl.text('NOTE :- EC -> Electronics And Communication')
    stl.text('NOTE :- ME -> Mechanical')
    stl.text('NOTE :- CE -> Civil')
    
    internships=stl.text_input('Internship',00)
    cGPA=stl.slider('CGPA',0,10,6)
    hostel=stl.selectbox('Hostel ( 1->YES/ 0->NO )',(0,1))
    historyOfBacklogs=stl.text_input('Backlogs',00)


    age=int(age)
    if(gender=='M'):
        gender=1
        gender=int(gender)
    elif(gender=='F'):
        gender=0
        gender=int(gender)
    if(stream=='EC'):
        stream_no=1
    elif(stream=='CS'):
        stream_no=2
    elif(stream=='IT'):
        stream_no=3
    elif(stream=='ME'):
        stream_no=4
    elif(stream=='Electrical'):
        stream_no=5
    elif(stream=='CE'):
        stream_no=6
        
    stream_no=int(stream_no)
    
    internships= int(internships)
    cGPA=int(cGPA)
    hostel=int(hostel)
    historyOfBacklogs=int(historyOfBacklogs)

    # code for predicition
    placedOrNot= ''

    # creating button for prediction

    if stl.button('Click for prediciton'):
        placedOrNot=placementPredicition(age,gender,stream_no,internships,cGPA,hostel,historyOfBacklogs)
    

    stl.success(placedOrNot)


if __name__ == '__main__':
    main()

