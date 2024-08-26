import PySimpleGUI as sg
import os

'''
simple custom text editor UI with multiple tabs that autosaves to file and can import textfiles
'''

# AUTOSAVE FUNCTION
def autosave(filename, values, textboxnumber):

    desktoppath = os.path.join(os.path.expanduser('~'), 'Desktop') 

    filepath = os.path.join(desktoppath, filename)

    try:
        # Open the file in write mode, which will create it if it doesn't exist
        with open(filepath, "w") as file:
            file.write(values[f'TEXTBOX{textboxnumber}'])

    except TypeError:
        pass


# STARTUP FUNCTION // write before read!

def startup(filename, window, textboxnumber):              

    desktoppath = os.path.join(os.path.expanduser('~'), 'Desktop') 
    filepath = os.path.join(desktoppath, filename)


    if not os.path.exists(filepath):
        with open(filepath, 'w') as writetofile:
            writetofile.write('')

    ## importing text 
    with open(filepath, 'r') as fileread:
        txt = fileread.read()
        window[f'TEXTBOX{textboxnumber}'].update(value = txt)


'''
---------------------------------------------------------
'''


sg.theme('TealMono')   # add color theme

# for the import and export of text from and to files
pathinput1 = sg.Input(visible=True, enable_events=True, key='pathinput1', expand_x=True)
pathinput2 = sg.Input(visible=False, enable_events=True, key='pathinput2', expand_x=True)

# define the parameters of the text boxes for each tab
textbox1 = sg.Multiline("", size=(45, 47), font= ('Arial', 14), enable_events=True, key='TEXTBOX1',
                        expand_x=True, expand_y=True, justification="left") 
textbox2 = sg.Multiline("", size=(45, 47), font= ('Arial', 14), enable_events=True, key='TEXTBOX2',
                        expand_x=True, expand_y=True, justification="left")
textbox3 = sg.Multiline("", size=(45, 47), font= ('Arial', 14), enable_events=True, key='TEXTBOX3',
                        expand_x=True, expand_y=True, justification="left")  

# each gets a multiline textbox
tab1_layout = [[textbox1]]    

tab2_layout = [[textbox2]]  

tab3_layout = [[textbox3]]             

# defines the layout
layout = [  [sg.FileBrowse('Open File'), pathinput1],
            [sg.TabGroup([[sg.Tab('Uni', tab1_layout, key='tab1'),                # three tabs for dif topics
                           sg.Tab('Work', tab2_layout, key='tab2'),
                           sg.Tab('Other', tab3_layout, key='tab3')]],
                           enable_events=True, 
                           key='my_tabs')],                                                    
            [pathinput2, sg.FileSaveAs(), sg.Button('Close')]                        # save and close buttons
                                   
        ]

# Create the Window
window = sg.Window('To-do list', layout, default_element_size=(12,1), finalize=True)    

# reads the text from the saved files and saves it to corresponding text window
startup('UniList.txt', window, 1)          
startup('WorkList.txt', window, 2)
startup('OtherList.txt', window, 3)


# Event Loop to process "events" and get the "values" of the inputs
while True:

    event, values = window.read()

    # if user closes window or clicks cancel 
    if event in (sg.WINDOW_CLOSED, 'Close', None):  
        break


    # prompt to get username from user
    autosave('UniList.txt', values, 1)          # SAVES EACH TEXT TO FILE FOR EACH LOOP ITERATION
    autosave('WorkList.txt', values, 2)
    autosave('OtherList.txt', values, 3)

   
    active_tab = values['my_tabs']

    ## tab1
    if active_tab == 'tab1':

        if event == 'pathinput1':
            file = open(values['pathinput1'])
            txt = file.read()
            window['TEXTBOX1'].update(value=txt)

        if event == 'pathinput2':
            file = open(values['pathinput2'], "w")
            file.write(values['TEXTBOX1'])
            file.close()


    ## tab2
    if active_tab == 'tab2':

        if event == 'pathinput1':
            file = open(values['pathinput1'])
            txt = file.read()
            window['TEXTBOX2'].update(value=txt)

        if event == 'pathinput2':
            file = open(values['pathinput2'], "w")
            file.write(values['TEXTBOX2'])
            file.close()

    ## tab3
    if active_tab == 'tab3':

        if event == 'pathinput1':
            file = open(values['pathinput1'])
            txt = file.read()
            window['TEXTBOX3'].update(value=txt)

        if event == 'pathinput2':
            file = open(values['pathinput2'], "w")
            file.write(values['TEXTBOX3'])
            file.close()


window.close()

