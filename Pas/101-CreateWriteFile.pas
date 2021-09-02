Program CreateFile;
// https://wiki.freepascal.org/File_Handling_In_Pascal
Uses
Sysutils;
Const
  C_FNAME = 'textfile.txt';
Var
  tfOut: TextFile;
Begin
  // Set the name of the file that will be created
  AssignFile(tfOut, C_FNAME);
  // Use exceptions to catch errors (this is the default so not absolutely requried)
 {$I+}
  // Embed the file creation in a try/except block to handle errors gracefully
  Try
    // Create the file, write some text and close it.
    Rewrite(tfOut);
    Writeln(tfOut, 'Hello textfile!');
    Writeln(tfOut, 'The answer to life, the universe and everything: ', 42);
    CloseFile(tfOut);
  Except
    // If there was an error the reason can be found here
    on E: EInOutError Do
          Writeln('File handling error occurred. Details: ', E.ClassName, '/', E.Message);
End;
// Give feedback and wait for key press
Writeln('File ', C_FNAME, ' created if all went ok. Press Enter to stop.');
Readln;
End.
