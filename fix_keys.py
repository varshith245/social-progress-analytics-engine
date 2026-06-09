import os
path = r'd:\social-progress-analytics\utils\charts.py'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    '"card_bg"': '"bg_card"',
    '"text"': '"text_primary"',
    '"background"': '"bg_primary"',
    '"primary"': '"accent_blue"',
    '"secondary"': '"accent_teal"',
    '"accent"': '"accent_coral"',
    "'card_bg'": "'bg_card'",
    "'text'": "'text_primary'",
    "'background'": "'bg_primary'",
    "'primary'": "'accent_blue'",
    "'secondary'": "'accent_teal'",
    "'accent'": "'accent_coral'"
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print('Replacements done.')
