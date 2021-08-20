Imports System
Imports System.IO

Public Class frmFileOps
    'Connection string for "txtFile.txt" in root folder with "FileOps.sln"
    'Dim FILE_NAME As String = System.IO.Path.Combine(My.Application.Info.DirectoryPath, "../../../txtFileInRoot-VB.txt")
    'Connection string for "txtFile.txt" in the same folder as "File_Write.exe"
    ReadOnly FILE_NAME As String = System.IO.Path.Combine(My.Application.Info.DirectoryPath, "txtFile.txt") 'in Debug folder
    'absolute path works but is a pain when changing folders
    'Dim FILE_NAME As String = "C:\Users\nevgo\OneDrive - NSW Department of Education and Communities\Code\03-File_ReadWriteAppend\VB-FileOps\File_Write-11-Array\txtFile.txt"

    Private Sub BtnWrite_Click(sender As Object, e As EventArgs) Handles BtnWrite.Click
        'From: http://www.homeandlearn.co.uk/NET/nets8p4.html
        If File.Exists(FILE_NAME) = True Then
            Dim objWriter As New IO.StreamWriter(FILE_NAME, False) 'False cancels append
            objWriter.Write(txtFileMsg.Text) 'add contents of text box if necessary
            objWriter.Close()
            'MessageBox.Show("Text written to file")
        Else
            MessageBox.Show("File Does Not Exist")
        End If
    End Sub
    Private Sub BtnWriteArray_Click(sender As Object, e As EventArgs) Handles BtnWriteArray.Click
        If File.Exists(FILE_NAME) = True Then
            'Create a string array with the lines of text
            Dim lines() As String = {"First line", "Second line", "Third line"}
            Dim objWriter As New IO.StreamWriter(FILE_NAME)
            For Each line As String In lines
                objWriter.WriteLine(line)
                'objWriter.WriteLine(1)
            Next
            objWriter.Write(txtFileMsg.Text) 'add contents of text box if necessary
            objWriter.Close()
            'MessageBox.Show("Text written to file")
        Else
            MessageBox.Show("File Does Not Exist")
        End If
    End Sub
    Private Sub BtnRead_Click(sender As Object, e As EventArgs) Handles BtnRead.Click
        'From: http://www.homeandlearn.co.uk/NET/nets8p2.html
        If File.Exists(FILE_NAME) = True Then
            Dim objReader As New StreamReader(FILE_NAME)
            txtFileMsg.Text = objReader.ReadToEnd
            objReader.Close()
        Else
            MessageBox.Show("File Does Not Exist")
        End If
    End Sub

    Private Sub BtnAppend_Click(sender As Object, e As EventArgs) Handles BtnAppend.Click
        ''From: https://msdn.microsoft.com/en-us/library/system.io.file.appendtext(v=vs.110).aspx
        If Not File.Exists(FILE_NAME) Then
            ' Create a file to write to.
            Using sw As StreamWriter = File.CreateText(FILE_NAME)
                sw.WriteLine("Hello")
                sw.WriteLine("And")
                sw.WriteLine("Welcome")
            End Using
        End If
        ' This text is always added, making the file longer over time 
        ' if it is not deleted.
        Using sw As StreamWriter = File.AppendText(FILE_NAME)
            sw.WriteLine(txtFileMsg.Text)
            'MessageBox.Show("Text added to file")
        End Using
    End Sub
End Class
