from PyQt5.QtWidgets import QWidget ,QApplication, QListWidget ,QTextEdit ,QPushButton ,QLineEdit ,QHBoxLayout ,QVBoxLayout, QInputDialog
 
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

line1.addWidget(text) 
line2.addWidget(notes_list) 
line2.addWidget(btn1) 
line2.addWidget(btn2) 
line2.addWidget(btn3)
line2.addWidget(tags_list)
line2.addWidget(lineText)  

line2.addWidget(btn1) 
line2.addWidget(btn2) 
line2.addWidget(btn3) 
line2.addWidget(btn4) 
line2.addWidget(btn5) 
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
    note_text = text.toPlainText() 
    note_name = notes_list.currentItem().text()
    notes[note_name]['text'] = note_text 

    writefile() 
notes = {}

def add_note():
     
    note_name, ok = QInputDialog.getText (window, "нова замітка" , "Назва замітки") 
    if ok and note_name != "":
        notes[note_name]= {
        "text": "", 
        "tags" : [], 
        }

    notes_list.addItem(note_name)  

with open("notes.json", "r", encoding="utf-8") as file: 
    notes = json.load(file)
notes_list.addItems(notes)

btn1.clicked.connect(add_note)
btn3.clicked.connect(save_note)
window.setLayout(main_line)
window.show()
app.exec_() 
