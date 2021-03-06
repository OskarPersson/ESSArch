from django.contrib import admin

from ESSArch_Core.tags.models import (
    DeliveryType,
    LocationFunctionType,
    LocationLevelType,
    MetricType,
    NodeIdentifierType,
    NodeNoteType,
    NodeRelationType,
    StructureRelationType,
    StructureType,
    StructureUnitType,
    TagVersionType,
)


class NodeNoteTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'history')


class NodeRelationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'mirrored_type')


class StructureRelationTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'mirrored_type')


class StructureUnitTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'structure_type')


class TagVersionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'archive_type', 'information_package_type')


admin.site.register(DeliveryType)
admin.site.register(LocationFunctionType)
admin.site.register(LocationLevelType)
admin.site.register(MetricType)
admin.site.register(NodeRelationType, NodeRelationTypeAdmin)
admin.site.register(NodeIdentifierType)
admin.site.register(NodeNoteType, NodeNoteTypeAdmin)
admin.site.register(StructureType)
admin.site.register(StructureRelationType, StructureRelationTypeAdmin)
admin.site.register(StructureUnitType, StructureUnitTypeAdmin)
admin.site.register(TagVersionType, TagVersionTypeAdmin)
