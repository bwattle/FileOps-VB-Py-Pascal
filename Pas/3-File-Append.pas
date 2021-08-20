program AppendFile (input,output);
uses crt;
Var UserFile : Text;
    Text: string;
Begin
	Assign(UserFile,'C:\SDD\ADDTEXT.TXT');
	append(UserFile);
	Writeln(UserFile,'You added this line');
	Writeln('Enter a word or two');
	Readln(Text);
	Writeln(UserFile,'');
	Writeln(UserFile,'You entered this text:');
	Writeln(UserFile,Text);
	Close(UserFile);
End.