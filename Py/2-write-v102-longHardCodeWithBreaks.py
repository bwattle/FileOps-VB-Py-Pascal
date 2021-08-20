text_file = open("textFile.txt", "w")
text_file.write("This text is written from v1.02 of the Python Write file. Here is some filler text: Some text to enable \nscrolling.. Lorem ipsum dolor sit amet, illum definitiones no quo, \nmaluisset concludaturque \net eum, altera fabulas ut quo. Atqui causae gloriatur ius te, id agam omnis evertitur eum. Affert laboramus repudiandae nec et. Inciderint efficiantur his ad. Eum no molestiae voluptatibus. \n Some text to enable scrolling.. Lorem ipsum dolor sit amet, illum definitiones no quo, maluisset concludaturque et eum, altera fabulas ut quo. Atqui causae gloriatur ius te, id agam omnis evertitur eum. Affert laboramus repudiandae nec et. Inciderint efficiantur his ad. Eum no molestiae voluptatibus.")
text_file.write("This text is broken into short lines in the editor." 
                + " \nHere is some filler text: Some text to enable scrolling.. " 
                + " \nLorem ipsum dolor sit amet, illum definitiones no quo, maluisset " 
                + " \nconcludaturque et eum, altera fabulas ut quo. Atqui causae " 
                + " \ngloriatur ius te, id agam omnis evertitur eum. Affert laboramus " 
                + " \nrepudiandae nec et. Inciderint efficiantur his ad. Eum no molestiae " 
                + " \nvoluptatibus. \n Some text to enable scrolling.. Lorem ipsum dolor " 
                + " \nsit amet, illum definitiones no quo, maluisset concludaturque et " 
                + " \neum, altera fabulas ut quo. Atqui causae gloriatur ius te, id agam " 
                + " \nomnis evertitur eum. Affert laboramus repudiandae nec et. Inciderint " 
                + " \nefficiantur his ad. Eum no molestiae voluptatibus.")

text_file.close()