# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-12-18 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('willolabs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ltiexternalcourseenrollmentgrades',
            name='lti_user_id',
            field=models.CharField(help_text=b'Example: ab3e190fae668d925d007d79219fbfce90afba6d', max_length=255, null=True, verbose_name=b'User ID'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='context_label',
            field=models.CharField(help_text=b'Example: Rover', max_length=50, null=True, verbose_name=b'Context Label'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='custom_canvas_api_domain',
            field=models.CharField(help_text=b'Example: willowlabs.instructure.com', max_length=255, null=True, verbose_name=b'Custom Canvas API Domain'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='custom_canvas_course_id',
            field=models.CharField(help_text=b'Example: 421', max_length=50, null=True, verbose_name=b'Custom Canvas Course ID'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='custom_canvas_course_startat',
            field=models.DateTimeField(help_text=b'Example: 2019-12-11 16:18:01 -0500', null=True, verbose_name=b'Custom Canvas Course Start At'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='ext_wl_launch_key',
            field=models.CharField(help_text=b'Example: QcTz6q', max_length=50, null=True, verbose_name=b'External WilloLab Launch Key'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='ext_wl_launch_url',
            field=models.URLField(help_text=b'Example: https://stage.willolabs.com/launch/QcTz6q/8cmzcd', null=True, verbose_name=b'External WilloLab Launch URL'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='ext_wl_outcome_service_url',
            field=models.URLField(help_text=b'Example: https://stage.willolabs.com/api/v1/outcomes/QcTz6q/e14751571da04dd3a2c71a311dda2e1b/', null=True, verbose_name=b'External  Outcome Service URL'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='ext_wl_version',
            field=models.CharField(help_text=b'Example: 1.0', max_length=25, null=True, verbose_name=b'External WilloLab Version'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='tool_consumer_info_product_family_code',
            field=models.CharField(help_text=b'Example: canvas', max_length=50, null=True, verbose_name=b'Tool Consumer - Product Family Code'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='tool_consumer_info_version',
            field=models.CharField(help_text=b'Example: cloud', max_length=50, null=True, verbose_name=b'Tool Consumer - Version'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='tool_consumer_instance_contact_email',
            field=models.EmailField(help_text=b'Example: notifications@instructure.com', max_length=254, null=True, verbose_name=b'Tool Consumer - Contact Email Address'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='tool_consumer_instance_guid',
            field=models.CharField(help_text=b'Example: 7M58pE4F4Y56gZHUe6jaxhQ1csaktjA00ZiVNQb7:canvas-lms', max_length=100, null=True, verbose_name=b'Tool Consumer - Instance GUID'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourse',
            name='tool_consumer_instance_name',
            field=models.CharField(help_text=b'Example: Willo Labs', max_length=50, null=True, verbose_name=b'Tool Consumer - Instance Name'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourseenrollment',
            name='lis_person_contact_email_primary',
            field=models.EmailField(help_text=b'Example: rover_student@willolabs.com', max_length=254, null=True, verbose_name=b'User - Primary Email Address'),
        ),
        migrations.AlterField(
            model_name='ltiexternalcourseenrollmentgrades',
            name='course_version',
            field=models.CharField(blank=True, help_text=b'Guid of latest course version', max_length=255, null=True),
        ),
    ]