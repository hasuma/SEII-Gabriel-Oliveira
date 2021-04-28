"""
https://www.youtube.com/watch?v=zx9OFYy5Xhs - Tutorial
https://www.iconfinder.com/ - Icones
"""

import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, \
                            QPushButton, QLabel, QPlainTextEdit, QStatusBar, QToolBar, \
                            QVBoxLayout, QAction, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase, QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog

class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NotePad')
        self.setWindowIcon(QIcon('./Icons/notepad.png'))
        self.screen_width, self.screen_height = self.geometry().width(), self.geometry().height()
        self.resize(self.screen_width * 2, self.screen_height * 2)

        self.filterTypes = 'Text Document (*.txt) ;; Python (*.py) ;; Markdown (*.md)'

        self.path = None

        fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedFont.setPointSize(12)

        mainLayout = QVBoxLayout()

        # editor
        self.editor = QPlainTextEdit()
        self.editor.setFont(fixedFont)
        mainLayout.addWidget(self.editor)

        # statusBar
        self.statusBar = self.statusBar()

        # app container
        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)
        
        # --------------------------------
        # File Menu
        # --------------------------------
        file_menu = self.menuBar().addMenu('&File')

        # --------------------------------
        # File ToolBar
        # --------------------------------
        file_toolbar = QToolBar('File')
        file_toolbar.setIconSize(QSize(30,30))
        self.addToolBar(Qt.BottomToolBarArea, file_toolbar)
     
        # Open, Save, Save As, Print Action (Print Document)
        open_file_action = QAction(QIcon('./Icons/file_open.png'), 'Open File...', self)
        open_file_action.setStatusTip('Open file...')
        open_file_action.setShortcut(QKeySequence.Open)
        open_file_action.triggered.connect(self.file_open)

        save_file_action = self.create_action(self,'./Icons/save_file.png', 'Save File', 'Save file', self.file_save)
        save_file_action.setShortcut(QKeySequence.Save)

        save_fileAs_action = self.create_action(self,'./Icons/save_as_file.png', 'Save File As...', 'Save file as...', self.file_saveAs)
        save_fileAs_action.setShortcut(QKeySequence('Ctrl+Shift+S'))

        print_action = self.create_action(self, './Icons/printer.png', 'Print File', 'Print file', self.print_file)
        print_action.setShortcut(QKeySequence.Print)

        file_menu.addActions([open_file_action,save_file_action,save_fileAs_action, print_action])
        file_toolbar.addActions([open_file_action,save_file_action,save_fileAs_action, print_action])

        # --------------------------------
        # Edit Menu
        # --------------------------------
        edit_menu = self.menuBar().addMenu('&Edit')
        # --------------------------------
        # Edit ToolBar
        # --------------------------------
        edit_toolbar = QToolBar('Edit')
        edit_toolbar.setIconSize(QSize(30,30))
        self.addToolBar(Qt.BottomToolBarArea, edit_toolbar)

        # Undo, Redo, Clear action
        undo_action = self.create_action(self, './Icons/undo.png', 'Undo', 'Undo', self.editor.undo)
        undo_action.setShortcut(QKeySequence.Undo)

        redo_action = self.create_action(self, './Icons/redo.png', 'Redo', 'Redo', self.editor.redo)
        redo_action.setShortcut(QKeySequence.Redo)

        clear_action = self.create_action(self, './Icons/clear.png', 'Clear', 'Clear', self.clear_content)

        edit_menu.addActions([undo_action,redo_action,clear_action])
        edit_toolbar.addActions([undo_action,redo_action,clear_action])
        
        # Add separator
        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

        # Cut, Copy, Paste, Select all actions
        cut_action = self.create_action(self, './Icons/cut.png', 'Cut', 'Cut', self.editor.cut)
        copy_action = self.create_action(self, './Icons/copy.png', 'Copy', 'Copy', self.editor.copy)
        paste_action = self.create_action(self, './Icons/paste.png', 'Paste', 'Paste', self.editor.paste)
        select_all_action = self.create_action(self, './Icons/select_all.png', 'Select All', 'Select all', self.editor.selectAll)
        
        cut_action.setShortcut(QKeySequence.Cut)
        copy_action.setShortcut(QKeySequence.Copy)
        paste_action.setShortcut(QKeySequence.Paste)
        select_all_action.setShortcut(QKeySequence.SelectAll)

        edit_menu.addActions([cut_action,copy_action,paste_action,select_all_action])
        edit_toolbar.addActions([cut_action,copy_action,paste_action,select_all_action])

        # Add separator
        edit_menu.addSeparator()
        edit_toolbar.addSeparator()

        # Wrap text
        wrap_text_action = self.create_action(self, './Icons/wrap_text.png', 'Wrap Text', 'Wrap text', self.toggle_wrap_text)
        wrap_text_action.setShortcut(QKeySequence('Ctrl+Shift+W'))

        edit_menu.addAction(wrap_text_action)
        edit_toolbar.addAction(wrap_text_action)


    def toggle_wrap_text(self):
        self.editor.setLineWrapMode(not self.editor.lineWrapMode())

    def clear_content(self):
        self.editor.setPlainText('')

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Open file',
            directory='',
            filter=self.filterTypes
        )
        if path:
            try:
                with open(path, 'r') as f:
                    text = f.read()
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            self.file_saveAs()
        else:
            try:
                text = self.editor.toPlainText()
                with open(self.path, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))

    def file_saveAs(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            'Save file as...',
            '',
            self.filterTypes
        )
        text = self.editor.toPlainText()

        if not path:
            return
        else:
            try:
                with open(path, 'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))
            else:
                self.path = path
                self.update_title()

    def print_file(self):
        printDialog = QPrintDialog()
        if printDialog.exec_():
            self.editor.print_(printDialog.printer())

    def update_title(self):
        self.setWindowTitle('{0} - NotePadG'.format(os.path.basename(self.path) if self.path else 'Unittled'))

    def dialog_message(self, message):
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.setIcon(QMessageBox.Critical)
        dlt.show()


    def create_action(self, parent, icon_path, action_name, set_status_tip, triggered_method):
        action = QAction(QIcon(icon_path), action_name, parent)
        action.setStatusTip(set_status_tip)
        action.triggered.connect(triggered_method)
        return action








if __name__ == '__main__':
    app = QApplication(sys.argv)
    notePad = AppDemo()
    notePad.show()
    sys.exit(app.exec_())
