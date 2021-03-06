from __future__ import absolute_import
from django.contrib import admin
from .models import Campaign, Contact, Configuration


class ConfigurationAdmin(admin.ModelAdmin):
    readonly_fields=(u'created', u'updated', )

class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        u'name',
        u'active',
        u'salesforce_id',
    )
    readonly_fields=(u'created', u'updated', )

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        u'user',
        u'real_course_created_at',
        u'campaign',
        u'contact_id',
        u'salesforce_push_pending',
        u'completed_training_wheels_date',
        u'started_assignment_date',
        u'completed_assignment_date',
        u'soft_ask_decision',
        u'soft_ask_decision_date',
        u'estimated_enrollment',
        u'latest_adoption_decision',
        u'completed_super_training_wheel_1',
        u'downloaded_gsg',
        u'watched_video',
        u'completed_am_page_tips',
        u'created_a_course',
        u'completed_building_assignments_training',
        u'completed_how_to_set_up_grading_page_tip'
    )
    readonly_fields=(u'created', u'updated', )



admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Contact, ContactAdmin)
