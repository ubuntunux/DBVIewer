from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class DeployNpc(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    zone_primarykey = models.TextField(db_column='Zone_PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deploy_count = models.TextField(db_column='Deploy_Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Deploy_Npc'


class DeployProp(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    zone_primarykey = models.TextField(db_column='Zone_PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deploy_count = models.TextField(db_column='Deploy_Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Deploy_Prop'


class EftableNpc(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondarykey = models.TextField(db_column='SecondaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    titlename = models.TextField(db_column='TitleName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    titlenamecomment = models.TextField(db_column='TitleNameComment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment1 = models.TextField(db_column='Comment1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nametag = models.TextField(db_column='NameTag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    balloonnamehide = models.TextField(db_column='BalloonNameHide', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    icon = models.TextField(db_column='Icon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    level = models.TextField(db_column='Level', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modelsize = models.TextField(db_column='ModelSize', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    grade = models.TextField(db_column='Grade', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type1 = models.TextField(db_column='Type1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bekilledshare = models.TextField(db_column='BeKilledShare', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    size = models.TextField(db_column='Size', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weight = models.TextField(db_column='Weight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    parts = models.TextField(db_column='Parts', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dietype = models.TextField(db_column='DieType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dieani = models.TextField(db_column='DieAni', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    diephysics = models.TextField(db_column='DiePhysics', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    diegibs = models.TextField(db_column='DieGibs', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invoketrigger = models.TextField(db_column='InvokeTrigger', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exp = models.TextField(db_column='Exp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    moneypercent = models.TextField(db_column='MoneyPercent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    moneyvalue = models.TextField(db_column='MoneyValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dropindex1 = models.TextField(db_column='DropIndex1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dropindex2 = models.TextField(db_column='DropIndex2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dropindex3 = models.TextField(db_column='DropIndex3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionrange = models.TextField(db_column='InteractionRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pathfindingtype = models.TextField(db_column='PathfindingType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    movecollison = models.TextField(db_column='MoveCollison', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    blockpcrootmotionskillpenetrate = models.TextField(db_column='BlockPCRootMotionSkillPenetrate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    immuneindex = models.TextField(db_column='ImmuneIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ticketdistance = models.TextField(db_column='Ticketdistance', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    detourrange = models.TextField(db_column='Detourrange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    showdamagehighlight = models.TextField(db_column='ShowDamageHighlight', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behittwistyawmin = models.TextField(db_column='BehitTwistYawMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behittwistyawmax = models.TextField(db_column='BehitTwistYawMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behittwistpitchmin = models.TextField(db_column='BehitTwistPitchMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behittwistpitchmax = models.TextField(db_column='BehitTwistPitchMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behittwistrollmin = models.TextField(db_column='BehitTwistRollMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behittwistrollmax = models.TextField(db_column='BehitTwistRollMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    minimumdistance = models.TextField(db_column='MinimumDistance', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stattype = models.TextField(db_column='StatType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attackpower = models.TextField(db_column='AttackPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hp = models.TextField(db_column='Hp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hp_count = models.TextField(db_column='Hp_Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mp = models.TextField(db_column='Mp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    combathprecovery = models.TextField(db_column='CombatHpRecovery', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    targetui = models.TextField(db_column='TargetUI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    targetui_design = models.TextField(db_column='TargetUI_Design', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifevessel = models.TextField(db_column='LifeVessel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    walkspeed = models.TextField(db_column='WalkSpeed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    movespeed = models.TextField(db_column='MoveSpeed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attribute = models.TextField(db_column='Attribute', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coefficient = models.TextField(db_column='Coefficient', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hitratio = models.TextField(db_column='Hitratio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    crtratio = models.TextField(db_column='Crtratio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dodge = models.TextField(db_column='Dodge', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    def_field = models.TextField(db_column='Def', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word. This field type is a guess.
    res = models.TextField(db_column='Res', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    crtblock = models.TextField(db_column='Crtblock', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aiindex = models.TextField(db_column='AiIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aggrotype = models.TextField(db_column='AggroType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aggrotickmin = models.TextField(db_column='AggroTickMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aggrotickmax = models.TextField(db_column='AggroTickMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attacktype = models.TextField(db_column='AttackType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    moverange = models.TextField(db_column='MoveRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    warrange = models.TextField(db_column='WarRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pursuitrange = models.TextField(db_column='PursuitRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sptime = models.TextField(db_column='SpTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spinvincibleduration = models.TextField(db_column='SpInvincibleDuration', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dieskillindex = models.TextField(db_column='DieSkillIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dieskillpercent = models.TextField(db_column='DieSkillPercent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    borderline = models.TextField(db_column='BorderLine', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destroyskillindex = models.TextField(db_column='DestroySkillIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destroyskillpercent = models.TextField(db_column='DestroySkillPercent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spbuffindex1 = models.TextField(db_column='SpBuffIndex1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spbuffindex2 = models.TextField(db_column='SpBuffIndex2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spbuffindex3 = models.TextField(db_column='SpBuffIndex3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sighttype = models.TextField(db_column='SightType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sightangle1 = models.TextField(db_column='SightAngle1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sightrange1 = models.TextField(db_column='SightRange1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sightangle2 = models.TextField(db_column='SightAngle2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sightrange2 = models.TextField(db_column='SightRange2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    watchangle = models.TextField(db_column='WatchAngle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tribe = models.TextField(db_column='Tribe', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    helptype = models.TextField(db_column='HelpType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    helprange = models.TextField(db_column='HelpRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    helpvalue = models.TextField(db_column='HelpValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    warlikevalue = models.TextField(db_column='WarlikeValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attackcooltimemin = models.TextField(db_column='AttackCooltimeMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attackcooltimemax = models.TextField(db_column='AttackCooltimeMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstskill1 = models.TextField(db_column='FirstSkill1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstskill2 = models.TextField(db_column='FirstSkill2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstskill1per = models.TextField(db_column='FirstSkill1Per', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    firstskill2per = models.TextField(db_column='FirstSkill2Per', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondskill1 = models.TextField(db_column='SecondSkill1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondskill2 = models.TextField(db_column='SecondSkill2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondskill3 = models.TextField(db_column='SecondSkill3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondskill4 = models.TextField(db_column='SecondSkill4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondskill1per = models.TextField(db_column='SecondSkill1Per', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondskill2per = models.TextField(db_column='SecondSkill2Per', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondskill3per = models.TextField(db_column='SecondSkill3Per', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondskill4per = models.TextField(db_column='SecondSkill4Per', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modpoint01 = models.TextField(db_column='ModPoint01', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modsignet01min = models.TextField(db_column='ModSignet01Min', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modsignet01max = models.TextField(db_column='ModSignet01Max', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behitdistrate = models.TextField(db_column='BehitDistRate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behitheightrate = models.TextField(db_column='BehitHeightRate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    behittimerate = models.TextField(db_column='BehitTimeRate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dieragdollvalueratestart = models.TextField(db_column='DieRagDollValueRateStart', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dieragdollvalueratechange = models.TextField(db_column='DieRagDollValueRateChange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dieragdollvalueratedest = models.TextField(db_column='DieRagDollValueRateDest', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    function = models.TextField(db_column='Function', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    functiontype = models.TextField(db_column='FunctionType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    functionname = models.TextField(db_column='FunctionName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    relation = models.TextField(db_column='Relation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    subfactionid = models.TextField(db_column='SubFactionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attack = models.TextField(db_column='Attack', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summonduration = models.TextField(db_column='SummonDuration', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unsummontype = models.TextField(db_column='UnsummonType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mapicon = models.TextField(db_column='MapIcon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mappriority = models.TextField(db_column='MapPriority', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionkeyicon = models.TextField(db_column='InteractionKeyIcon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionkeystring = models.TextField(db_column='InteractionKeyString', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    clickactionid = models.TextField(db_column='ClickActionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    clickactiontime = models.TextField(db_column='ClickActionTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactiondesc = models.TextField(db_column='CommonActionDesc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attacktargetdistance = models.TextField(db_column='AttackTargetDistance', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summontype = models.TextField(db_column='SummonType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summonspawnaction = models.TextField(db_column='SummonSpawnAction', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summonaitype = models.TextField(db_column='SummonAiType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summonlifetime = models.TextField(db_column='SummonLifetime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summongroup = models.TextField(db_column='SummonGroup', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summoncount = models.TextField(db_column='SummonCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exclusiongroup = models.TextField(db_column='ExclusionGroup', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exclusionrange = models.TextField(db_column='ExclusionRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summonamount = models.TextField(db_column='SummonAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summonfollowrange = models.TextField(db_column='SummonFollowRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summonapproachrange = models.TextField(db_column='SummonApproachRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attacksightrange1 = models.TextField(db_column='AttackSightRange1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summonreturnrange = models.TextField(db_column='SummonReturnRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    particlesoundpackage = models.TextField(db_column='ParticleSoundPackage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    synctarget = models.TextField(db_column='SyncTarget', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stiffenpointmax = models.TextField(db_column='StiffenPointMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stiffenpointdecrease = models.TextField(db_column='StiffenPointDecrease', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paralyzationpointmin = models.TextField(db_column='ParalyzationPointMin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paralyzationpointmax = models.TextField(db_column='ParalyzationPointMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paralyzationpointdecrease = models.TextField(db_column='ParalyzationPointDecrease', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paralyzationpercent = models.TextField(db_column='ParalyzationPercent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EFTable_Npc'


class EftableProp(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondarykey = models.TextField(db_column='SecondaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nametag = models.TextField(db_column='NameTag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchtype = models.TextField(db_column='TouchType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volumetype = models.TextField(db_column='VolumeType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickuptype = models.TextField(db_column='PickupType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contenttype = models.TextField(db_column='ContentType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zoneobject = models.TextField(db_column='ZoneObject', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actorclass = models.TextField(db_column='ActorClass', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    level = models.TextField(db_column='Level', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    scale = models.TextField(db_column='Scale', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    debris = models.TextField(db_column='Debris', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    blockprojectile = models.TextField(db_column='BlockProjectile', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hittype = models.TextField(db_column='HitType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hitamount = models.TextField(db_column='HitAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hitstep1 = models.TextField(db_column='HitStep1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hitstep2 = models.TextField(db_column='HitStep2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hitstep3 = models.TextField(db_column='HitStep3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchamount = models.TextField(db_column='TouchAmount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchregentime = models.TextField(db_column='TouchRegenTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    restoredelay = models.TextField(db_column='RestoreDelay', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchontime = models.TextField(db_column='TouchOnTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchofftime = models.TextField(db_column='TouchOffTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchrotationdestdegree = models.TextField(db_column='TouchRotationDestDegree', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchrotationangularspeed = models.TextField(db_column='TouchRotationAngularSpeed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchrotationautorevert = models.TextField(db_column='TouchRotationAutoRevert', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jointhp = models.TextField(db_column='JointHP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    jointdamage = models.TextField(db_column='JointDamage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionrange = models.TextField(db_column='InteractionRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupduration = models.TextField(db_column='PickupDuration', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupdroplifetime = models.TextField(db_column='PickupDropLifetime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupuseconditionid = models.TextField(db_column='PickupUseConditionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupuseactionid = models.TextField(db_column='PickupUseActionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupusetargettype = models.TextField(db_column='PickupUseTargetType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupusetargetid = models.TextField(db_column='PickupUseTargetId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupusetargetrange = models.TextField(db_column='PickupUseTargetRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupmovemotion = models.TextField(db_column='PickupMoveMotion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupmovespeed = models.TextField(db_column='PickupMoveSpeed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupdropcommonactionindex = models.TextField(db_column='PickupDropCommonActionIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupthrowcommonactionindex = models.TextField(db_column='PickupThrowCommonActionIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupthrowprojectileid = models.TextField(db_column='PickupThrowProjectileId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickupthrowprojectilebound = models.TextField(db_column='PickupThrowProjectileBound', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pickuphitcount = models.TextField(db_column='PickupHitCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactionindex = models.TextField(db_column='CommonActionIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactiontime = models.TextField(db_column='CommonActionTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactiondesc = models.TextField(db_column='CommonActionDesc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    blocking = models.TextField(db_column='Blocking', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    clickicon = models.TextField(db_column='ClickIcon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    conditionid = models.TextField(db_column='ConditionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    executeactionid = models.TextField(db_column='ExecuteActionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    executeactioncount = models.TextField(db_column='ExecuteActionCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stateonactionid = models.TextField(db_column='StateOnActionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    stateoffactionid = models.TextField(db_column='StateOffActionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    usageactionid = models.TextField(db_column='UsageActionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spawnactionid = models.TextField(db_column='SpawnActionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    assembleontrasit = models.TextField(db_column='AssembleOnTrasit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    assemblegooffstring = models.TextField(db_column='AssembleGoOffString', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    assembleoffstring = models.TextField(db_column='AssembleOffString', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    questid = models.TextField(db_column='QuestId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    defaultaction = models.TextField(db_column='DefaultAction', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid0 = models.TextField(db_column='SkillId0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillcount0 = models.TextField(db_column='SkillCount0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid1 = models.TextField(db_column='SkillId1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillcount1 = models.TextField(db_column='SkillCount1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid2 = models.TextField(db_column='SkillId2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillcount2 = models.TextField(db_column='SkillCount2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gaugerechargable = models.TextField(db_column='GaugeRechargable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gaugestart = models.TextField(db_column='GaugeStart', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gaugemax = models.TextField(db_column='GaugeMax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactionid0 = models.TextField(db_column='CommonActionId0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactioncount0 = models.TextField(db_column='CommonActionCount0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactionid1 = models.TextField(db_column='CommonActionId1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactioncount1 = models.TextField(db_column='CommonActionCount1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactionid2 = models.TextField(db_column='CommonActionId2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactioncount2 = models.TextField(db_column='CommonActionCount2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mapicon = models.TextField(db_column='MapIcon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mappriority = models.TextField(db_column='MapPriority', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionkeyicon = models.TextField(db_column='InteractionKeyIcon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionkeystring = models.TextField(db_column='InteractionKeyString', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    professiontype = models.TextField(db_column='ProfessionType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifemethodgrade = models.TextField(db_column='LifeMethodGrade', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifecastingtier1 = models.TextField(db_column='LifeCastingTier1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifecastingtier2 = models.TextField(db_column='LifeCastingTier2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifecastingtier3 = models.TextField(db_column='LifeCastingTier3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifecastingtier4 = models.TextField(db_column='LifeCastingTier4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifecastingtier5 = models.TextField(db_column='LifeCastingTier5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifecastingtier6 = models.TextField(db_column='LifeCastingTier6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeexp = models.TextField(db_column='LifeExp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifedurability_success = models.TextField(db_column='LifeDurability_Success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifedurability_fail = models.TextField(db_column='LifeDurability_Fail', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    successrate_f = models.TextField(db_column='SuccessRate_F', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    successrate_d = models.TextField(db_column='SuccessRate_D', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    successrate_c = models.TextField(db_column='SuccessRate_C', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    successrate_b = models.TextField(db_column='SuccessRate_B', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    successrate_a = models.TextField(db_column='SuccessRate_A', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    successrate_s = models.TextField(db_column='SuccessRate_S', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeitemdroptype = models.TextField(db_column='LifeItemDropType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeitemdropindex = models.TextField(db_column='LifeItemDropIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeitemdropindex_fail = models.TextField(db_column='LifeItemDropIndex_Fail', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    miningbombrange = models.TextField(db_column='MiningBombRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    miningbombmaxtargetcount = models.TextField(db_column='MiningBombMaxTargetCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeextraconditionidonsuccess = models.TextField(db_column='LifeExtraConditionIdOnSuccess', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeextraactionidonsuccess = models.TextField(db_column='LifeExtraActionIdOnSuccess', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeextraactiononsuccessratio = models.TextField(db_column='LifeExtraActionOnSuccessRatio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeextraconditionidonfail = models.TextField(db_column='LifeExtraConditionIdOnFail', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifeextraactionidonfail = models.TextField(db_column='LifeExtraActionIdOnFail', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    barehandratio = models.TextField(db_column='BareHandRatio', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    squareholecontinent = models.TextField(db_column='SquareHoleContinent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    squareholemapindex = models.TextField(db_column='SquareHoleMapIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    squareholelevel = models.TextField(db_column='SquareHoleLevel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    squareholeuselevel = models.TextField(db_column='SquareHoleUseLevel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    squareholecostmoneybase = models.TextField(db_column='SquareHoleCostMoneyBase', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    squareholecostitemindex = models.TextField(db_column='SquareHoleCostItemIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    squarehole_ui_xlocation = models.TextField(db_column='SquareHole_UI_Xlocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    squarehole_ui_ylocation = models.TextField(db_column='SquareHole_UI_Ylocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spawnactiontime = models.TextField(db_column='SpawnActionTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    despawnactiontime = models.TextField(db_column='DespawnActionTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spawnannouncemsg = models.TextField(db_column='SpawnAnnounceMsg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactiondesc_variation = models.TextField(db_column='CommonActionDesc_Variation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EFTable_Prop'


class EftableShip(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondarykey = models.TextField(db_column='SecondaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    icon = models.TextField(db_column='Icon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iconindex = models.TextField(db_column='IconIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collisionx = models.TextField(db_column='CollisionX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collisionz = models.TextField(db_column='CollisionZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    movespeed = models.TextField(db_column='MoveSpeed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    movespeedd = models.TextField(db_column='MoveSpeedD', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    revolve = models.TextField(db_column='Revolve', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maxsupply = models.TextField(db_column='MaxSupply', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maxcrew = models.TextField(db_column='MaxCrew', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid0 = models.TextField(db_column='SkillId0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid1 = models.TextField(db_column='SkillId1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid2 = models.TextField(db_column='SkillId2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid3 = models.TextField(db_column='SkillId3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EFTable_Ship'


class EftableTower(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondarykey = models.TextField(db_column='SecondaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    radius = models.TextField(db_column='Radius', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    height = models.TextField(db_column='Height', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    faction = models.TextField(db_column='Faction', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    subfactionid = models.TextField(db_column='SubFactionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hptype = models.TextField(db_column='HpType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maxhp = models.TextField(db_column='MaxHp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    respawntype = models.TextField(db_column='RespawnType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    respawndelay = models.TextField(db_column='RespawnDelay', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    npclifetime = models.TextField(db_column='NpcLifetime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EFTable_Tower'


class EftableTrap(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondarykey = models.TextField(db_column='SecondaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    scale = models.TextField(db_column='Scale', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coltype = models.TextField(db_column='ColType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    colx = models.TextField(db_column='ColX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coly = models.TextField(db_column='ColY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    overicon = models.TextField(db_column='OverIcon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    overnametag = models.TextField(db_column='OverNameTag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    visibility = models.TextField(db_column='Visibility', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actiontype = models.TextField(db_column='ActionType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actionindex = models.TextField(db_column='ActionIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actiontime = models.TextField(db_column='ActionTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lifetime = models.TextField(db_column='Lifetime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hp = models.TextField(db_column='Hp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    faction = models.TextField(db_column='Faction', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    subfactionid = models.TextField(db_column='SubFactionId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    activetime = models.TextField(db_column='ActiveTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    expireonmasterabsence = models.TextField(db_column='ExpireOnMasterAbsence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    explodedelay = models.TextField(db_column='ExplodeDelay', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    destroydelay = models.TextField(db_column='DestroyDelay', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summongroup = models.TextField(db_column='SummonGroup', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    summoncount = models.TextField(db_column='SummonCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exclusiongroup = models.TextField(db_column='ExclusionGroup', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    exclusionrange = models.TextField(db_column='ExclusionRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectinvoke1 = models.TextField(db_column='EffectInvoke1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectinvokecount1 = models.TextField(db_column='EffectInvokeCount1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectinvoke2 = models.TextField(db_column='EffectInvoke2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectinvokecount2 = models.TextField(db_column='EffectInvokeCount2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectcount = models.TextField(db_column='EffectCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectdelay = models.TextField(db_column='EffectDelay', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectcooldown = models.TextField(db_column='EffectCooldown', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectbatchcount = models.TextField(db_column='EffectBatchCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectbatchtick = models.TextField(db_column='EffectBatchTick', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectmulti = models.TextField(db_column='EffectMulti', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectmovetarget = models.TextField(db_column='EffectMoveTarget', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    effectfiltertarget = models.TextField(db_column='EffectFilterTarget', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    uninstall = models.TextField(db_column='Uninstall', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    uninstallaffinity = models.TextField(db_column='UninstallAffinity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    uninstallrange = models.TextField(db_column='UninstallRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reactcoltype = models.TextField(db_column='ReactColType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reactcolx = models.TextField(db_column='ReactColX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reactcoly = models.TextField(db_column='ReactColY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchaffinity = models.TextField(db_column='TouchAffinity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    touchrange = models.TextField(db_column='TouchRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    linkaffinity = models.TextField(db_column='LinkAffinity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    linkcount = models.TextField(db_column='LinkCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    linkrange = models.TextField(db_column='LinkRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    inputrange = models.TextField(db_column='InputRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    synctransition = models.TextField(db_column='SyncTransition', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EFTable_Trap'


class EftableVehicle(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondarykey = models.TextField(db_column='SecondaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comment1 = models.TextField(db_column='Comment1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modelsize = models.TextField(db_column='ModelSize', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collisionx = models.TextField(db_column='CollisionX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collisionz = models.TextField(db_column='CollisionZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionrange = models.TextField(db_column='InteractionRange', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pathfindingtype = models.TextField(db_column='PathfindingType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ui = models.TextField(db_column='Ui', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mapicon = models.TextField(db_column='MapIcon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mappriority = models.TextField(db_column='MapPriority', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionkeyicon = models.TextField(db_column='InteractionKeyIcon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    interactionkeystring = models.TextField(db_column='InteractionKeyString', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fov = models.TextField(db_column='Fov', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    movespeed = models.TextField(db_column='MoveSpeed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maxhp = models.TextField(db_column='MaxHp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hptype = models.TextField(db_column='HpType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buff = models.TextField(db_column='Buff', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    seatedtime = models.TextField(db_column='SeatedTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    unseatedtime = models.TextField(db_column='UnSeatedTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid0 = models.TextField(db_column='SkillId0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillcount0 = models.TextField(db_column='SkillCount0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid1 = models.TextField(db_column='SkillId1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillcount1 = models.TextField(db_column='SkillCount1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillid2 = models.TextField(db_column='SkillId2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    skillcount2 = models.TextField(db_column='SkillCount2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactionid0 = models.TextField(db_column='CommonActionId0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactioncount0 = models.TextField(db_column='CommonActionCount0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactionid1 = models.TextField(db_column='CommonActionId1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactioncount1 = models.TextField(db_column='CommonActionCount1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactionid2 = models.TextField(db_column='CommonActionId2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    commonactioncount2 = models.TextField(db_column='CommonActionCount2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rideonkismetcamera = models.TextField(db_column='RideonKismetCamera', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dismountkismetcamera = models.TextField(db_column='DismountKismetCamera', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ridingmode = models.TextField(db_column='RidingMode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    particlesoundpackage = models.TextField(db_column='ParticleSoundPackage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EFTable_Vehicle'


class EftableZonebase(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    primarykey = models.TextField(db_column='PrimaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    secondarykey = models.TextField(db_column='SecondaryKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    continent = models.TextField(db_column='Continent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    continenttype = models.TextField(db_column='ContinentType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    groupid = models.TextField(db_column='GroupId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    contenttype = models.TextField(db_column='ContentType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sectorsize = models.TextField(db_column='SectorSize', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    maxusercount = models.TextField(db_column='MaxUserCount', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collisioncheckfriendly = models.TextField(db_column='CollisionCheckFriendly', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collisioncheckhostile = models.TextField(db_column='CollisionCheckHostile', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collisionchecknpc = models.TextField(db_column='CollisionCheckNPC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    collisioncheckpc = models.TextField(db_column='CollisionCheckPC', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    obsoletetime = models.TextField(db_column='ObsoleteTime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thumbnail = models.TextField(db_column='Thumbnail', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thumbnailindex = models.TextField(db_column='ThumbnailIndex', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    minimapzoomfactor = models.TextField(db_column='MinimapZoomFactor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startinstancedungeonquest = models.TextField(db_column='StartInstanceDungeonQuest', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    substituteconditionquestid = models.TextField(db_column='SubstituteConditionQuestId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    substitutezoneid = models.TextField(db_column='SubstituteZoneId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isprologue = models.TextField(db_column='IsPrologue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    revivecurrentlocationonly = models.TextField(db_column='ReviveCurrentLocationOnly', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ispacked = models.TextField(db_column='IsPacked', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    levelfilename = models.TextField(db_column='LevelFileName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mapsizeminx = models.TextField(db_column='MapSizeMinX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mapsizemaxx = models.TextField(db_column='MapSizeMaxX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mapsizeminy = models.TextField(db_column='MapSizeMinY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mapsizemaxy = models.TextField(db_column='MapSizeMaxY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    loadingimage = models.TextField(db_column='LoadingImage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    loadingsound = models.TextField(db_column='LoadingSound', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hintgroupid = models.TextField(db_column='HintGroupID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zonebuffid = models.TextField(db_column='ZoneBuffId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    zonebufftarget = models.TextField(db_column='ZoneBuffTarget', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    spotspawngroupid = models.TextField(db_column='SpotSpawnGroupId', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    abletouseextendmap = models.TextField(db_column='AbleToUseExtendMap', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    abletouseminimap = models.TextField(db_column='AbleToUseMiniMap', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mapimage = models.TextField(db_column='MapImage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    abletousebutton = models.TextField(db_column='AbleToUseButton', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ui_xlocation = models.TextField(db_column='UI_Xlocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ui_ylocation = models.TextField(db_column='UI_Ylocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ui_center_xlocation = models.TextField(db_column='UI_Center_XLocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ui_center_ylocation = models.TextField(db_column='UI_Center_Ylocation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'EFTable_ZoneBase'


class LookinfosDevice(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    objectname = models.TextField(db_column='ObjectName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lookinfokey = models.TextField(db_column='LookInfoKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mesh = models.TextField(db_column='Mesh', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actionobject = models.TextField(db_column='ActionObject', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animset = models.TextField(db_column='Animset', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    physicasset = models.TextField(db_column='PhysicAsset', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    particlesystem = models.TextField(db_column='ParticleSystem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'LookInfos_Device'


class LookinfosNpc(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    objecttype = models.TextField(db_column='ObjectType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lookinfokey = models.TextField(db_column='LookInfoKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    objectname = models.TextField(db_column='ObjectName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isvariation = models.TextField(db_column='IsVariation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    baseobejctname = models.TextField(db_column='BaseObejctName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    variationfrom = models.TextField(db_column='VariationFrom', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mesh = models.TextField(db_column='Mesh', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animset = models.TextField(db_column='Animset', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    physicasset = models.TextField(db_column='PhysicAsset', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actionobject = models.TextField(db_column='ActionObject', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    partsmesh_1 = models.TextField(db_column='PartsMesh_1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    partsmesh_2 = models.TextField(db_column='PartsMesh_2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    partsmesh_3 = models.TextField(db_column='PartsMesh_3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    particlesystem = models.TextField(db_column='ParticleSystem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'LookInfos_Npc'


class LookinfosProp(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    objectname = models.TextField(db_column='ObjectName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lookinfokey = models.TextField(db_column='LookInfoKey', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mesh = models.TextField(db_column='Mesh', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    material = models.TextField(db_column='Material', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    animset = models.TextField(db_column='Animset', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    physicasset = models.TextField(db_column='PhysicAsset', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    particlesystem = models.TextField(db_column='ParticleSystem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'LookInfos_Prop'


class Namedb(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # AutoField?
    key = models.TextField(db_column='Key', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    group = models.TextField(db_column='Group', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'NameDB'
