import PyPDF2



# ouvrir en mode lecture

directory = "C:\\Users\\manil\\Desktop\\Master_ico\\S2\\amelioration__perso\\python_montly_expenses\\planning_loum07.pdf"

reader = PyPDF2.PdfReader(directory)
writer = PyPDF2.PdfWriter(directory)
meta = reader.metadata

# print(meta.author)
# print(meta.creator)
# print(meta.producer)
# print(meta.subject)
# print(meta.title)

# je récupère la première page
page = reader.pages[0]
# j'affiche le contenu de la page

text = page.extract_text()
# print(text)




# Remplacements souhaités
replacements = {
    "14H15": "07H30",
    "21H15": "21H15",
    "7,00": "13h75"
}


lines = text.splitlines()
# print(len(lines))


# for i, line in enumerate(lines):

#     if line.startswith('Sa1GEANT') and '14H15' in line:
#         # Remplacer '10' par 'vingt'
#         modified_line = line.replace('14H15', '07H30')
#         lines[i] = modified_line
    


# for line in lines:
#     print(line)

   
# Parcourir les lignes et effectuer les remplacements dans la ligne qui commence par "Sa1GEANT"
for i, line in enumerate(lines):
    if line.startswith('Sa1GEANT'):
        for old_value, new_value in replacements.items():
            if old_value in line:
                lines[i] = line.replace(old_value, new_value)

# Reconstruire le texte modifié
modified_text = '\n'.join(lines)

# Afficher le texte modifié
print(modified_text)

# Créer un nouveau fichier PDF avec les modifications
output_directory = "C:\\Users\\manil\\Desktop\\Master_ico\\S2\\amelioration__perso\\python_montly_expenses\\planning_loum07_modified.pdf"
writer = PyPDF2.PdfWriter()
modified_page = PyPDF2._page.PageObject.create_blank_page(None, 900, 900)
modified_page.merge_page(page)
modified_page.extract_text = lambda: modified_text.encode('latin-1', 'replace').decode('latin-1')  # Mettre à jour le texte de la page avec les modifications
writer.add_page(modified_page)
with open(output_directory, 'wb') as output_file:
    writer.write(output_file)

print("Fichier PDF modifié enregistré avec succès.")