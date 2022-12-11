
import streamlit as st
from db_fxns import * 
import streamlit.components.v1 as stc

HTML_BANNER = """
    <div style="background-color:#a8d8ea;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">TO DO LIST</h1>
    </div>
    """
def data_value(item):
	html_str = f"""
	<div style="max-width: 400px;margin: 50px auto;background: white;border-radius: 5px;box-shadow: 5px 5px 15px -5px rgba(0, 0, 0, 0.3)">
 		<div style="min-height: 70px;display: flex;align-items: center;border-bottom: 1px solid #f0eeee;">
            <h2 style="color:black;text-align:center;">{item}</h2>
  	</div>
	</div>
	"""
	st.markdown(html_str, unsafe_allow_html=True)

def add_bg():
  st.markdown(
         f"""
         <style>
         .stApp {{
              background-color: #E4E9FD;
  						background-image: -webkit-linear-gradient(65deg, #a8d8ea 50%, #e4f3f8 50%);
  						min-height: 1000px;
         			}}
         </style>
         """,
         unsafe_allow_html=True)

def main():
	stc.html(HTML_BANNER)
	add_bg()
	menu = ["VIEW TASK","ADD TASK","REMOVE TASK"]
	choice = st.sidebar.selectbox("Menu",menu)
	create_table()
	if choice=="VIEW TASK":
		result = view_all_data()
		for i in result:
			data_value(i[0])
	elif choice=="ADD TASK":
		st.subheader("Add Item")
		task = st.text_area("Task To Do")
		task = str(task)
		if st.button("Add Task"):
			add_data(task)
			st.success("Added ::{} ::To Task".format(task))
	elif choice=="REMOVE TASK":
		unique_list = [i[0] for i in view_all_task_names()]
		delete_by_task_name =  st.selectbox("Select Task",unique_list)
		if st.button("Delete"):
			delete_data(delete_by_task_name)
			st.warning("Deleted: '{}'".format(delete_by_task_name))
	


if __name__ == '__main__':
	main()
