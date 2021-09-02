Program ReadFile;
// https://wiki.freepascal.org/File_Handling_In_Pascal
Uses
Sysutils;
Const
  C_FNAME = 'textfile.txt';
Var
  tfIn: TextFile;
  s: String;
Begin
  // Give some feedback
  Writeln('Reading the contents of file: ', C_FNAME);
  Writeln('=========================================');
  // Set the name of the file that will be read
  AssignFile(tfIn, C_FNAME);
  // Embed the file handling in a try/except block to handle errors gracefully
  Try
    // Open the file for reading
    Reset(tfIn);
    // Keep reading lines until the end of the file is reached
    While Not Eof(tfIn) Do
      Begin
        Readln(tfIn, s);
        Writeln(s);
      End;
    // Done so close the file
    CloseFile(tfIn);
  Except
    on E: EInOutError Do
          Writeln('File handling error occurred. Details: ', E.Message);
End;
// Wait for the user to end the program
Writeln('=========================================');
Writeln('File ', C_FNAME, ' was probably read. Press enter to stop.');
Readln;
End.
