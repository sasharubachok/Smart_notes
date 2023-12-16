from PyQt5.QtWidgets import QWidget ,QApplication, QListWidget ,QTextEdit , QMessageBox, QPushButton ,QLineEdit ,QHBoxLayout ,QVBoxLayout, QInputDialog
 
import json
app = QApplication([]) 
window = QWidget ()

text = QTextEdit()
lineText = QLineEdit() 
notes_list = QListWidget()
tags_list = QListWidget()

btn1 = QPushButton("Створити замітку")
btn2 = QPushButton("Вiдкрипити замітку") 
btn3 = QPushButton("Зберегти замітку") 
btn4 = QPushButton("Додати до замітки") 
btn5 = QPushButton("Відкріпити від замітки") 
btn6 = QPushButton("Шукати замітки по тегу") 

main_line = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()
btn1.setStyleSheet('''
background-color: #5c96b5
''') 
btn2.setStyleSheet('''
background-color: #5c96b5
''')  
btn3.setStyleSheet('''
background-color: #5c96b5
''') 
window.setStyleSheet(''' 
  background-color: #427196                   
 ''') 
btn4.setStyleSheet('''
background-color: #5c96b5
''') 
btn5.setStyleSheet('''
background-color: #5c96b5
''') 
btn6.setStyleSheet('''
background-color: #5c96b5
''') 
line1.addWidget(text) 
line2.addWidget(notes_list) 
 
h_line = QHBoxLayout()

h_line.addWidget(btn1)
h_line.addWidget(btn2) 

line2.addLayout(h_line)
line2.addWidget(btn3)
line2.addWidget(tags_list)
line2.addWidget(lineText)  

h_line2 = QHBoxLayout() 
h_line2.addWidget(btn5) 
h_line2.addWidget(btn4) 
line2.addLayout(h_line2)

line2.addWidget(btn6)



main_line.addLayout(line1)
main_line.addLayout(line2) 
def writefile(): 
    with open("notes.json", "w" , encoding="utf-8") as file: 
        json.dump(notes, file, ensure_ascii=True, sort_keys=True, indent=4)

def show_note():
    note_name = notes_list.currentItem.text()
    text.setText(notes[note_name]['text'])
def save_note(): 
    try:
        note_text = text.toPlainText() 
        note_name = notes_list.currentItem().text()
        notes[note_name]['text'] = note_text 
        writefile() 
    except:
        msg = QMessageBox(window, text="Виберіть замітку") 
        msg.show() 

notes = {}

def add_note():
     
    note_name, ok = QInputDialog.getText (window, "нова замітка" , "Назва замітки") 
    if ok and note_name != "":
        notes[note_name]= {
        "text": "", 
        "tags" : [], 
        }
def add_tag(): 
    note_name = notes_list.currentItem().text()
    tag = lineText.text() 
    notes[note_name]["tags"].append(tag) 
    
    writefile() 


def search_note_bytag():
    tag = lineText.text() 
    if(btn6.text()=="Search"):
        fillered = {}
        for key in notes: 
            if tag in notes[key]['tags']:
                fillered[key] = notes[key] 
        btn6.setText("ВІдмінити пошук?") 

    else: 
        btn6.setText("Search")
        notes_list.clear() 
        notes_list.addItems(fillered) 
        tags_list.clear() 
        lineText.clear() 

btn6.clicked.connect(search_note_bytag)

def del_tag(): 
    note_name = notes_list.currentItem().text() 
    tag_name = tags_list.currentItem().text() 
    notes[note_name]["tags"].remove(tag_name) 
try:    
    with open("notes.json", "r", encoding="utf-8") as file: 
        notes = json.load(file)
        notes_list.addItems(notes)

except:
    print("file not found")   

btn1.clicked.connect(add_note)
btn3.clicked.connect(save_note)
window.setLayout(main_line)
window.show()
app.exec_() 


