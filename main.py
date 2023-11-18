from PyQt5.QtWidgets import QWidget ,QApplication, QListWidget ,QTextEdit ,QPushButton ,QLineEdit ,QHBoxLayout ,QVBoxLayout

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

window.setLayout(main_line) 

window.show()
app.exec_() 
