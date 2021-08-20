program Sum_Numbers_To_X (input,output);
uses crt;
Var FileName, Txt : String;
    UserFile   : Text;
Begin
clrscr;
	FileName := 'TxtFile'; {file_name is the actual name of the file to be read from}
	Assign(UserFile,'U:\sdd\'+FileName+'.txt'); {assign a text file}
	Rewrite(UserFile); {open the file 'FileName' for writing}
	Writeln(UserFile,'Welcome to SDD');
	Writeln(UserFile,'This is the second line of the file');
	Writeln(UserFile,'obviously this is the third');
	Writeln('Write some text to be written to the file');
	Readln(Txt);
	Writeln(UserFile,'');
	Writeln(UserFile,'You entered this text:');
	Writeln(UserFile,Txt);
	Close(UserFile);
End.