#-*- coding: utf-8 -*-
import streamlit as st
import functions

def add_todo():
    new_todo = st.session_state["add_todo"] + "\n"
    print(new_todo)
    todos.append(new_todo)
    functions.write_todos(todos)

todos=functions.get_todos()

#st.title("Prueba de acentuación: á, é, í, ó, ú, ñ")
#st.subheader("Aclaración")
st.write("Incrementa la productividad")

for index, todo in enumerate(todos):
    chk_eliminar = st.checkbox(todo, key=todo)
    if chk_eliminar:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="Informa", placeholder="Ingrese el nombre del archivo",
              on_change=add_todo, key='add_todo')

#print("probando")
#st.session_state
