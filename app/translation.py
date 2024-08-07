from modeltranslation.translator import register, TranslationOptions

from app.models import  Category, CategoryInnerDescription, Plant, PlantInnerDescription


# @register(Blog)
# class BlogTranslationOptions(TranslationOptions):
#     fields = ('title', 'description')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(CategoryInnerDescription)
class CategoryInnerDescriptionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Plant)
class PlantTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(PlantInnerDescription)
class PlantInnerDescriptionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')