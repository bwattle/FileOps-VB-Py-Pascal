<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmFileOps
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(frmFileOps))
        Me.txtFileMsg = New System.Windows.Forms.TextBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.BtnWrite = New System.Windows.Forms.Button()
        Me.BtnRead = New System.Windows.Forms.Button()
        Me.BtnAppend = New System.Windows.Forms.Button()
        Me.BtnWriteArray = New System.Windows.Forms.Button()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'txtFileMsg
        '
        Me.txtFileMsg.Location = New System.Drawing.Point(42, 25)
        Me.txtFileMsg.Multiline = True
        Me.txtFileMsg.Name = "txtFileMsg"
        Me.txtFileMsg.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
        Me.txtFileMsg.Size = New System.Drawing.Size(177, 191)
        Me.txtFileMsg.TabIndex = 0
        Me.txtFileMsg.Text = resources.GetString("txtFileMsg.Text")
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(39, 9)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(95, 13)
        Me.Label1.TabIndex = 1
        Me.Label1.Text = "Text to write in file:"
        '
        'BtnWrite
        '
        Me.BtnWrite.Location = New System.Drawing.Point(42, 271)
        Me.BtnWrite.Name = "BtnWrite"
        Me.BtnWrite.Size = New System.Drawing.Size(177, 28)
        Me.BtnWrite.TabIndex = 2
        Me.BtnWrite.Text = "Wipe and WRITE to file"
        Me.BtnWrite.UseVisualStyleBackColor = True
        '
        'BtnRead
        '
        Me.BtnRead.Location = New System.Drawing.Point(42, 339)
        Me.BtnRead.Name = "BtnRead"
        Me.BtnRead.Size = New System.Drawing.Size(177, 32)
        Me.BtnRead.TabIndex = 3
        Me.BtnRead.Text = "READ from file"
        Me.BtnRead.UseVisualStyleBackColor = True
        '
        'BtnAppend
        '
        Me.BtnAppend.Location = New System.Drawing.Point(42, 378)
        Me.BtnAppend.Name = "BtnAppend"
        Me.BtnAppend.Size = New System.Drawing.Size(177, 32)
        Me.BtnAppend.TabIndex = 4
        Me.BtnAppend.Text = "APPEND to file (or create file)"
        Me.BtnAppend.UseVisualStyleBackColor = True
        '
        'BtnWriteArray
        '
        Me.BtnWriteArray.Location = New System.Drawing.Point(42, 305)
        Me.BtnWriteArray.Name = "BtnWriteArray"
        Me.BtnWriteArray.Size = New System.Drawing.Size(177, 28)
        Me.BtnWriteArray.TabIndex = 5
        Me.BtnWriteArray.Text = "WRITE ARRAY to file"
        Me.BtnWriteArray.UseVisualStyleBackColor = True
        '
        'Label2
        '
        Me.Label2.Enabled = False
        Me.Label2.Location = New System.Drawing.Point(40, 221)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(179, 47)
        Me.Label2.TabIndex = 6
        Me.Label2.Text = "Comment Lines 6 or 8 to change the ""txtFile.txt"" location. Default is in the same" &
    " folder as ""File_Ops.exe"":"
        '
        'frmFileOps
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(6.0!, 13.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(260, 421)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.BtnWriteArray)
        Me.Controls.Add(Me.BtnAppend)
        Me.Controls.Add(Me.BtnRead)
        Me.Controls.Add(Me.BtnWrite)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.txtFileMsg)
        Me.Name = "frmFileOps"
        Me.Text = "v1.01 File Operations"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents txtFileMsg As TextBox
    Friend WithEvents Label1 As Label
    Friend WithEvents BtnWrite As Button
    Friend WithEvents BtnRead As Button
    Friend WithEvents BtnAppend As Button
    Friend WithEvents BtnWriteArray As Button
    Friend WithEvents Label2 As Label
End Class
