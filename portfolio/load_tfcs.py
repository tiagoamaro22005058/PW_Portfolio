import json

from portfolio.models import TFC

with open('data/tfcs_2025.json', encoding='utf-8') as f:
    tfcs = json.load(f)

for item in tfcs:
    TFC.objects.get_or_create(
        titulo=item['titulo'],
        defaults={
            'autores': item.get('autores', ''),
            'orientadores': item.get('orientadores') or '',
            'curso': item.get('curso') or '',
            'ano': item.get('ano', 2025),
            'sumario': item.get('sumario', ''),
            'palavras_chave': ', '.join(item.get('palavras_chave') or []),
            'areas': ', '.join(item.get('areas') or []),
            'tecnologias': ', '.join(item.get('tecnologias') or []),
            'link_pdf': item.get('link_pdf') or '',
            'rating': item.get('rating', 1),
        }
    )

print("TFCs carregados com sucesso!")