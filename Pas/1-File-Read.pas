program Sum_Numbers_To_X (input,output);
uses crt;
Var UserFile : Text;
Var FileName, TFile : String;
Begin
	//Writeln('Enter the file name (with its full path) of the text file:');
	//readln(FileName); {A .txt file will be assigned to a text variable}
	Assign(UserFile, FileName + '.txt');
	Reset(UserFile); {'Reset(x)' - means open the file x}
	Repeat
		Readln(UserFile,TFile);
		Writeln(TFile);
	Until Eof(UserFile);
	Close(UserFile);
	//Readln();
End.