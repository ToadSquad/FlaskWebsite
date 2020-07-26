

class Website():
    def __init__(self):
        
        self.fileloc = "FlaskBackend.py"
        self.file = open(self.fileloc,"w")
        self.file.write('''
        from flask import Flask
        app = Flask(__name__)
        
        class FlaskSite():
            def __init__(self):
                app.run(debug=False)'''
        )
    def addPage(self,route):
        funcname = route.replace('/','')
        strToAdd = """
        @route('"""+route+"""')
        def """+funcname+"""():
        
        #End of Function
        """
        self.file.write(strToAdd)
    def setOutputFile(self,fileloc):
        self.fileloc = fileloc
        self.file = open(self.fileloc,'w')


class Html():
    def table(self,type,diction):
        text = '''<table class="'''+type+'''">
        <thead>
        <tr>
        '''
        for column in diction:
            text = text + "<th>"+column+"</th>\n"
        text = text+" </thead>\n"
        for column in diction:
            text = text + '''
            <tbody>
            <tr>'''
            for item in diction[column]:
                text = text + "<td>"+item+"</td>\n"
website = Website()
website.addPage('/')




