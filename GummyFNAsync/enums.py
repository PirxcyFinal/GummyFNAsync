from enum import Enum


class BackendRarity(Enum):
    Transcendent = 'EFortRarity::Transcendent'
    Legendary = 'EFortRarity::Legendary'
    Epic = 'EFortRarity::Epic'
    Rare = 'EFortRarity::Rare'
    Uncommon = 'EFortRarity::Uncommon'
    Common = 'EFortRarity::Uncommon'


class BackendType(Enum):
    Backpack = 'AthenaBackpack'
    Wrap = 'AthenaItemWrap'
    Glider = 'AthenaGlider'
    Pickaxe = 'AthenaPickaxe'
    Outfit = 'AthenaCharacter'
