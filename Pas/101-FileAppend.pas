Program AppendToFile;
// https://wiki.freepascal.org/File_Handling_In_Pascal
Uses
Sysutils;
Const
  C_FNAME = 'textfile.txt';
Var
  tfOut: TextFile;
Begin
  // Set the name of the file that will receive some more text
  AssignFile(tfOut, C_FNAME);
  // Embed the file handling in a try/except block to handle errors gracefully
  Try
    // Open the file for appending, write some more text to it and close it.
    Append(tfOut);
    Writeln(tfOut, 'Hello again textfile!');
    Writeln(tfOut, 'The result of 6 * 7 = ', 6 * 7);
    CloseFile(tfOut);
  Except
    on E: EInOutError Do
          Writeln('File handling error occurred. Details: ', E.Message);
End;
// Give feedback and wait for key press
Writeln('File ', C_FNAME, ' might have more text. Press enter to stop.');
Readln;
End.
