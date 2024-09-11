ship = 'Titanic'
print(ship)
ship = "Titanic"
print(ship)
ship = """Titanic"""
print(ship)

# Vaak zul je quotes in een string moeten gebruiken. Dit kan met de escape character \, of door de string met enkele quotes te omringen
zonder_escape = 'This is a "good" plan'
print(zonder_escape)
met_escape = "This is a \"good\" plan"
print(met_escape)

# Gebruik """ """ als je meerdere regels tekst moet tonen
paragraph = """Computer Technology means all designs, drawings, procedures (including design, manufacturing, test and maintenance procedures), specifications, software (other than as described within the meaning of the term "Software" defined elsewhere herein), printed circuit board art work, integrated circuit masks, test equipment, tools, fixtures, documentation, training materials, and information, in whatever form, related to, useful, utilizable or necessary in the design, manufacture, test and/or maintenance of the computer system, or relate to any Technology Licenses."""
print(paragraph)
# With the len() function you can ask how many characters the string has
characters_in_paragraph = len(paragraph)
print(f"{paragraph}\n\nThe paragraph has {characters_in_paragraph} characters.")

year = 1936
inventor = "Alan Turing"
name_of_machine = "automatic machine"
invention = f'The Turing machine was invented in {year} by {inventor}, who called it an "a-machine" ({name_of_machine})'
print(invention)