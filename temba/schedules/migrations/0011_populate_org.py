# Generated by Django 2.2.4 on 2019-08-23 18:26

from django.db import migrations


def noop(apps, schema_editor):  # pragma: no cover
    pass


def populate_org(apps, schema_editor):  # pragma: no cover
    Schedule = apps.get_model("schedules", "Schedule")
    Trigger = apps.get_model("triggers", "Trigger")
    Broadcast = apps.get_model("msgs", "Broadcast")

    updated = 0

    for t in Trigger.objects.all().exclude(schedule=None):
        Schedule.objects.filter(id=t.schedule_id).update(org_id=t.org_id)
        updated += 1

    for b in Broadcast.objects.all().exclude(schedule=None):
        Schedule.objects.filter(id=b.schedule_id).update(org_id=b.org_id)
        updated += 1

    if updated > 0:
        print(f"populated {updated} schedules with org")


class Migration(migrations.Migration):

    dependencies = [
        ("triggers", "0016_auto_20190816_1517"),
        ("msgs", "0134_remove_broadcast_purged"),
        ("schedules", "0010_populate_days_of_week"),
    ]

    operations = [migrations.RunPython(populate_org, noop)]