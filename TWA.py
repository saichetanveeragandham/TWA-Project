import snowflake.connector
from tkinter import *
#connection to database established with credentials
try:
    con_eb = snowflake.connector.connect(user='NavyaNelluri',
                                     password='Navya.c@698',
                                     account='ujlmjrs-rx06772',
                                         database='PROJECT_TWA',
                                         schema = "PROJECT_TWA_SCHEMA"
                                     ) 
except Exception as e:
    print(str(e))
cs=con_eb.cursor()
print(cs)
cs.execute("SELECT * FROM PROJECT_TWA.PROJECT_TWA_SCHEMA.JobSeeker")
jobSeeker_result=cs.fetchone();
print(jobSeeker_result)
cs.execute(" select * from PROJECT_TWA.PROJECT_TWA_SCHEMA.JOBDETAILS")
JobDetails_result=cs.fetchone();
print(JobDetails_result)
def option_selected(*args):
    selected_option = variable.get()
    if selected_option != "select jobseeker":
        label1.config(text="Selected Job Seeker: " + selected_option)
        label2.config(text = "Available Jobs: " + JobDetails_result[4] )
    else:
        label1.config(text="")
        label2.config(text="Sorry! No matching jobs")
        
        
master = Tk()
master.geometry("400x300")  # Set the default size to 400 pixels wide and 300 pixels high
master.title("Project_TWA")

variable = StringVar(master)
variable.set("select jobseeker") # default value
variable.trace("w", option_selected) 

w = OptionMenu(master, variable, jobSeeker_result[0])
w.pack()

label1 = Label(master, text="")
label1.pack()

label2 = Label(master, text="")
label2.pack()

mainloop()