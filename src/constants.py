from datetime import datetime

# initial set up items
today = datetime.now()
date_for_file = today.strftime('%m%d%Y%H%M%S')
logo_file_name = 'hv_logo_sized_201_53.png'
tmp_xlsx_name = 'Wholesale_Order_Form.xlsx'
sheet_name = 'HVVWSGoodsOrderingSheet'
ws_order_form_name = f'Wholesale_Order_Form_{date_for_file}.xlsx'
strain_no_sale_list = ['DX4', 'Larry Berry', 'Black Magic', 'Chocolate Pie', 'Dosidos',
                       'Musk #1', 'Mimosa EVO', 'Ice Cream Cake',
                       '"Starting Line Up" - Another Level - Banana Jealousy - Hash Burger - Sugar Shack #5 - Super Lemon Haze']

no_harvest_date = ['PR5-2.5', 'PR5-5','PR2-.5-3PMZ', 'PR2-.5-INFSD-3PMZ', 'MZ-7G-CGRP', 'MZ-7G-HMLN',
                   'MZ-7G-LMND', 'MZ-7G-STRP', 'MZ-7G-SWTM', 'MZ-7G-WLDB', 'PR-MNR', 'FP-MNR', 'FP-MNR-STR', 'PR-MNR-STR', 'PURET-500', 'PURET-TERP-500', 'RSLV-1:1-250',
               'RSO-TINC-500', 'REMT-1:1-250', 'HVG-6-SEEDPACK-AUTO', 'HVG-6-SEEDPACK-PHOTO', 'HM-DSP-LVO-.5G', 'HM-DSP-LVO-1G', 'LVO-CART-.5', 'LVO-CART-1',
               'LHR-CART-.5', 'SS-50', 'CFX-SS-50', 'GUM100-CFX-CALM', 'GUM100-CFX-ENERGY', 'GUM100-CFX-FOCUS',
               'GUM100-CFX-SLEEP', 'GUM100-CFX-20:1', 'GUM100-CFX-RELIEF', 'GUM5-CFX-20:1-P', 'GUM100-RAPID', 'FD100', 'GUM-HR-50', 'GUM-HR-100',
               'GUM100', 'CHOC100', 'GUM400', 'GUM1000', 'CHOC400', 'CHOC1000', 'LHR-COLDCURE', 'LHR-JAM', 'TRD-HASH', 'PR-1.2-TID-INFSD']

# dataframe final column order
final_col_order = ['Product Description', 'Strain/Flavor', 'I/S/H', 'TAC', 'THC-A', 'Total THC', 'Total Terpenes', 'Harvest Date',
                   'Net Weights/Volumes', 'Servings', 'Price/EA', 'Case Count', 'Qty. Available', 'Available (CASE)', 'Price/Case', 'Order Quantity (CASE)', 'Total', ' ']

# strain to I/S/H mapping
ish_dict = {'Candy Games #25':'S', 'Candy Store #25':'S', 'Sugar Shack #5':'S', 'Super Lemon Haze':'S', 'Game Over':'S', 'Banana Shack':'S',
            'End Game Cookies':'H/S', 'Little Tokyo':'H/S', 'MAC1':'H/S', 'Overtime':'H/S', 'Sourchillz':'H/S', 'Splash':'H/S', 
            'Banana Jealousy':'H', 'Candy Store #38':'H', 'Rainbow Belts 3.0':'H', 'Glue':'H', 'T. SAGE':'H',
            'Another Level':'H/I', 'Big Bad Wolf':'H/I', 'Candy Games #38':'H/I', 'Cross Town Traffic':'H/I', 'Dirty Taxi':'H/I', 'Dubble Tropicanna':'H/I',
            'Galatic Warheads':'', 'Garlic Icing':'H/I', 'Kush Mints x Jealousy':'H/I', 'Kut Throat Kandy':'H/I', 'Permanent Marker':'H/I', 'Sunset Sherbet':'H/I',
            'White Truffle':'H/I', 'GMO Zkittlez':'I', 'Hash Burger':'I', 'Melon Baller':'I', 'Motorbreath #15':'I', 'Stardawg':'I',
            'White Wedding':'I', 'Limoncello Haze':'S', 'Limoncello Haze':'H/I', 'Apple Zauce':'H', 'Bananappeal':'H', 'Butter Breath':'H/I',
            'CuratedFX - Sleep':'H/I', 'Funk Trunk':'H/I', 'Punchberry':'H/I', 'Purple Paradox':'H/I', 'Wicked Jam':'H/I', 'Dog Patch':'S',
            'Donny Burger':'I', 'Big Bagg #11':'H', '501st OG':'H/I', 'Sour Diesel x Chem D':'H/S', 'White Wedding + Donny Burger':'I',
            'Motorbreath #15 x Super Lemon Haze':'H', 'Ghost Train Haze x Super Lemon Haze':'S', 'Banana Jealousy x Super Lemon Haze':'H/S',
            'Glue + Kief':'H', 'White Wedding + Glue + Kief':'H/I', 'White Wedding + GMO Zkittlez + Kief':'I', 'Sticky Wedding':'I', 'Short Cut':'H',
            'Sweet 16':'H/I', 'Donny Burger + Dubble Tropicanna':'H/I', 'White Wedding + Motorbreath #15':'I', 'Mimosa EVO':'H/I',
            'CuratedFX - Calm':'H', 'Grapevine':'H/I', 'Blood Orange Blossom':'H', 'Tangerine Fizz':'H', 'Blueberry Muffin':'I',
            'Han Solo Burger':'H/I', 'Knockout':'H/S', 'Baller\'s Game':'I', 'Oh My Thai':'H/S', 'Everglades OG':'H', 'Easy Button':'H',
            'Pineapple Daddy':'H', 'Pineapple Diesel':'H', 'Key Lime Divine': 'H/S', 'Master Key': 'H', 'Concord Grape': 'I', 'Honey Melon': 'H', 'Lemonade': 'S',
            'Strawberry Punch': 'S', 'Sweet Watermelon': 'H', 'Wild Blueberry': 'I', 'Banana Lemon Cupcake': 'H/S', 'Super Lemon Haze 2.0':'S',
            'Galactic Warheads': 'H/I', 'Donny Burger x Banana Jealousy': 'H/I', 'Lime Wreck Haze': 'S', 'Crosstown Traffic': 'H/I', 'DX4': 'H',
            'Oreoz': 'H/I', 'Glueberry Pie': 'I', 'Tropical Blossom': 'H/S', 'Guava Sherb': 'H/I', 'Icy Mint': 'S', 'GMO Z': 'I'}

harvest_list = ['Flower Jar 3.5g (+)','Head Stash 3.5g','Premium Flower Jar 1g','Pre-Roll 1g', 'Pre-Roll Blunt 1g','Pre-Roll 7-Pack 3.5g']

# ordered_ids = ['HEAD-STASH-3.5', 'FLWR-3.5-PLUS', 'FLWR-3.5', 'PR1', 'PR1-KIEF', 'PR1-BLNT', 'PR5-5-BLNT', 'PRT-7',
#                'PR5-5', 'PR5-2.5', 'MZ-7G-CGRP', 'MZ-7G-HMLN', 'MZ-7G-LMND', 'MZ-7G-STRP', 'MZ-7G-SWTM', 'MZ-7G-WLDB', 'PR2-.5-3PMZ',
#                'PR-MNR', 'FP-MNR', 'FP-MNR-STR', 'PR-MNR-STR', 'PURET-500', 'PURET-TERP-500', 'RSLV-1:1-250',
#                'RSO-TINC-500', 'REMT-1:1-250', 'HVG-6-SEEDPACK-AUTO', 'HVG-6-SEEDPACK-PHOTO', 'HM-DSP-LVO-.5G', 'HM-DSP-LVO-1G', 'LVO-CART-.5', 'LVO-CART-1',
#                'LHR-CART-.5', 'SS-50', 'CFX-SS-50', 'GUM100-CFX-CALM', 'GUM100-CFX-ENERGY', 'GUM100-CFX-FOCUS',
#                'GUM100-CFX-SLEEP', 'GUM100-CFX-20:1', 'GUM100-CFX-RELIEF', 'GUM5-CFX-20:1-P', 'GUM100-RAPID', 'FD100', 'GUM-HR-50', 'GUM-HR-100',
#                'GUM100', 'CHOC100', 'GUM400', 'GUM1000', 'CHOC400', 'CHOC1000', 'LHR-COLDCURE', 'LHR-JAM', 'TRD-HASH']

ordered_ids = ['HEAD-STASH-3.5', 'FLWR-3.5-PLUS', 'FLWR-3.5', 'PR1', 'PR-1.2-TID-INFSD', 'PR1-BLNT', 'PR2-.5-3PMZ', 'PR2-.5-INFSD-3PMZ', 'PRT-7',  'MZ-7G-CGRP', 'MZ-7G-HMLN',
               'MZ-7G-LMND', 'MZ-7G-STRP', 'MZ-7G-SWTM', 'MZ-7G-WLDB', 'PR1-KIEF', 'PR5-5-BLNT', 'PR5-5', 'PR5-2.5', 'PR-MNR', 'FP-MNR', 'FP-MNR-STR', 'PR-MNR-STR', 'RSLV-1:1-250', 'PURET-500', 'PURET-TERP-500', 
               'RSO-TINC-500', 'REMT-1:1-250', 'HVG-6-SEEDPACK-AUTO', 'HVG-6-SEEDPACK-PHOTO', 'HM-DSP-LVO-.5G', 'HM-DSP-LVO-1G', 'LVO-CART-.5', 'LVO-CART-1',
               'LHR-CART-.5', 'SS-50', 'CFX-SS-50', 'GUM100-CFX-CALM', 'GUM100-CFX-ENERGY', 'GUM100-CFX-FOCUS',
               'GUM100-CFX-SLEEP', 'GUM100-CFX-20:1', 'GUM100-CFX-RELIEF', 'GUM5-CFX-20:1-P', 'GUM100-RAPID', 'FD100', 'GUM-HR-50', 'GUM-HR-100',
               'GUM100', 'CHOC100', 'GUM400', 'GUM1000', 'CHOC400', 'CHOC1000', 'LHR-COLDCURE', 'LHR-JAM', 'TRD-HASH']

# cat_by_inventory_id = {'PR1': 'PRE-ROLLS 1g', 'PR1-KIEF': 'PRE-ROLLS 1g - KIEF', 'PRT-7': 'PRE-ROLL 7-Pack 3.5g', 'LVO-CART-1': '1g 510', 'HM-DSP-LVO-.5G': 'The Hitmaker - .5g Disposable Vape',
#                     'HM-DSP-LVO-1G': 'The Hitmaker - 1g Disposable Vape', 'GUM100-CFX-ENERGY': 'CuratedFX Gummies - Rapid Onset - 100mg THC', 'REMT-1:1-250': 'TOTINCTURES',
#                     'GUM100-RAPID': 'RAPID ONSET Gummies - 100mg THC', 'GUM100': 'Original Gummies (Rec Dose) - 100mg THC', 'CHOC100': 'Chocolates (Rec Dose) - 100mg THC', 'SS-50': 'Stir Stix - Rapid Onset - 50mg THC',
#                     'CFX-SS-50': 'CuratedFX Stir Stix - Rapid Onset - 50mg THC', 'FD100': 'Fruit Drops - 100mg THC', 'GUM100-CFX-CALM': 'CuratedFX Gummies - Rapid Onset - 100mg THC',
#                     'FLWR-3.5-PLUS': 'FLOWER - Jar 3.5g (+)', 'FLWR-3.5': 'FLOWER - Jar 3.5g', 'PURET-500': 'TOPICAL/ TINCTURES', 'PR1-BLNT': 'PRE-ROLL Blunt 1g',
#                     'RSLV-1:1-250': 'TOPICAL/ TINCTURES', 'PR5-5-BLNT': 'Pre-Roll Blunt 5-Pack 5g', 'PR-MNR': 'Moonrockets', 'FP-MNR': 'Moonrockets',
#                     'FP-MNR-STR': 'Moonrockets', 'PR-MNR-STR': 'Moonrockets', 'LHR-CART-.5': 'Live Hash Rosin Cartridge .5g', 'LHR-COLDCURE': 'Live Hash Rosin - Cold Cure', 'LHR-JAM': 'Live Hash Rosin - Jam',
#                     'HEAD-STASH-3.5': 'HEAD STASH 3.5g', 'PR5-5': 'PRE-ROLL 1g 5 Pack 5g', 'PR5-2.5': 'PRE-ROLL .5g 5 Pack 2.5g', 'RSO-TINC-500': 'TOPICAL/ TINCTURES',
#                     'MZ-7G-LMND': 'muze - 7g', 'MZ-1G-CGRP': 'muze - 1g', 'MZ-1G-HMLN': 'muze - 1g', 'MZ-1G-LMND': 'muze - 1g', 'MZ-1G-STRP': 'muze - 1g',
#                     'MZ-1G-SWTM': 'muze - 1g', 'MZ-1G-WLDB': 'muze - 1g', 'MZ-7G-CGRP': 'muze - 7g', 'MZ-7G-HMLN': 'muze - 7g', 'MZ-7G-STRP': 'muze - 7g',
#                     'MZ-7G-SWTM': 'muze - 7g', 'MZ-7G-WLDB': 'muze - 7g', 'CHOC1000': 'Chocolates (Med Dose) - 400mg THC & 1000mg THC', 'GUM400': 'Original Gummies (Med Dose) - 400mg THC & 1000mg THC',
#                     'CHOC400': 'Chocolates (Med Dose) - 400mg THC & 1000mg THC', 'GUM100-CFX-FOCUS': 'CuratedFX Gummies - Rapid Onset - 100mg THC', 'GUM100-CFX-SLEEP': 'CuratedFX Gummies - Rapid Onset - 100mg THC',
#                     'PFWR-1': 'Premium Flower 1g', 'GUM1000': 'Original Gummies (Med Dose) - 400mg THC & 1000mg THC', 'LVO-CART-.5': '.5g 510', 'PURET-TERP-500': 'TOPICAL/ TINCTURES',
#                     'TRD-HASH': 'Traditional Style Hash', 'HVG-6-SEEDPACK-AUTO': 'Happy Valley Retail Seed Pack - 6 Seeds - Auto', 'HVG-6-SEEDPACK-PHOTO': 'Happy Valley Retail Seed Pack - 6 Seeds - Photo', 'GUM5-CFX-20:1-P': 'CuratedFX Gummies - Rapid Onset - 100mg THC',
#                     'GUM-HR-100': 'Hash Rosin Gummies - 100mg THC', 'GUM-HR-50': 'Hash Rosin Gummies', 'GUM100-CFX-20:1':'CuratedFX Gummies - Rapid Onset - 100mg THC',
#                     'GUM100-CFX-RELIEF': 'CuratedFX Gummies - Rapid Onset - 100mg THC',
#                     'PR2-.5-3PMZ': 'muze - 1g (2x .5g) pre-rolls', 'PR2-.5-INFSD-3PMZ': 'muze - 1g (2x .5g) infused pre-rolls'}

cat_by_inventory_id = {'PR1': 'PRE-ROLLS 1g', 'PR1-KIEF': 'PRE-ROLLS 1g - KIEF', 'PRT-7': 'PRE-ROLL 7-Pack 3.5g', 'LVO-CART-1': '1g 510', 'HM-DSP-LVO-.5G': 'The Hitmaker - .5g Disposable Vape',
                    'HM-DSP-LVO-1G': 'The Hitmaker - 1g Disposable Vape', 'GUM100-CFX-ENERGY': 'CuratedFX Gummies - Rapid Onset - 100mg THC', 'REMT-1:1-250': 'TINCTURES',
                    'GUM100-RAPID': 'RAPID ONSET Gummies - 100mg THC', 'GUM100': 'Original Gummies (Rec Dose) - 100mg THC', 'CHOC100': 'Chocolates (Rec Dose) - 100mg THC', 'SS-50': 'Stir Stix - Rapid Onset - 50mg THC',
                    'CFX-SS-50': 'Stir Stix - Rapid Onset - 50mg THC', 'FD100': 'Fruit Drops - 100mg THC', 'GUM100-CFX-CALM': 'CuratedFX Gummies - Rapid Onset - 100mg THC',
                    'FLWR-3.5-PLUS': 'FLOWER - Jar 3.5g (+)', 'FLWR-3.5': 'FLOWER - Jar 3.5g', 'PURET-500': 'TINCTURES', 'PR1-BLNT': 'PRE-ROLL Blunt 1g',
                    'RSLV-1:1-250': 'TOPICAL', 'PR5-5-BLNT': 'Pre-Roll Blunt 5-Pack 5g', 'PR-MNR': 'Moonrockets', 'FP-MNR': 'Moonrockets',
                    'FP-MNR-STR': 'Moonrockets', 'PR-MNR-STR': 'Moonrockets', 'LHR-CART-.5': 'Live Hash Rosin Cartridge .5g', 'LHR-COLDCURE': 'Live Hash Rosin - Cold Cure', 'LHR-JAM': 'Live Hash Rosin - Jam',
                    'HEAD-STASH-3.5': 'HEAD STASH 3.5g', 'PR5-5': 'PRE-ROLL 1g 5 Pack 5g', 'PR5-2.5': 'PRE-ROLL .5g 5 Pack 2.5g', 'RSO-TINC-500': 'TINCTURES',
                    'MZ-7G-LMND': 'muze - 7g', 'MZ-1G-CGRP': 'muze - 1g', 'MZ-1G-HMLN': 'muze - 1g', 'MZ-1G-LMND': 'muze - 1g', 'MZ-1G-STRP': 'muze - 1g',
                    'MZ-1G-SWTM': 'muze - 1g', 'MZ-1G-WLDB': 'muze - 1g', 'MZ-7G-CGRP': 'muze - 7g', 'MZ-7G-HMLN': 'muze - 7g', 'MZ-7G-STRP': 'muze - 7g',
                    'MZ-7G-SWTM': 'muze - 7g', 'MZ-7G-WLDB': 'muze - 7g', 'CHOC1000': 'Chocolates (Med Dose) - 400mg THC & 1000mg THC', 'GUM400': 'Original Gummies (Med Dose) - 400mg THC & 1000mg THC',
                    'CHOC400': 'Chocolates (Med Dose) - 400mg THC & 1000mg THC', 'GUM100-CFX-FOCUS': 'CuratedFX Gummies - Rapid Onset - 100mg THC', 'GUM100-CFX-SLEEP': 'CuratedFX Gummies - Rapid Onset - 100mg THC',
                    'PFWR-1': 'Premium Flower 1g', 'GUM1000': 'Original Gummies (Med Dose) - 400mg THC & 1000mg THC', 'LVO-CART-.5': '.5g 510', 'PURET-TERP-500': 'TINCTURES',
                    'TRD-HASH': 'Traditional Style Hash', 'HVG-6-SEEDPACK-AUTO': 'Happy Valley Retail Seed Pack - 6 Seeds - Auto', 'HVG-6-SEEDPACK-PHOTO': 'Happy Valley Retail Seed Pack - 6 Seeds - Photo', 'GUM5-CFX-20:1-P': 'CuratedFX Gummies - Rapid Onset - 100mg THC',
                    'GUM-HR-100': 'Hash Rosin Gummies - 100mg THC', 'GUM-HR-50': 'Hash Rosin Gummies', 'GUM100-CFX-20:1':'CuratedFX Gummies - Rapid Onset - 100mg THC',
                    'GUM100-CFX-RELIEF': 'CuratedFX Gummies - Rapid Onset - 100mg THC', 'PR2-.5-3PMZ': 'muze - 1g (2x .5g) pre-rolls', 'PR2-.5-INFSD-3PMZ': 'muze - 1g (2x .5g) infused pre-rolls', 'PR-1.2-TID-INFSD': 'INFUSED PRE-ROLLS 1.2g'}

price_ea = {'PR1': '$5.00', 'PR1-KIEF': '$5.00', 'PRT-7': '$20.00', 'LVO-CART-1': '$15.00', 'HM-DSP-LVO-.5G': '$10.00',
                    'HM-DSP-LVO-1G': '$17.50', 'GUM100-CFX-ENERGY': '$12.50', 'REMT-1:1-250': '$20.00',
                    'GUM100-RAPID': '$10.00', 'GUM100': '$7.00', 'CHOC100': '$10.00', 'SS-50': '$5.00',
                    'CFX-SS-50': '$6.00', 'FD100': '$7.00', 'GUM100-CFX-CALM': '$12.50',
                    'FLWR-3.5-PLUS': '$17.50', 'FLWR-3.5': '$17.50', 'PURET-500': '$17.50', 'PR1-BLNT': '$6.00',
                    'RSLV-1:1-250': '$25.00', 'PR5-5-BLNT': '??', 'PR-MNR': '$12.50', 'FP-MNR': '$22.50',
                    'FP-MNR-STR': '$22.50', 'PR-MNR-STR': '$12.50', 'LHR-CART-.5': '$17.50', 'LHR-COLDCURE': '$35.00', 'LHR-JAM': '??',
                    'HEAD-STASH-3.5': '$25.00', 'PR5-5': '$30.00', 'PR5-2.5': '$17.50', 'RSO-TINC-500': '$25.00',
                    'MZ-7G-LMND': '$15.00', 'MZ-1G-CGRP': '$0.01', 'MZ-1G-HMLN': '$0.01', 'MZ-1G-LMND': '$0.01', 'MZ-1G-STRP': '$0.01',
                    'MZ-1G-SWTM': '$0.01', 'MZ-1G-WLDB': '$0.01', 'MZ-7G-CGRP': '$15.00', 'MZ-7G-HMLN': '$15.00', 'MZ-7G-STRP': '$15.00',
                    'MZ-7G-SWTM': '$15.00', 'MZ-7G-WLDB': '$15.00', 'CHOC1000': '$45.00', 'GUM400': '$25.00',
                    'CHOC400': '$25.00', 'GUM100-CFX-FOCUS': '$12.50', 'GUM100-CFX-SLEEP': '$12.50',
                    'PFWR-1': '$8.00', 'GUM1000': '$45.00', 'LVO-CART-.5': '$10.00', 'PURET-TERP-500': '$20.00',
                    'TRD-HASH': '$30.00', 'HVG-6-SEEDPACK-AUTO': '$30.00', 'HVG-6-SEEDPACK-PHOTO': '$30.00', 'GUM5-CFX-20:1-P': '$12.50', 'GUM-HR-100': '$12.50', 'GUM100-CFX-20:1':'$12.50',
                    'GUM100-CFX-RELIEF': '$12.50', 'PR2-.5-3PMZ': '$3.50', 'PR2-.5-INFSD-3PMZ': '$7.50', 'PR-1.2-TID-INFSD': '$10.00'}

net_weight_vol = {'PR1': '1g', 'PR1-KIEF': '1g', 'PRT-7': '3.5g', 'LVO-CART-1': '1g', 'HM-DSP-LVO-.5G': '.5g',
                    'HM-DSP-LVO-1G': '1g', 'GUM100-CFX-ENERGY': ' ', 'REMT-1:1-250': '30ml',
                    'GUM100-RAPID': ' ', 'GUM100': ' ', 'CHOC100': ' ', 'SS-50': ' ',
                    'CFX-SS-50': ' ', 'FD100': ' ', 'GUM100-CFX-CALM': ' ',
                    'FLWR-3.5-PLUS': '3.5g', 'FLWR-3.5': '3.5g', 'PURET-500': '30ml', 'PR1-BLNT': '1g',
                    'RSLV-1:1-250': '30ml', 'PR5-5-BLNT': '5g', 'PR-MNR': '1g', 'FP-MNR': '2g',
                    'FP-MNR-STR': '2g', 'PR-MNR-STR': '1g', 'LHR-CART-.5': '.5g', 'LHR-COLDCURE': '1g', 'LHR-JAM': '1g',
                    'HEAD-STASH-3.5': '3.5g', 'PR5-5': '5g', 'PR5-2.5': '2.5g', 'RSO-TINC-500': '30ml',
                    'MZ-7G-LMND': '7g', 'MZ-1G-CGRP': '1g', 'MZ-1G-HMLN': '1g', 'MZ-1G-LMND': '1g', 'MZ-1G-STRP': '1g',
                    'MZ-1G-SWTM': '1g', 'MZ-1G-WLDB': '1g', 'MZ-7G-CGRP': '7g', 'MZ-7G-HMLN': '7g', 'MZ-7G-STRP': '7g',
                    'MZ-7G-SWTM': '7g', 'MZ-7G-WLDB': '7g', 'CHOC1000': ' ', 'GUM400': ' ',
                    'CHOC400': ' ', 'GUM100-CFX-FOCUS': ' ', 'GUM100-CFX-SLEEP': ' ',
                    'PFWR-1': '1g', 'GUM1000': ' ', 'LVO-CART-.5': '.5g', 'PURET-TERP-500': '30ml',
                    'TRD-HASH': '1g', 'HVG-6-SEEDPACK-AUTO': ' ',  'HVG-6-SEEDPACK-PHOTO': ' ', 'GUM5-CFX-20:1-P': ' ', 'GUM-HR-100': ' ',
                    'GUM100-CFX-20:1':' ', 'GUM100-CFX-RELIEF': ' ', 'PR2-.5-3PMZ': '1g', 'PR2-.5-INFSD-3PMZ': '1g','PR-1.2-TID-INFSD': '1.2g'}

case_count = {'PR1': 100, 'PR1-KIEF': 100, 'PRT-7': 50, 'LVO-CART-1': 50, 'HM-DSP-LVO-.5G': 50,
                    'HM-DSP-LVO-1G': 50, 'GUM100-CFX-ENERGY': 50, 'REMT-1:1-250': 50,
                    'GUM100-RAPID': 50, 'GUM100': 50, 'CHOC100': 50, 'SS-50': 50,
                    'CFX-SS-50': 50, 'FD100': 50, 'GUM100-CFX-CALM': 50,
                    'FLWR-3.5-PLUS': 50, 'FLWR-3.5': 50, 'PURET-500': 50, 'PR1-BLNT': 100,
                    'RSLV-1:1-250': 50, 'PR5-5-BLNT': 50, 'PR-MNR': 50, 'FP-MNR': 50,
                    'FP-MNR-STR': 50, 'PR-MNR-STR': 50, 'LHR-CART-.5': 50, 'LHR-COLDCURE': 50, 'LHR-JAM': '??',
                    'HEAD-STASH-3.5': 50, 'PR5-5': 50, 'PR5-2.5': 50, 'RSO-TINC-500': 50,
                    'MZ-7G-LMND': 50, 'MZ-1G-CGRP': 25, 'MZ-1G-HMLN': 25, 'MZ-1G-LMND': 25, 'MZ-1G-STRP': 25,
                    'MZ-1G-SWTM': 25, 'MZ-1G-WLDB': 25, 'MZ-7G-CGRP': 50, 'MZ-7G-HMLN': 50, 'MZ-7G-STRP': 50,
                    'MZ-7G-SWTM': 50, 'MZ-7G-WLDB': 50, 'CHOC1000': 50, 'GUM400': 50,
                    'CHOC400': 50, 'GUM100-CFX-FOCUS': 50, 'GUM100-CFX-SLEEP': 50,
                    'PFWR-1': 50, 'GUM1000': 50, 'LVO-CART-.5': 50, 'PURET-TERP-500': 50,
                    'TRD-HASH': 50, 'HVG-6-SEEDPACK-AUTO': 10, 'HVG-6-SEEDPACK-PHOTO': 10, 'GUM5-CFX-20:1-P': 50, 'GUM-HR-100': 50,
                    'GUM100-CFX-20:1': 50, 'GUM100-CFX-RELIEF': 50, 'PR2-.5-3PMZ': 100, 'PR2-.5-INFSD-3PMZ': 100, 'PR-1.2-TID-INFSD': 100}

servings = {'PR1': ' ', 'PR1-KIEF': ' ', 'PRT-7': ' ', 'LVO-CART-1': ' ', 'HM-DSP-LVO-.5G': ' ',
                    'HM-DSP-LVO-1G': ' ', 'GUM100-CFX-ENERGY': 20, 'REMT-1:1-250': ' ',
                    'GUM100-RAPID': 20, 'GUM100': 20, 'CHOC100': 20, 'SS-50': 10,
                    'CFX-SS-50': 10, 'FD100': 20, 'GUM100-CFX-CALM': 20,
                    'FLWR-3.5-PLUS': ' ', 'FLWR-3.5': ' ', 'PURET-500': ' ', 'PR1-BLNT': ' ',
                    'RSLV-1:1-250': ' ', 'PR5-5-BLNT': ' ', 'PR-MNR': ' ', 'FP-MNR': ' ',
                    'FP-MNR-STR': ' ', 'PR-MNR-STR': ' ', 'LHR-CART-.5': ' ', 'LHR-COLDCURE': ' ', 'LHR-JAM': ' ',
                    'HEAD-STASH-3.5': ' ', 'PR5-5': ' ', 'PR5-2.5': ' ', 'RSO-TINC-500': ' ',
                    'MZ-7G-LMND': ' ', 'MZ-1G-CGRP': ' ', 'MZ-1G-HMLN': ' ', 'MZ-1G-LMND': ' ', 'MZ-1G-STRP': ' ',
                    'MZ-1G-SWTM': ' ', 'MZ-1G-WLDB': ' ', 'MZ-7G-CGRP': ' ', 'MZ-7G-HMLN': ' ', 'MZ-7G-STRP': ' ',
                    'MZ-7G-SWTM': ' ', 'MZ-7G-WLDB': ' ', 'CHOC1000': 20, 'GUM400': 20,
                    'CHOC400': 20, 'GUM100-CFX-FOCUS': 20, 'GUM100-CFX-SLEEP': 20,
                    'PFWR-1': ' ', 'GUM1000': 20, 'LVO-CART-.5': ' ', 'PURET-TERP-500': ' ',
                    'TRD-HASH': ' ', 'HVG-6-SEEDPACK-AUTO': 6, 'HVG-6-SEEDPACK-PHOTO': 6, 'GUM5-CFX-20:1-P': 20, 'GUM-HR-100': 10,
                    'GUM100-CFX-20:1': 20, 'GUM100-CFX-RELIEF': 20, 'PR2-.5-3PMZ': ' ', 'PR2-.5-INFSD-3PMZ': ' ', 'PR-1.2-TID-INFSD': ' '}

# cfx_gum_map = {'Berries & Cream': 'Calm - Berries & Cream', 'Lemon Lime': 'Energy - Lemon Lime',
#                'Tropical Punch': 'Focus - Tropical Punch', 'Grape': 'Sleep - Grape', 'Blueberry': 'Sleep - Blueberry', 'Watermelon': 'Watermelon'}

cfx_gum_map = {('GUM100-CFX-CALM', 'Berries & Cream'): 'Calm - Berries & Cream', ('GUM100-CFX-ENERGY', 'Lemon Lime'): 'Energy - Lemon Lime', 
               ('GUM100-CFX-FOCUS', 'Tropical Punch'): 'Focus - Tropical Punch', ('GUM100-CFX-SLEEP', 'Grape'): 'Sleep - Grape',
               ('GUM100-CFX-SLEEP','Blueberry'): 'Sleep - Blueberry', ('GUM100-CFX-20:1','Watermelon'): 'Watermelon', ('GUM100-CFX-RELIEF','Watermelon'): 'Relief - Watermelon'}

cfx_gum_cbds_map = {'Calm - Berries & Cream': 'THC - CBD - CBN', 'Energy - Lemon Lime': 'THC-V - CBD - THC - Caffeine',
               'Focus - Tropical Punch': 'THC - CBD - CBG', 'Sleep - Grape': 'CBN - THC - Suntheanine', 'Sleep - Blueberry': 'CBN - THC - Suntheanine',
               'Watermelon': '20:1 CBD:THC', 'Relief - Watermelon': '20:1:1 CBD:THC:CBC'}

top_tinc_thc_cbd_map = {'Pure Tincture - THC - 500MG': '500mg THC', 'Pure Terpene-Infused Tincture - THC - 500MG': '500mg THC', 'Relief Salve - 250mg CBD:250mg THC': '250mg CBD:250mg THC',
                        'RSO Tincture - THC - 500MG': '500mg THC', 'Remedy Tincture - 1:1 with Cannabis Terpenes - 250MG CBD 250MG THC': '250mg CBD:250mg THC'}

prod_desc_with_no_batch_val = ['Pure Tincture - THC - 500MG', 'Pure Terpene-Infused Tincture - THC - 500MG', 'Relief Salve - 250mg CBD:250mg THC',
                               'RSO Tincture - THC - 500MG', 'Remedy Tincture - 1:1 with Cannabis Terpenes - 250MG CBD 250MG THC', 'Stir Stix - 50mg THC',
                               'CuratedFX Stir Stix - 50mg THC', 'Gummies Curated FX - CALM - 100mg THC', 'Gummies Curated FX - ENERGY - 100mg THC',
                               'Gummies Curated FX - FOCUS - 100mg THC', 'Gummies Curated FX - SLEEP - 100mg THC', 'Gummies Curated FX - 20:1 CBD:THC - 100mg THC',
                               'Gummies - Rapid Onset - 100mg THC', 'Fruit Drops - 100mg THC', 'Gummies - Hash Rosin - 100mg THC', 'Gummies 100mg THC',
                               'Chocolate 100mg THC', 'Gummies 1000mg THC', 'Gummies 400mg THC', 'Chocolate 400mg THC', 'Chocolate 1000mg THC', 'Pre-Roll "Variety" 5-Pack 2.5g', 'Pre-Roll 5-Pack 5g',
                               'Gummies Curated FX - RELIEF - 100mg THC', 'Happy Valley Retail Seed Pack - 6 Seeds - Auto', 'Happy Valley Retail Seed Pack - 6 Seeds - Photo']

# FORMAT EXAMPLE - DO NOT DELETE THIS
# value_pricing = {('FLWR-3.5-PLUS', 'Lime Wreck Haze'): '$5.00',
#                  ('FLWR-3.5-PLUS', 'Melon Baller'): '$1.00',
#                  ('HM-DSP-LVO-1G', 'Purple Paradox'): '$14.00',
#                 ('CHOC100', 'Milk'): '$600.00'}

# the dictionary is as follows:
# (Product Description, Strain/Flavor: Value Price)
value_pricing = {('Hitmaker Disposable Vape 1g', 'CuratedFX - Sleep'): '$15.00',
                 ('Hitmaker Disposable Vape 1g', 'CuratedFX - Calm'): '$15.00',
                 ('Hitmaker Disposable Vape .5g', 'CuratedFX - Calm'): '$8.00',
                ('Hitmaker Disposable Vape .5g', 'CuratedFX - Sleep'): '$8.00',
                ('Live Vape Oil Cartridge .5g', 'CuratedFX - Sleep'): '$8.00',
                ('Live Vape Oil Cartridge .5g', 'CuratedFX - Calm'): '$8.00',
                ('Live Vape Oil Cartridge 1g', 'CuratedFX - Sleep'): '$12.50',
                ('Live Vape Oil Cartridge 1g', 'CuratedFX - Calm'): '$12.50'}

# when NO value pricing - uncomment this out and comment out the dictionary above
# value_pricing = {}

volume_pricing_ad = {'FLWR-3.5-PLUS': 'Purchase 10+ cases get all for $15/ unit *Excludes Head Stash*',
                  'PRT-7': '10+ cases get $17.50 per unit',
                  'HM-DSP-LVO-1G': '10+ Cases of Vape gets $1 off per unit',
                  'HM-DSP-LVO-.5G': '10+ Cases of Vape gets $1 off per unit',
                  'LVO-CART-1': '10+ Cases of Vape gets $1 off per unit',
                  'LVO-CART-.5': '10+ Cases of Vape gets $1 off per unit',
                  'GUM100-RAPID': '10+ Cases of Gummies gets $2 off per unit',
                  'GUM100': '10+ Cases of Gummies gets $2 off per unit',
                  'GUM-HR-100': '10+ Cases of Gummies gets $2 off per unit',
                  'FD100': '10+ Cases of Fruit Drops gets $2 off per unit'}

volume_pricing = {'Flower Jar 3.5g (+)': '15.00',
                  'Pre-Roll 7-Pack 3.5g': '17.50',
                  'Hitmaker Disposable Vape 1g': '16.50',
                  'Hitmaker Disposable Vape .5g': '9.00',
                  'Live Vape Oil Cartridge 1g': '14.00',
                  'Live Vape Oil Cartridge .5g': '9.00',
                  'Gummies - Rapid Onset - 100mg THC': '8.00',
                  'Gummies 100mg THC': '5.00',
                  'Gummies - Hash Rosin - 100mg THC': '10.50',
                  'Fruit Drops - 100mg THC': '5.00'}

# this dictionary maps the strain to the cultivar "id" that's used to link strains
# to the respective cultivar page on hv's website
strain_to_cult_page = {'Candy Store #25':'candy-store-25', 'Sugar Shack #5':'sugar-shack-5',
                    'Super Lemon Haze':'super-lemon-haze', 'Zweet OG':'zweet-og', 'End Game Cookies':'end-game-cookies',
                    'Splash':'splash', 'Banana Jealousy':'banana-jealousy', 'Candy Store #38':'candy-store-38', 'T. SAGE':'t-sage',
                    'Dubble Tropicanna':'dubble-tropicanna', 'Sunset Sherbet':'sunset-sherbet', 'White Truffle':'white-truffle',
                    'GMO Zkittlez':'gmo-zkittlez', 'Melon Baller':'melon-baller', 'Motorbreath #15':'motorbreath-15', 
                    'White Wedding':'white-wedding', 'Donny Burger':'donny-burger', 'Galactic Warheads':'galactic-warheads'
                      }

strain_to_gen_page = {'Candy Games #25':'candy-games-25', 'Candy Games #38':'candy-games-38', 'Knockout':'knockout', 'Baller\'s Game':'ballers-game',
                      'Oh My Thai':'oh-my-thai', 'Everglades OG':'everglades-og', 'Easy Button':'easy-button',
                      'Pineapple Daddy':'pineapple-daddy','Another Level':'another-level', 'Pineapple Diesel':'pineapple-diesel',
                      'Short Cut': 'shortcut', 'Game Over': 'game-over', 'Overtime': 'overtime', 'Sweet 16': 'sweet-16'
                      }