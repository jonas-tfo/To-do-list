import PySimpleGUI as sg

'''
ADD AUTO SAVE

'''

sg.theme('DarkAmber')   # Add a touch of color

pathinput1 = sg.Input(visible=True, enable_events=True, key='pathinput1', expand_x=True)
pathinput2 = sg.Input(visible=False, enable_events=True, key='pathinput2', expand_x=True)

textbox1 = sg.Multiline("", size=(45, 45), font= ('Arial', 14), enable_events=True, key='TEXTBOX1',
                        expand_x=True, expand_y=True, justification="left") 

textbox2 = sg.Multiline("", size=(45, 45), font= ('Arial', 14), enable_events=True, key='TEXTBOX2',
                        expand_x=True, expand_y=True, justification="left")

textbox3 = sg.Multiline("", size=(45, 45), font= ('Arial', 14), enable_events=True, key='TEXTBOX3',
                        expand_x=True, expand_y=True, justification="left")  


tab1_layout = [[textbox1]]    # each gets a multiline textbox

tab2_layout = [[textbox2]]  

tab3_layout = [[textbox3]]             

# the layout
layout = [  [sg.FileBrowse(), pathinput1],
            [sg.TabGroup([[sg.Tab('Uni', tab1_layout, key='tab1'),                # three tabs for dif topics
                           sg.Tab('Work', tab2_layout, key='tab2'),
                           sg.Tab('Other', tab3_layout, key='tab3')]],
                           enable_events=True, 
                           key='my_tabs')],                                                    # the text box
            [pathinput2, sg.FileSaveAs(), sg.Button('Close')]                        # save and close buttons
                                   
        ]

# Create the Window
window = sg.Window('To-do list', layout, default_element_size=(12,1))


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    try:
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
    except TypeError:
        pass

    if event in (None, 'Close'):  # if user closes window or clicks cancel
        break

window.close()
