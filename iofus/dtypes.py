from iofus.binaryio import BooleanByteWrapper, ByteArray, FuncTree
from iofus.denums import *
from iofus.network import ProtocolTypeManager


class StatisticData():
    protocolId = 484

    def getTypeId(self):
        return 484

    def initStatisticData(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_StatisticData(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_StatisticData(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_StatisticData(self, param1):
        pass


class GameServerInformations():
    protocolId = 25

    def __init__(self):
        super().__init__()
        self.id = 0
        self.type = -1
        self.status = 1
        self.completion = 0
        self.isSelectable = False
        self.charactersCount = 0
        self.charactersSlots = 0
        self.date = 0

    def getTypeId(self):
        return 25

    def initGameServerInformations(self, param1=0, param2=-1, param3=1, param4=0, param5=False, param6=0, param7=0, param8=0):
        self.id = param1
        self.type = param2
        self.status = param3
        self.completion = param4
        self.isSelectable = param5
        self.charactersCount = param6
        self.charactersSlots = param7
        self.date = param8
        return self

    def reset(self):
        self.id = 0
        self.type = -1
        self.status = 1
        self.completion = 0
        self.isSelectable = False
        self.charactersCount = 0
        self.charactersSlots = 0
        self.date = 0

    def serialize(self, param1):
        self.serializeAs_GameServerInformations(param1)

    def serializeAs_GameServerInformations(self, param1):
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_var_short(self.id)
        param1.write_byte(self.type)
        param1.write_byte(self.status)
        param1.write_byte(self.completion)
        param1.write_boolean(self.isSelectable)
        if self.charactersCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.charactersCount) + ") on element charactersCount.")
        param1.write_byte(self.charactersCount)
        if self.charactersSlots < 0:
            raise RuntimeError("Forbidden value (" + str(self.charactersSlots) + ") on element charactersSlots.")
        param1.write_byte(self.charactersSlots)
        if self.date < -9007199254740990 or self.date > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.date) + ") on element date.")
        param1.write_double(self.date)

    def deserialize(self, param1):
        self.deserializeAs_GameServerInformations(param1)

    def deserializeAs_GameServerInformations(self, param1):
        self._idFunc(param1)
        self._typeFunc(param1)
        self._statusFunc(param1)
        self._completionFunc(param1)
        self._isSelectableFunc(param1)
        self._charactersCountFunc(param1)
        self._charactersSlotsFunc(param1)
        self._dateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameServerInformations(param1)

    def deserializeAsyncAs_GameServerInformations(self, param1):
        param1.add_child(self._idFunc)
        param1.add_child(self._typeFunc)
        param1.add_child(self._statusFunc)
        param1.add_child(self._completionFunc)
        param1.add_child(self._isSelectableFunc)
        param1.add_child(self._charactersCountFunc)
        param1.add_child(self._charactersSlotsFunc)
        param1.add_child(self._dateFunc)

    def _idFunc(self, param1):
        self.id = param1.read_var_uh_short()
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of GameServerInformations.id.")

    def _typeFunc(self, param1):
        self.type = param1.read_byte()

    def _statusFunc(self, param1):
        self.status = param1.read_byte()
        if self.status < 0:
            raise RuntimeError("Forbidden value (" + str(self.status) + ") on element of GameServerInformations.status.")

    def _completionFunc(self, param1):
        self.completion = param1.read_byte()
        if self.completion < 0:
            raise RuntimeError("Forbidden value (" + str(self.completion) + ") on element of GameServerInformations.completion.")

    def _isSelectableFunc(self, param1):
        self.isSelectable = param1.read_boolean()

    def _charactersCountFunc(self, param1):
        self.charactersCount = param1.read_byte()
        if self.charactersCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.charactersCount) + ") on element of GameServerInformations.charactersCount.")

    def _charactersSlotsFunc(self, param1):
        self.charactersSlots = param1.read_byte()
        if self.charactersSlots < 0:
            raise RuntimeError("Forbidden value (" + str(self.charactersSlots) + ") on element of GameServerInformations.charactersSlots.")

    def _dateFunc(self, param1):
        self.date = param1.read_double()
        if self.date < -9007199254740990 or self.date > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.date) + ") on element of GameServerInformations.date.")


class Achievement():
    protocolId = 363

    def __init__(self):
        super().__init__()
        self.id = 0
        self.finishedObjective = []
        self.startedObjectives = []
        self._finishedObjectivetree = FuncTree()
        self._startedObjectivestree = FuncTree()

    def getTypeId(self):
        return 363

    def initAchievement(self, param1=0, param2=[], param3=[]):
        self.id = param1
        self.finishedObjective = param2
        self.startedObjectives = param3
        return self

    def reset(self):
        self.id = 0
        self.finishedObjective = []
        self.startedObjectives = []

    def serialize(self, param1):
        self.serializeAs_Achievement(param1)

    def serializeAs_Achievement(self, param1):
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_var_short(self.id)
        param1.write_short(len(self.finishedObjective))
        _loc2_ = 0
        while _loc2_ < len(self.finishedObjective):
            as_parent(self.finishedObjective[_loc2_], AchievementObjective).serializeAs_AchievementObjective(param1)
            _loc2_ += 1
        param1.write_short(len(self.startedObjectives))
        _loc3_ = 0
        while _loc3_ < len(self.startedObjectives):
            as_parent(self.startedObjectives[_loc3_], AchievementStartedObjective).serializeAs_AchievementStartedObjective(param1)
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_Achievement(param1)

    def deserializeAs_Achievement(self, param1):
        _loc6_ = None
        _loc7_ = None
        self._idFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = AchievementObjective()
            _loc6_.deserialize(param1)
            self.finishedObjective.append(_loc6_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc7_ = AchievementStartedObjective()
            _loc7_.deserialize(param1)
            self.startedObjectives.append(_loc7_)
            _loc5_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_Achievement(param1)

    def deserializeAsyncAs_Achievement(self, param1):
        param1.add_child(self._idFunc)
        self._finishedObjectivetree = param1.add_child(self._finishedObjectivetreeFunc)
        self._startedObjectivestree = param1.add_child(self._startedObjectivestreeFunc)

    def _idFunc(self, param1):
        self.id = param1.read_var_uh_short()
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of Achievement.id.")

    def _finishedObjectivetreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._finishedObjectivetree.add_child(self._finishedObjectiveFunc)
            _loc3_ += 1

    def _finishedObjectiveFunc(self, param1):
        _loc2_ = AchievementObjective()
        _loc2_.deserialize(param1)
        self.finishedObjective.append(_loc2_)

    def _startedObjectivestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._startedObjectivestree.add_child(self._startedObjectivesFunc)
            _loc3_ += 1

    def _startedObjectivesFunc(self, param1):
        _loc2_ = AchievementStartedObjective()
        _loc2_.deserialize(param1)
        self.startedObjectives.append(_loc2_)


class AchievementObjective():
    protocolId = 404

    def __init__(self):
        super().__init__()
        self.id = 0
        self.maxValue = 0

    def getTypeId(self):
        return 404

    def initAchievementObjective(self, param1=0, param2=0):
        self.id = param1
        self.maxValue = param2
        return self

    def reset(self):
        self.id = 0
        self.maxValue = 0

    def serialize(self, param1):
        self.serializeAs_AchievementObjective(param1)

    def serializeAs_AchievementObjective(self, param1):
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_var_int(self.id)
        if self.maxValue < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxValue) + ") on element maxValue.")
        param1.write_var_short(self.maxValue)

    def deserialize(self, param1):
        self.deserializeAs_AchievementObjective(param1)

    def deserializeAs_AchievementObjective(self, param1):
        self._idFunc(param1)
        self._maxValueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AchievementObjective(param1)

    def deserializeAsyncAs_AchievementObjective(self, param1):
        param1.add_child(self._idFunc)
        param1.add_child(self._maxValueFunc)

    def _idFunc(self, param1):
        self.id = param1.read_var_uh_int()
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of AchievementObjective.id.")

    def _maxValueFunc(self, param1):
        self.maxValue = param1.read_var_uh_short()
        if self.maxValue < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxValue) + ") on element of AchievementObjective.maxValue.")


class AchievementRewardable():
    protocolId = 412

    def __init__(self):
        super().__init__()
        self.id = 0
        self.finishedlevel = 0

    def getTypeId(self):
        return 412

    def initAchievementRewardable(self, param1=0, param2=0):
        self.id = param1
        self.finishedlevel = param2
        return self

    def reset(self):
        self.id = 0
        self.finishedlevel = 0

    def serialize(self, param1):
        self.serializeAs_AchievementRewardable(param1)

    def serializeAs_AchievementRewardable(self, param1):
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_var_short(self.id)
        if self.finishedlevel < 0 or self.finishedlevel > 206:
            raise RuntimeError("Forbidden value (" + str(self.finishedlevel) + ") on element finishedlevel.")
        param1.write_byte(self.finishedlevel)

    def deserialize(self, param1):
        self.deserializeAs_AchievementRewardable(param1)

    def deserializeAs_AchievementRewardable(self, param1):
        self._idFunc(param1)
        self._finishedlevelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AchievementRewardable(param1)

    def deserializeAsyncAs_AchievementRewardable(self, param1):
        param1.add_child(self._idFunc)
        param1.add_child(self._finishedlevelFunc)

    def _idFunc(self, param1):
        self.id = param1.read_var_uh_short()
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of AchievementRewardable.id.")

    def _finishedlevelFunc(self, param1):
        self.finishedlevel = param1.read_unsigned_byte()
        if self.finishedlevel < 0 or self.finishedlevel > 206:
            raise RuntimeError("Forbidden value (" + str(self.finishedlevel) + ") on element of AchievementRewardable.finishedlevel.")


class FightDispellableEffectExtendedInformations():
    protocolId = 208

    def __init__(self):
        super().__init__()
        self.actionId = 0
        self.sourceId = 0
        self.effect = AbstractFightDispellableEffect()
        self._effecttree = FuncTree()

    def getTypeId(self):
        return 208

    def initFightDispellableEffectExtendedInformations(self, param1=0, param2=0, param3=None):
        self.actionId = param1
        self.sourceId = param2
        self.effect = param3
        return self

    def reset(self):
        self.actionId = 0
        self.sourceId = 0
        self.effect = AbstractFightDispellableEffect()

    def serialize(self, param1):
        self.serializeAs_FightDispellableEffectExtendedInformations(param1)

    def serializeAs_FightDispellableEffectExtendedInformations(self, param1):
        if self.actionId < 0:
            raise RuntimeError("Forbidden value (" + str(self.actionId) + ") on element actionId.")
        param1.write_var_short(self.actionId)
        if self.sourceId < -9007199254740990 or self.sourceId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.sourceId) + ") on element sourceId.")
        param1.write_double(self.sourceId)
        param1.write_short(self.effect.getTypeId())
        self.effect.serialize(param1)

    def deserialize(self, param1):
        self.deserializeAs_FightDispellableEffectExtendedInformations(param1)

    def deserializeAs_FightDispellableEffectExtendedInformations(self, param1):
        self._actionIdFunc(param1)
        self._sourceIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        self.effect = ProtocolTypeManager.get_instance(AbstractFightDispellableEffect,_loc2_)
        self.effect.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightDispellableEffectExtendedInformations(param1)

    def deserializeAsyncAs_FightDispellableEffectExtendedInformations(self, param1):
        param1.add_child(self._actionIdFunc)
        param1.add_child(self._sourceIdFunc)
        self._effecttree = param1.add_child(self._effecttreeFunc)

    def _actionIdFunc(self, param1):
        self.actionId = param1.read_var_uh_short()
        if self.actionId < 0:
            raise RuntimeError("Forbidden value (" + str(self.actionId) + ") on element of FightDispellableEffectExtendedInformations.actionId.")

    def _sourceIdFunc(self, param1):
        self.sourceId = param1.read_double()
        if self.sourceId < -9007199254740990 or self.sourceId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.sourceId) + ") on element of FightDispellableEffectExtendedInformations.sourceId.")

    def _effecttreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.effect = ProtocolTypeManager.get_instance(AbstractFightDispellableEffect,_loc2_)
        self.effect.deserializeAsync(self._effecttree)


class AbstractFightDispellableEffect():
    protocolId = 206

    def __init__(self):
        super().__init__()
        self.uid = 0
        self.targetId = 0
        self.turnDuration = 0
        self.dispelable = 1
        self.spellId = 0
        self.effectId = 0
        self.parentBoostUid = 0

    def getTypeId(self):
        return 206

    def initAbstractFightDispellableEffect(self, param1=0, param2=0, param3=0, param4=1, param5=0, param6=0, param7=0):
        self.uid = param1
        self.targetId = param2
        self.turnDuration = param3
        self.dispelable = param4
        self.spellId = param5
        self.effectId = param6
        self.parentBoostUid = param7
        return self

    def reset(self):
        self.uid = 0
        self.targetId = 0
        self.turnDuration = 0
        self.dispelable = 1
        self.spellId = 0
        self.effectId = 0
        self.parentBoostUid = 0

    def serialize(self, param1):
        self.serializeAs_AbstractFightDispellableEffect(param1)

    def serializeAs_AbstractFightDispellableEffect(self, param1):
        if self.uid < 0:
            raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element uid.")
        param1.write_var_int(self.uid)
        if self.targetId < -9007199254740990 or self.targetId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element targetId.")
        param1.write_double(self.targetId)
        param1.write_short(self.turnDuration)
        param1.write_byte(self.dispelable)
        if self.spellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element spellId.")
        param1.write_var_short(self.spellId)
        if self.effectId < 0:
            raise RuntimeError("Forbidden value (" + str(self.effectId) + ") on element effectId.")
        param1.write_var_int(self.effectId)
        if self.parentBoostUid < 0:
            raise RuntimeError("Forbidden value (" + str(self.parentBoostUid) + ") on element parentBoostUid.")
        param1.write_var_int(self.parentBoostUid)

    def deserialize(self, param1):
        self.deserializeAs_AbstractFightDispellableEffect(param1)

    def deserializeAs_AbstractFightDispellableEffect(self, param1):
        self._uidFunc(param1)
        self._targetIdFunc(param1)
        self._turnDurationFunc(param1)
        self._dispelableFunc(param1)
        self._spellIdFunc(param1)
        self._effectIdFunc(param1)
        self._parentBoostUidFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AbstractFightDispellableEffect(param1)

    def deserializeAsyncAs_AbstractFightDispellableEffect(self, param1):
        param1.add_child(self._uidFunc)
        param1.add_child(self._targetIdFunc)
        param1.add_child(self._turnDurationFunc)
        param1.add_child(self._dispelableFunc)
        param1.add_child(self._spellIdFunc)
        param1.add_child(self._effectIdFunc)
        param1.add_child(self._parentBoostUidFunc)

    def _uidFunc(self, param1):
        self.uid = param1.read_var_uh_int()
        if self.uid < 0:
            raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element of AbstractFightDispellableEffect.uid.")

    def _targetIdFunc(self, param1):
        self.targetId = param1.read_double()
        if self.targetId < -9007199254740990 or self.targetId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of AbstractFightDispellableEffect.targetId.")

    def _turnDurationFunc(self, param1):
        self.turnDuration = param1.read_short()

    def _dispelableFunc(self, param1):
        self.dispelable = param1.read_byte()
        if self.dispelable < 0:
            raise RuntimeError("Forbidden value (" + str(self.dispelable) + ") on element of AbstractFightDispellableEffect.dispelable.")

    def _spellIdFunc(self, param1):
        self.spellId = param1.read_var_uh_short()
        if self.spellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of AbstractFightDispellableEffect.spellId.")

    def _effectIdFunc(self, param1):
        self.effectId = param1.read_var_uh_int()
        if self.effectId < 0:
            raise RuntimeError("Forbidden value (" + str(self.effectId) + ") on element of AbstractFightDispellableEffect.effectId.")

    def _parentBoostUidFunc(self, param1):
        self.parentBoostUid = param1.read_var_uh_int()
        if self.parentBoostUid < 0:
            raise RuntimeError("Forbidden value (" + str(self.parentBoostUid) + ") on element of AbstractFightDispellableEffect.parentBoostUid.")


class GameActionMark():
    protocolId = 351

    def __init__(self):
        super().__init__()
        self.markAuthorId = 0
        self.markTeamId = 2
        self.markSpellId = 0
        self.markSpellLevel = 0
        self.markId = 0
        self.markType = 0
        self.markimpactCell = 0
        self.cells = []
        self.active = False
        self._cellstree = FuncTree()

    def getTypeId(self):
        return 351

    def initGameActionMark(self, param1=0, param2=2, param3=0, param4=0, param5=0, param6=0, param7=0, param8=[], param9=False):
        self.markAuthorId = param1
        self.markTeamId = param2
        self.markSpellId = param3
        self.markSpellLevel = param4
        self.markId = param5
        self.markType = param6
        self.markimpactCell = param7
        self.cells = param8
        self.active = param9
        return self

    def reset(self):
        self.markAuthorId = 0
        self.markTeamId = 2
        self.markSpellId = 0
        self.markSpellLevel = 0
        self.markId = 0
        self.markType = 0
        self.markimpactCell = 0
        self.cells = []
        self.active = False

    def serialize(self, param1):
        self.serializeAs_GameActionMark(param1)

    def serializeAs_GameActionMark(self, param1):
        if self.markAuthorId < -9007199254740990 or self.markAuthorId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.markAuthorId) + ") on element markAuthorId.")
        param1.write_double(self.markAuthorId)
        param1.write_byte(self.markTeamId)
        if self.markSpellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.markSpellId) + ") on element markSpellId.")
        param1.write_int(self.markSpellId)
        if self.markSpellLevel < 1 or self.markSpellLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.markSpellLevel) + ") on element markSpellLevel.")
        param1.write_short(self.markSpellLevel)
        param1.write_short(self.markId)
        param1.write_byte(self.markType)
        if self.markimpactCell < -1 or self.markimpactCell > 559:
            raise RuntimeError("Forbidden value (" + str(self.markimpactCell) + ") on element markimpactCell.")
        param1.write_short(self.markimpactCell)
        param1.write_short(len(self.cells))
        _loc2_ = 0
        while _loc2_ < len(self.cells):
            as_parent(self.cells[_loc2_], GameActionMarkedCell).serializeAs_GameActionMarkedCell(param1)
            _loc2_ += 1
        param1.write_boolean(self.active)

    def deserialize(self, param1):
        self.deserializeAs_GameActionMark(param1)

    def deserializeAs_GameActionMark(self, param1):
        _loc4_ = None
        self._markAuthorIdFunc(param1)
        self._markTeamIdFunc(param1)
        self._markSpellIdFunc(param1)
        self._markSpellLevelFunc(param1)
        self._markIdFunc(param1)
        self._markTypeFunc(param1)
        self._markimpactCellFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = GameActionMarkedCell()
            _loc4_.deserialize(param1)
            self.cells.append(_loc4_)
            _loc3_ += 1
        self._activeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameActionMark(param1)

    def deserializeAsyncAs_GameActionMark(self, param1):
        param1.add_child(self._markAuthorIdFunc)
        param1.add_child(self._markTeamIdFunc)
        param1.add_child(self._markSpellIdFunc)
        param1.add_child(self._markSpellLevelFunc)
        param1.add_child(self._markIdFunc)
        param1.add_child(self._markTypeFunc)
        param1.add_child(self._markimpactCellFunc)
        self._cellstree = param1.add_child(self._cellstreeFunc)
        param1.add_child(self._activeFunc)

    def _markAuthorIdFunc(self, param1):
        self.markAuthorId = param1.read_double()
        if self.markAuthorId < -9007199254740990 or self.markAuthorId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.markAuthorId) + ") on element of GameActionMark.markAuthorId.")

    def _markTeamIdFunc(self, param1):
        self.markTeamId = param1.read_byte()
        if self.markTeamId < 0:
            raise RuntimeError("Forbidden value (" + str(self.markTeamId) + ") on element of GameActionMark.markTeamId.")

    def _markSpellIdFunc(self, param1):
        self.markSpellId = param1.read_int()
        if self.markSpellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.markSpellId) + ") on element of GameActionMark.markSpellId.")

    def _markSpellLevelFunc(self, param1):
        self.markSpellLevel = param1.read_short()
        if self.markSpellLevel < 1 or self.markSpellLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.markSpellLevel) + ") on element of GameActionMark.markSpellLevel.")

    def _markIdFunc(self, param1):
        self.markId = param1.read_short()

    def _markTypeFunc(self, param1):
        self.markType = param1.read_byte()

    def _markimpactCellFunc(self, param1):
        self.markimpactCell = param1.read_short()
        if self.markimpactCell < -1 or self.markimpactCell > 559:
            raise RuntimeError("Forbidden value (" + str(self.markimpactCell) + ") on element of GameActionMark.markimpactCell.")

    def _cellstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._cellstree.add_child(self._cellsFunc)
            _loc3_ += 1

    def _cellsFunc(self, param1):
        _loc2_ = GameActionMarkedCell()
        _loc2_.deserialize(param1)
        self.cells.append(_loc2_)

    def _activeFunc(self, param1):
        self.active = param1.read_boolean()


class GameActionMarkedCell():
    protocolId = 85

    def __init__(self):
        super().__init__()
        self.cellId = 0
        self.zoneSize = 0
        self.cellColor = 0
        self.cellsType = 0

    def getTypeId(self):
        return 85

    def initGameActionMarkedCell(self, param1=0, param2=0, param3=0, param4=0):
        self.cellId = param1
        self.zoneSize = param2
        self.cellColor = param3
        self.cellsType = param4
        return self

    def reset(self):
        self.cellId = 0
        self.zoneSize = 0
        self.cellColor = 0
        self.cellsType = 0

    def serialize(self, param1):
        self.serializeAs_GameActionMarkedCell(param1)

    def serializeAs_GameActionMarkedCell(self, param1):
        if self.cellId < 0 or self.cellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element cellId.")
        param1.write_var_short(self.cellId)
        param1.write_byte(self.zoneSize)
        param1.write_int(self.cellColor)
        param1.write_byte(self.cellsType)

    def deserialize(self, param1):
        self.deserializeAs_GameActionMarkedCell(param1)

    def deserializeAs_GameActionMarkedCell(self, param1):
        self._cellIdFunc(param1)
        self._zoneSizeFunc(param1)
        self._cellColorFunc(param1)
        self._cellsTypeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameActionMarkedCell(param1)

    def deserializeAsyncAs_GameActionMarkedCell(self, param1):
        param1.add_child(self._cellIdFunc)
        param1.add_child(self._zoneSizeFunc)
        param1.add_child(self._cellColorFunc)
        param1.add_child(self._cellsTypeFunc)

    def _cellIdFunc(self, param1):
        self.cellId = param1.read_var_uh_short()
        if self.cellId < 0 or self.cellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of GameActionMarkedCell.cellId.")

    def _zoneSizeFunc(self, param1):
        self.zoneSize = param1.read_byte()

    def _cellColorFunc(self, param1):
        self.cellColor = param1.read_int()

    def _cellsTypeFunc(self, param1):
        self.cellsType = param1.read_byte()


class ServerSessionConstant():
    protocolId = 430

    def __init__(self):
        super().__init__()
        self.id = 0

    def getTypeId(self):
        return 430

    def initServerSessionConstant(self, param1=0):
        self.id = param1
        return self

    def reset(self):
        self.id = 0

    def serialize(self, param1):
        self.serializeAs_ServerSessionConstant(param1)

    def serializeAs_ServerSessionConstant(self, param1):
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_var_short(self.id)

    def deserialize(self, param1):
        self.deserializeAs_ServerSessionConstant(param1)

    def deserializeAs_ServerSessionConstant(self, param1):
        self._idFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ServerSessionConstant(param1)

    def deserializeAsyncAs_ServerSessionConstant(self, param1):
        param1.add_child(self._idFunc)

    def _idFunc(self, param1):
        self.id = param1.read_var_uh_short()
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of ServerSessionConstant.id.")


class AbstractCharacterInformation():
    protocolId = 400

    def __init__(self):
        super().__init__()
        self.id = 0

    def getTypeId(self):
        return 400

    def initAbstractCharacterInformation(self, param1=0):
        self.id = param1
        return self

    def reset(self):
        self.id = 0

    def serialize(self, param1):
        self.serializeAs_AbstractCharacterInformation(param1)

    def serializeAs_AbstractCharacterInformation(self, param1):
        if self.id < 0 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_var_long(self.id)

    def deserialize(self, param1):
        self.deserializeAs_AbstractCharacterInformation(param1)

    def deserializeAs_AbstractCharacterInformation(self, param1):
        self._idFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AbstractCharacterInformation(param1)

    def deserializeAsyncAs_AbstractCharacterInformation(self, param1):
        param1.add_child(self._idFunc)

    def _idFunc(self, param1):
        self.id = param1.read_var_uh_long()
        if self.id < 0 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of AbstractCharacterInformation.id.")


class ActorAlignmentInformations():
    protocolId = 201

    def __init__(self):
        super().__init__()
        self.alignmentSide = 0
        self.alignmentValue = 0
        self.alignmentGrade = 0
        self.characterPower = 0

    def getTypeId(self):
        return 201

    def initActorAlignmentInformations(self, param1=0, param2=0, param3=0, param4=0):
        self.alignmentSide = param1
        self.alignmentValue = param2
        self.alignmentGrade = param3
        self.characterPower = param4
        return self

    def reset(self):
        self.alignmentSide = 0
        self.alignmentValue = 0
        self.alignmentGrade = 0
        self.characterPower = 0

    def serialize(self, param1):
        self.serializeAs_ActorAlignmentInformations(param1)

    def serializeAs_ActorAlignmentInformations(self, param1):
        param1.write_byte(self.alignmentSide)
        if self.alignmentValue < 0:
            raise RuntimeError("Forbidden value (" + str(self.alignmentValue) + ") on element alignmentValue.")
        param1.write_byte(self.alignmentValue)
        if self.alignmentGrade < 0:
            raise RuntimeError("Forbidden value (" + str(self.alignmentGrade) + ") on element alignmentGrade.")
        param1.write_byte(self.alignmentGrade)
        if self.characterPower < -9007199254740990 or self.characterPower > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.characterPower) + ") on element characterPower.")
        param1.write_double(self.characterPower)

    def deserialize(self, param1):
        self.deserializeAs_ActorAlignmentInformations(param1)

    def deserializeAs_ActorAlignmentInformations(self, param1):
        self._alignmentSideFunc(param1)
        self._alignmentValueFunc(param1)
        self._alignmentGradeFunc(param1)
        self._characterPowerFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ActorAlignmentInformations(param1)

    def deserializeAsyncAs_ActorAlignmentInformations(self, param1):
        param1.add_child(self._alignmentSideFunc)
        param1.add_child(self._alignmentValueFunc)
        param1.add_child(self._alignmentGradeFunc)
        param1.add_child(self._characterPowerFunc)

    def _alignmentSideFunc(self, param1):
        self.alignmentSide = param1.read_byte()

    def _alignmentValueFunc(self, param1):
        self.alignmentValue = param1.read_byte()
        if self.alignmentValue < 0:
            raise RuntimeError("Forbidden value (" + str(self.alignmentValue) + ") on element of ActorAlignmentInformations.alignmentValue.")

    def _alignmentGradeFunc(self, param1):
        self.alignmentGrade = param1.read_byte()
        if self.alignmentGrade < 0:
            raise RuntimeError("Forbidden value (" + str(self.alignmentGrade) + ") on element of ActorAlignmentInformations.alignmentGrade.")

    def _characterPowerFunc(self, param1):
        self.characterPower = param1.read_double()
        if self.characterPower < -9007199254740990 or self.characterPower > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.characterPower) + ") on element of ActorAlignmentInformations.characterPower.")


class CharacterBaseCharacteristic():
    protocolId = 4

    def __init__(self):
        super().__init__()
        self.base = 0
        self.additionnal = 0
        self.objectsAndMountBonus = 0
        self.alignGiftBonus = 0
        self.contextModif = 0

    def getTypeId(self):
        return 4

    def initCharacterBaseCharacteristic(self, param1=0, param2=0, param3=0, param4=0, param5=0):
        self.base = param1
        self.additionnal = param2
        self.objectsAndMountBonus = param3
        self.alignGiftBonus = param4
        self.contextModif = param5
        return self

    def reset(self):
        self.base = 0
        self.additionnal = 0
        self.objectsAndMountBonus = 0
        self.alignGiftBonus = 0
        self.contextModif = 0

    def serialize(self, param1):
        self.serializeAs_CharacterBaseCharacteristic(param1)

    def serializeAs_CharacterBaseCharacteristic(self, param1):
        param1.write_var_short(self.base)
        param1.write_var_short(self.additionnal)
        param1.write_var_short(self.objectsAndMountBonus)
        param1.write_var_short(self.alignGiftBonus)
        param1.write_var_short(self.contextModif)

    def deserialize(self, param1):
        self.deserializeAs_CharacterBaseCharacteristic(param1)

    def deserializeAs_CharacterBaseCharacteristic(self, param1):
        self._baseFunc(param1)
        self._additionnalFunc(param1)
        self._objectsAndMountBonusFunc(param1)
        self._alignGiftBonusFunc(param1)
        self._contextModifFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterBaseCharacteristic(param1)

    def deserializeAsyncAs_CharacterBaseCharacteristic(self, param1):
        param1.add_child(self._baseFunc)
        param1.add_child(self._additionnalFunc)
        param1.add_child(self._objectsAndMountBonusFunc)
        param1.add_child(self._alignGiftBonusFunc)
        param1.add_child(self._contextModifFunc)

    def _baseFunc(self, param1):
        self.base = param1.read_var_short()

    def _additionnalFunc(self, param1):
        self.additionnal = param1.read_var_short()

    def _objectsAndMountBonusFunc(self, param1):
        self.objectsAndMountBonus = param1.read_var_short()

    def _alignGiftBonusFunc(self, param1):
        self.alignGiftBonus = param1.read_var_short()

    def _contextModifFunc(self, param1):
        self.contextModif = param1.read_var_short()


class CharacterCharacteristicsInformations():
    protocolId = 8

    def __init__(self):
        super().__init__()
        self.experience = 0
        self.experienceLevelFloor = 0
        self.experienceNextLevelFloor = 0
        self.experienceBonusLimit = 0
        self.kamas = 0
        self.statsPoints = 0
        self.additionnalPoints = 0
        self.spellsPoints = 0
        self.alignmentInfos = ActorExtendedAlignmentInformations()
        self.lifePoints = 0
        self.maxLifePoints = 0
        self.energyPoints = 0
        self.maxEnergyPoints = 0
        self.actionPointsCurrent = 0
        self.movementPointsCurrent = 0
        self.initiative = CharacterBaseCharacteristic()
        self.prospecting = CharacterBaseCharacteristic()
        self.actionPoints = CharacterBaseCharacteristic()
        self.movementPoints = CharacterBaseCharacteristic()
        self.strength = CharacterBaseCharacteristic()
        self.vitality = CharacterBaseCharacteristic()
        self.wisdom = CharacterBaseCharacteristic()
        self.chance = CharacterBaseCharacteristic()
        self.agility = CharacterBaseCharacteristic()
        self.intelligence = CharacterBaseCharacteristic()
        self.range = CharacterBaseCharacteristic()
        self.summonableCreaturesBoost = CharacterBaseCharacteristic()
        self.reflect = CharacterBaseCharacteristic()
        self.criticalHit = CharacterBaseCharacteristic()
        self.criticalHitWeapon = 0
        self.criticalMiss = CharacterBaseCharacteristic()
        self.healBonus = CharacterBaseCharacteristic()
        self.allDamagesBonus = CharacterBaseCharacteristic()
        self.weaponDamagesBonusPercent = CharacterBaseCharacteristic()
        self.damagesBonusPercent = CharacterBaseCharacteristic()
        self.trapBonus = CharacterBaseCharacteristic()
        self.trapBonusPercent = CharacterBaseCharacteristic()
        self.glyphBonusPercent = CharacterBaseCharacteristic()
        self.runeBonusPercent = CharacterBaseCharacteristic()
        self.permanentDamagePercent = CharacterBaseCharacteristic()
        self.tackleBlock = CharacterBaseCharacteristic()
        self.tackleEvade = CharacterBaseCharacteristic()
        self.PAAttack = CharacterBaseCharacteristic()
        self.PMAttack = CharacterBaseCharacteristic()
        self.pushDamageBonus = CharacterBaseCharacteristic()
        self.criticalDamageBonus = CharacterBaseCharacteristic()
        self.neutralDamageBonus = CharacterBaseCharacteristic()
        self.earthDamageBonus = CharacterBaseCharacteristic()
        self.waterDamageBonus = CharacterBaseCharacteristic()
        self.airDamageBonus = CharacterBaseCharacteristic()
        self.fireDamageBonus = CharacterBaseCharacteristic()
        self.dodgePALostProbability = CharacterBaseCharacteristic()
        self.dodgePMLostProbability = CharacterBaseCharacteristic()
        self.neutralElementResistPercent = CharacterBaseCharacteristic()
        self.earthElementResistPercent = CharacterBaseCharacteristic()
        self.waterElementResistPercent = CharacterBaseCharacteristic()
        self.airElementResistPercent = CharacterBaseCharacteristic()
        self.fireElementResistPercent = CharacterBaseCharacteristic()
        self.neutralElementReduction = CharacterBaseCharacteristic()
        self.earthElementReduction = CharacterBaseCharacteristic()
        self.waterElementReduction = CharacterBaseCharacteristic()
        self.airElementReduction = CharacterBaseCharacteristic()
        self.fireElementReduction = CharacterBaseCharacteristic()
        self.pushDamageReduction = CharacterBaseCharacteristic()
        self.criticalDamageReduction = CharacterBaseCharacteristic()
        self.pvpNeutralElementResistPercent = CharacterBaseCharacteristic()
        self.pvpEarthElementResistPercent = CharacterBaseCharacteristic()
        self.pvpWaterElementResistPercent = CharacterBaseCharacteristic()
        self.pvpAirElementResistPercent = CharacterBaseCharacteristic()
        self.pvpFireElementResistPercent = CharacterBaseCharacteristic()
        self.pvpNeutralElementReduction = CharacterBaseCharacteristic()
        self.pvpEarthElementReduction = CharacterBaseCharacteristic()
        self.pvpWaterElementReduction = CharacterBaseCharacteristic()
        self.pvpAirElementReduction = CharacterBaseCharacteristic()
        self.pvpFireElementReduction = CharacterBaseCharacteristic()
        self.meleeDamageDonePercent = CharacterBaseCharacteristic()
        self.meleeDamageReceivedPercent = CharacterBaseCharacteristic()
        self.rangedDamageDonePercent = CharacterBaseCharacteristic()
        self.rangedDamageReceivedPercent = CharacterBaseCharacteristic()
        self.weaponDamageDonePercent = CharacterBaseCharacteristic()
        self.weaponDamageReceivedPercent = CharacterBaseCharacteristic()
        self.spellDamageDonePercent = CharacterBaseCharacteristic()
        self.spellDamageReceivedPercent = CharacterBaseCharacteristic()
        self.spellModifications = []
        self.probationTime = 0
        self._alignmentInfostree = FuncTree()
        self._initiativetree = FuncTree()
        self._prospectingtree = FuncTree()
        self._actionPointstree = FuncTree()
        self._movementPointstree = FuncTree()
        self._strengthtree = FuncTree()
        self._vitalitytree = FuncTree()
        self._wisdomtree = FuncTree()
        self._chancetree = FuncTree()
        self._agilitytree = FuncTree()
        self._intelligencetree = FuncTree()
        self._rangetree = FuncTree()
        self._summonableCreaturesBoosttree = FuncTree()
        self._reflecttree = FuncTree()
        self._criticalHittree = FuncTree()
        self._criticalMisstree = FuncTree()
        self._healBonustree = FuncTree()
        self._allDamagesBonustree = FuncTree()
        self._weaponDamagesBonusPercenttree = FuncTree()
        self._damagesBonusPercenttree = FuncTree()
        self._trapBonustree = FuncTree()
        self._trapBonusPercenttree = FuncTree()
        self._glyphBonusPercenttree = FuncTree()
        self._runeBonusPercenttree = FuncTree()
        self._permanentDamagePercenttree = FuncTree()
        self._tackleBlocktree = FuncTree()
        self._tackleEvadetree = FuncTree()
        self._PAAttacktree = FuncTree()
        self._PMAttacktree = FuncTree()
        self._pushDamageBonustree = FuncTree()
        self._criticalDamageBonustree = FuncTree()
        self._neutralDamageBonustree = FuncTree()
        self._earthDamageBonustree = FuncTree()
        self._waterDamageBonustree = FuncTree()
        self._airDamageBonustree = FuncTree()
        self._fireDamageBonustree = FuncTree()
        self._dodgePALostProbabilitytree = FuncTree()
        self._dodgePMLostProbabilitytree = FuncTree()
        self._neutralElementResistPercenttree = FuncTree()
        self._earthElementResistPercenttree = FuncTree()
        self._waterElementResistPercenttree = FuncTree()
        self._airElementResistPercenttree = FuncTree()
        self._fireElementResistPercenttree = FuncTree()
        self._neutralElementReductiontree = FuncTree()
        self._earthElementReductiontree = FuncTree()
        self._waterElementReductiontree = FuncTree()
        self._airElementReductiontree = FuncTree()
        self._fireElementReductiontree = FuncTree()
        self._pushDamageReductiontree = FuncTree()
        self._criticalDamageReductiontree = FuncTree()
        self._pvpNeutralElementResistPercenttree = FuncTree()
        self._pvpEarthElementResistPercenttree = FuncTree()
        self._pvpWaterElementResistPercenttree = FuncTree()
        self._pvpAirElementResistPercenttree = FuncTree()
        self._pvpFireElementResistPercenttree = FuncTree()
        self._pvpNeutralElementReductiontree = FuncTree()
        self._pvpEarthElementReductiontree = FuncTree()
        self._pvpWaterElementReductiontree = FuncTree()
        self._pvpAirElementReductiontree = FuncTree()
        self._pvpFireElementReductiontree = FuncTree()
        self._meleeDamageDonePercenttree = FuncTree()
        self._meleeDamageReceivedPercenttree = FuncTree()
        self._rangedDamageDonePercenttree = FuncTree()
        self._rangedDamageReceivedPercenttree = FuncTree()
        self._weaponDamageDonePercenttree = FuncTree()
        self._weaponDamageReceivedPercenttree = FuncTree()
        self._spellDamageDonePercenttree = FuncTree()
        self._spellDamageReceivedPercenttree = FuncTree()
        self._spellModificationstree = FuncTree()

    def getTypeId(self):
        return 8

    def initCharacterCharacteristicsInformations(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0, param8=0, param9=None, param10=0, param11=0, param12=0, param13=0, param14=0, param15=0, param16=None, param17=None, param18=None, param19=None, param20=None, param21=None, param22=None, param23=None, param24=None, param25=None, param26=None, param27=None, param28=None, param29=None, param30=0, param31=None, param32=None, param33=None, param34=None, param35=None, param36=None, param37=None, param38=None, param39=None, param40=None, param41=None, param42=None, param43=None, param44=None, param45=None, param46=None, param47=None, param48=None, param49=None, param50=None, param51=None, param52=None, param53=None, param54=None, param55=None, param56=None, param57=None, param58=None, param59=None, param60=None, param61=None, param62=None, param63=None, param64=None, param65=None, param66=None, param67=None, param68=None, param69=None, param70=None, param71=None, param72=None, param73=None, param74=None, param75=None, param76=None, param77=None, param78=None, param79=None, param80=None, param81=None, param82=None, param83=None, param84=[], param85=0):
        self.experience = param1
        self.experienceLevelFloor = param2
        self.experienceNextLevelFloor = param3
        self.experienceBonusLimit = param4
        self.kamas = param5
        self.statsPoints = param6
        self.additionnalPoints = param7
        self.spellsPoints = param8
        self.alignmentInfos = param9
        self.lifePoints = param10
        self.maxLifePoints = param11
        self.energyPoints = param12
        self.maxEnergyPoints = param13
        self.actionPointsCurrent = param14
        self.movementPointsCurrent = param15
        self.initiative = param16
        self.prospecting = param17
        self.actionPoints = param18
        self.movementPoints = param19
        self.strength = param20
        self.vitality = param21
        self.wisdom = param22
        self.chance = param23
        self.agility = param24
        self.intelligence = param25
        self.range = param26
        self.summonableCreaturesBoost = param27
        self.reflect = param28
        self.criticalHit = param29
        self.criticalHitWeapon = param30
        self.criticalMiss = param31
        self.healBonus = param32
        self.allDamagesBonus = param33
        self.weaponDamagesBonusPercent = param34
        self.damagesBonusPercent = param35
        self.trapBonus = param36
        self.trapBonusPercent = param37
        self.glyphBonusPercent = param38
        self.runeBonusPercent = param39
        self.permanentDamagePercent = param40
        self.tackleBlock = param41
        self.tackleEvade = param42
        self.PAAttack = param43
        self.PMAttack = param44
        self.pushDamageBonus = param45
        self.criticalDamageBonus = param46
        self.neutralDamageBonus = param47
        self.earthDamageBonus = param48
        self.waterDamageBonus = param49
        self.airDamageBonus = param50
        self.fireDamageBonus = param51
        self.dodgePALostProbability = param52
        self.dodgePMLostProbability = param53
        self.neutralElementResistPercent = param54
        self.earthElementResistPercent = param55
        self.waterElementResistPercent = param56
        self.airElementResistPercent = param57
        self.fireElementResistPercent = param58
        self.neutralElementReduction = param59
        self.earthElementReduction = param60
        self.waterElementReduction = param61
        self.airElementReduction = param62
        self.fireElementReduction = param63
        self.pushDamageReduction = param64
        self.criticalDamageReduction = param65
        self.pvpNeutralElementResistPercent = param66
        self.pvpEarthElementResistPercent = param67
        self.pvpWaterElementResistPercent = param68
        self.pvpAirElementResistPercent = param69
        self.pvpFireElementResistPercent = param70
        self.pvpNeutralElementReduction = param71
        self.pvpEarthElementReduction = param72
        self.pvpWaterElementReduction = param73
        self.pvpAirElementReduction = param74
        self.pvpFireElementReduction = param75
        self.meleeDamageDonePercent = param76
        self.meleeDamageReceivedPercent = param77
        self.rangedDamageDonePercent = param78
        self.rangedDamageReceivedPercent = param79
        self.weaponDamageDonePercent = param80
        self.weaponDamageReceivedPercent = param81
        self.spellDamageDonePercent = param82
        self.spellDamageReceivedPercent = param83
        self.spellModifications = param84
        self.probationTime = param85
        return self

    def reset(self):
        self.experience = 0
        self.experienceLevelFloor = 0
        self.experienceNextLevelFloor = 0
        self.experienceBonusLimit = 0
        self.kamas = 0
        self.statsPoints = 0
        self.additionnalPoints = 0
        self.spellsPoints = 0
        self.alignmentInfos = ActorExtendedAlignmentInformations()
        self.maxLifePoints = 0
        self.energyPoints = 0
        self.maxEnergyPoints = 0
        self.actionPointsCurrent = 0
        self.movementPointsCurrent = 0
        self.initiative = CharacterBaseCharacteristic()
        self.criticalMiss = CharacterBaseCharacteristic()
        self.probationTime = 0

    def serialize(self, param1):
        self.serializeAs_CharacterCharacteristicsInformations(param1)

    def serializeAs_CharacterCharacteristicsInformations(self, param1):
        if self.experience < 0 or self.experience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element experience.")
        param1.write_var_long(self.experience)
        if self.experienceLevelFloor < 0 or self.experienceLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceLevelFloor) + ") on element experienceLevelFloor.")
        param1.write_var_long(self.experienceLevelFloor)
        if self.experienceNextLevelFloor < 0 or self.experienceNextLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceNextLevelFloor) + ") on element experienceNextLevelFloor.")
        param1.write_var_long(self.experienceNextLevelFloor)
        if self.experienceBonusLimit < 0 or self.experienceBonusLimit > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceBonusLimit) + ") on element experienceBonusLimit.")
        param1.write_var_long(self.experienceBonusLimit)
        if self.kamas < 0 or self.kamas > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element kamas.")
        param1.write_var_long(self.kamas)
        if self.statsPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.statsPoints) + ") on element statsPoints.")
        param1.write_var_short(self.statsPoints)
        if self.additionnalPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.additionnalPoints) + ") on element additionnalPoints.")
        param1.write_var_short(self.additionnalPoints)
        if self.spellsPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellsPoints) + ") on element spellsPoints.")
        param1.write_var_short(self.spellsPoints)
        self.alignmentInfos.serializeAs_ActorExtendedAlignmentInformations(param1)
        if self.lifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element lifePoints.")
        param1.write_var_int(self.lifePoints)
        if self.maxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element maxLifePoints.")
        param1.write_var_int(self.maxLifePoints)
        if self.energyPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.energyPoints) + ") on element energyPoints.")
        param1.write_var_short(self.energyPoints)
        if self.maxEnergyPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxEnergyPoints) + ") on element maxEnergyPoints.")
        param1.write_var_short(self.maxEnergyPoints)
        param1.write_var_short(self.actionPointsCurrent)
        param1.write_var_short(self.movementPointsCurrent)
        self.initiative.serializeAs_CharacterBaseCharacteristic(param1)
        self.prospecting.serializeAs_CharacterBaseCharacteristic(param1)
        self.actionPoints.serializeAs_CharacterBaseCharacteristic(param1)
        self.movementPoints.serializeAs_CharacterBaseCharacteristic(param1)
        self.strength.serializeAs_CharacterBaseCharacteristic(param1)
        self.vitality.serializeAs_CharacterBaseCharacteristic(param1)
        self.wisdom.serializeAs_CharacterBaseCharacteristic(param1)
        self.chance.serializeAs_CharacterBaseCharacteristic(param1)
        self.agility.serializeAs_CharacterBaseCharacteristic(param1)
        self.intelligence.serializeAs_CharacterBaseCharacteristic(param1)
        self.range.serializeAs_CharacterBaseCharacteristic(param1)
        self.summonableCreaturesBoost.serializeAs_CharacterBaseCharacteristic(param1)
        self.reflect.serializeAs_CharacterBaseCharacteristic(param1)
        self.criticalHit.serializeAs_CharacterBaseCharacteristic(param1)
        if self.criticalHitWeapon < 0:
            raise RuntimeError("Forbidden value (" + str(self.criticalHitWeapon) + ") on element criticalHitWeapon.")
        param1.write_var_short(self.criticalHitWeapon)
        self.criticalMiss.serializeAs_CharacterBaseCharacteristic(param1)
        self.healBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.allDamagesBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.weaponDamagesBonusPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.damagesBonusPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.trapBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.trapBonusPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.glyphBonusPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.runeBonusPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.permanentDamagePercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.tackleBlock.serializeAs_CharacterBaseCharacteristic(param1)
        self.tackleEvade.serializeAs_CharacterBaseCharacteristic(param1)
        self.PAAttack.serializeAs_CharacterBaseCharacteristic(param1)
        self.PMAttack.serializeAs_CharacterBaseCharacteristic(param1)
        self.pushDamageBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.criticalDamageBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.neutralDamageBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.earthDamageBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.waterDamageBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.airDamageBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.fireDamageBonus.serializeAs_CharacterBaseCharacteristic(param1)
        self.dodgePALostProbability.serializeAs_CharacterBaseCharacteristic(param1)
        self.dodgePMLostProbability.serializeAs_CharacterBaseCharacteristic(param1)
        self.neutralElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.earthElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.waterElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.airElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.fireElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.neutralElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.earthElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.waterElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.airElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.fireElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.pushDamageReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.criticalDamageReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpNeutralElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpEarthElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpWaterElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpAirElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpFireElementResistPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpNeutralElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpEarthElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpWaterElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpAirElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.pvpFireElementReduction.serializeAs_CharacterBaseCharacteristic(param1)
        self.meleeDamageDonePercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.meleeDamageReceivedPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.rangedDamageDonePercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.rangedDamageReceivedPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.weaponDamageDonePercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.weaponDamageReceivedPercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.spellDamageDonePercent.serializeAs_CharacterBaseCharacteristic(param1)
        self.spellDamageReceivedPercent.serializeAs_CharacterBaseCharacteristic(param1)
        param1.write_short(len(self.spellModifications))
        _loc2_ = 0
        while _loc2_ < len(self.spellModifications):
            as_parent(self.spellModifications[_loc2_], CharacterSpellModification).serializeAs_CharacterSpellModification(param1)
            _loc2_ += 1
        if self.probationTime < 0:
            raise RuntimeError("Forbidden value (" + str(self.probationTime) + ") on element probationTime.")
        param1.write_int(self.probationTime)

    def deserialize(self, param1):
        self.deserializeAs_CharacterCharacteristicsInformations(param1)

    def deserializeAs_CharacterCharacteristicsInformations(self, param1):
        _loc4_ = None
        self._experienceFunc(param1)
        self._experienceLevelFloorFunc(param1)
        self._experienceNextLevelFloorFunc(param1)
        self._experienceBonusLimitFunc(param1)
        self._kamasFunc(param1)
        self._statsPointsFunc(param1)
        self._additionnalPointsFunc(param1)
        self._spellsPointsFunc(param1)
        self.alignmentInfos = ActorExtendedAlignmentInformations()
        self.alignmentInfos.deserialize(param1)
        self._lifePointsFunc(param1)
        self._maxLifePointsFunc(param1)
        self._energyPointsFunc(param1)
        self._maxEnergyPointsFunc(param1)
        self._actionPointsCurrentFunc(param1)
        self._movementPointsCurrentFunc(param1)
        self.initiative = CharacterBaseCharacteristic()
        self.initiative.deserialize(param1)
        self.prospecting = CharacterBaseCharacteristic()
        self.prospecting.deserialize(param1)
        self.actionPoints = CharacterBaseCharacteristic()
        self.actionPoints.deserialize(param1)
        self.movementPoints = CharacterBaseCharacteristic()
        self.movementPoints.deserialize(param1)
        self.strength = CharacterBaseCharacteristic()
        self.strength.deserialize(param1)
        self.vitality = CharacterBaseCharacteristic()
        self.vitality.deserialize(param1)
        self.wisdom = CharacterBaseCharacteristic()
        self.wisdom.deserialize(param1)
        self.chance = CharacterBaseCharacteristic()
        self.chance.deserialize(param1)
        self.agility = CharacterBaseCharacteristic()
        self.agility.deserialize(param1)
        self.intelligence = CharacterBaseCharacteristic()
        self.intelligence.deserialize(param1)
        self.range = CharacterBaseCharacteristic()
        self.range.deserialize(param1)
        self.summonableCreaturesBoost = CharacterBaseCharacteristic()
        self.summonableCreaturesBoost.deserialize(param1)
        self.reflect = CharacterBaseCharacteristic()
        self.reflect.deserialize(param1)
        self.criticalHit = CharacterBaseCharacteristic()
        self.criticalHit.deserialize(param1)
        self._criticalHitWeaponFunc(param1)
        self.criticalMiss = CharacterBaseCharacteristic()
        self.criticalMiss.deserialize(param1)
        self.healBonus = CharacterBaseCharacteristic()
        self.healBonus.deserialize(param1)
        self.allDamagesBonus = CharacterBaseCharacteristic()
        self.allDamagesBonus.deserialize(param1)
        self.weaponDamagesBonusPercent = CharacterBaseCharacteristic()
        self.weaponDamagesBonusPercent.deserialize(param1)
        self.damagesBonusPercent = CharacterBaseCharacteristic()
        self.damagesBonusPercent.deserialize(param1)
        self.trapBonus = CharacterBaseCharacteristic()
        self.trapBonus.deserialize(param1)
        self.trapBonusPercent = CharacterBaseCharacteristic()
        self.trapBonusPercent.deserialize(param1)
        self.glyphBonusPercent = CharacterBaseCharacteristic()
        self.glyphBonusPercent.deserialize(param1)
        self.runeBonusPercent = CharacterBaseCharacteristic()
        self.runeBonusPercent.deserialize(param1)
        self.permanentDamagePercent = CharacterBaseCharacteristic()
        self.permanentDamagePercent.deserialize(param1)
        self.tackleBlock = CharacterBaseCharacteristic()
        self.tackleBlock.deserialize(param1)
        self.tackleEvade = CharacterBaseCharacteristic()
        self.tackleEvade.deserialize(param1)
        self.PAAttack = CharacterBaseCharacteristic()
        self.PAAttack.deserialize(param1)
        self.PMAttack = CharacterBaseCharacteristic()
        self.PMAttack.deserialize(param1)
        self.pushDamageBonus = CharacterBaseCharacteristic()
        self.pushDamageBonus.deserialize(param1)
        self.criticalDamageBonus = CharacterBaseCharacteristic()
        self.criticalDamageBonus.deserialize(param1)
        self.neutralDamageBonus = CharacterBaseCharacteristic()
        self.neutralDamageBonus.deserialize(param1)
        self.earthDamageBonus = CharacterBaseCharacteristic()
        self.earthDamageBonus.deserialize(param1)
        self.waterDamageBonus = CharacterBaseCharacteristic()
        self.waterDamageBonus.deserialize(param1)
        self.airDamageBonus = CharacterBaseCharacteristic()
        self.airDamageBonus.deserialize(param1)
        self.fireDamageBonus = CharacterBaseCharacteristic()
        self.fireDamageBonus.deserialize(param1)
        self.dodgePALostProbability = CharacterBaseCharacteristic()
        self.dodgePALostProbability.deserialize(param1)
        self.dodgePMLostProbability = CharacterBaseCharacteristic()
        self.dodgePMLostProbability.deserialize(param1)
        self.neutralElementResistPercent = CharacterBaseCharacteristic()
        self.neutralElementResistPercent.deserialize(param1)
        self.earthElementResistPercent = CharacterBaseCharacteristic()
        self.earthElementResistPercent.deserialize(param1)
        self.waterElementResistPercent = CharacterBaseCharacteristic()
        self.waterElementResistPercent.deserialize(param1)
        self.airElementResistPercent = CharacterBaseCharacteristic()
        self.airElementResistPercent.deserialize(param1)
        self.fireElementResistPercent = CharacterBaseCharacteristic()
        self.fireElementResistPercent.deserialize(param1)
        self.neutralElementReduction = CharacterBaseCharacteristic()
        self.neutralElementReduction.deserialize(param1)
        self.earthElementReduction = CharacterBaseCharacteristic()
        self.earthElementReduction.deserialize(param1)
        self.waterElementReduction = CharacterBaseCharacteristic()
        self.waterElementReduction.deserialize(param1)
        self.airElementReduction = CharacterBaseCharacteristic()
        self.airElementReduction.deserialize(param1)
        self.fireElementReduction = CharacterBaseCharacteristic()
        self.fireElementReduction.deserialize(param1)
        self.pushDamageReduction = CharacterBaseCharacteristic()
        self.pushDamageReduction.deserialize(param1)
        self.criticalDamageReduction = CharacterBaseCharacteristic()
        self.criticalDamageReduction.deserialize(param1)
        self.pvpNeutralElementResistPercent = CharacterBaseCharacteristic()
        self.pvpNeutralElementResistPercent.deserialize(param1)
        self.pvpEarthElementResistPercent = CharacterBaseCharacteristic()
        self.pvpEarthElementResistPercent.deserialize(param1)
        self.pvpWaterElementResistPercent = CharacterBaseCharacteristic()
        self.pvpWaterElementResistPercent.deserialize(param1)
        self.pvpAirElementResistPercent = CharacterBaseCharacteristic()
        self.pvpAirElementResistPercent.deserialize(param1)
        self.pvpFireElementResistPercent = CharacterBaseCharacteristic()
        self.pvpFireElementResistPercent.deserialize(param1)
        self.pvpNeutralElementReduction = CharacterBaseCharacteristic()
        self.pvpNeutralElementReduction.deserialize(param1)
        self.pvpEarthElementReduction = CharacterBaseCharacteristic()
        self.pvpEarthElementReduction.deserialize(param1)
        self.pvpWaterElementReduction = CharacterBaseCharacteristic()
        self.pvpWaterElementReduction.deserialize(param1)
        self.pvpAirElementReduction = CharacterBaseCharacteristic()
        self.pvpAirElementReduction.deserialize(param1)
        self.pvpFireElementReduction = CharacterBaseCharacteristic()
        self.pvpFireElementReduction.deserialize(param1)
        self.meleeDamageDonePercent = CharacterBaseCharacteristic()
        self.meleeDamageDonePercent.deserialize(param1)
        self.meleeDamageReceivedPercent = CharacterBaseCharacteristic()
        self.meleeDamageReceivedPercent.deserialize(param1)
        self.rangedDamageDonePercent = CharacterBaseCharacteristic()
        self.rangedDamageDonePercent.deserialize(param1)
        self.rangedDamageReceivedPercent = CharacterBaseCharacteristic()
        self.rangedDamageReceivedPercent.deserialize(param1)
        self.weaponDamageDonePercent = CharacterBaseCharacteristic()
        self.weaponDamageDonePercent.deserialize(param1)
        self.weaponDamageReceivedPercent = CharacterBaseCharacteristic()
        self.weaponDamageReceivedPercent.deserialize(param1)
        self.spellDamageDonePercent = CharacterBaseCharacteristic()
        self.spellDamageDonePercent.deserialize(param1)
        self.spellDamageReceivedPercent = CharacterBaseCharacteristic()
        self.spellDamageReceivedPercent.deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = CharacterSpellModification()
            _loc4_.deserialize(param1)
            self.spellModifications.append(_loc4_)
            _loc3_ += 1
        self._probationTimeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterCharacteristicsInformations(param1)

    def deserializeAsyncAs_CharacterCharacteristicsInformations(self, param1):
        param1.add_child(self._experienceFunc)
        param1.add_child(self._experienceLevelFloorFunc)
        param1.add_child(self._experienceNextLevelFloorFunc)
        param1.add_child(self._experienceBonusLimitFunc)
        param1.add_child(self._kamasFunc)
        param1.add_child(self._statsPointsFunc)
        param1.add_child(self._additionnalPointsFunc)
        param1.add_child(self._spellsPointsFunc)
        self._alignmentInfostree = param1.add_child(self._alignmentInfostreeFunc)
        param1.add_child(self._lifePointsFunc)
        param1.add_child(self._maxLifePointsFunc)
        param1.add_child(self._energyPointsFunc)
        param1.add_child(self._maxEnergyPointsFunc)
        param1.add_child(self._actionPointsCurrentFunc)
        param1.add_child(self._movementPointsCurrentFunc)
        self._initiativetree = param1.add_child(self._initiativetreeFunc)
        self._prospectingtree = param1.add_child(self._prospectingtreeFunc)
        self._actionPointstree = param1.add_child(self._actionPointstreeFunc)
        self._movementPointstree = param1.add_child(self._movementPointstreeFunc)
        self._strengthtree = param1.add_child(self._strengthtreeFunc)
        self._vitalitytree = param1.add_child(self._vitalitytreeFunc)
        self._wisdomtree = param1.add_child(self._wisdomtreeFunc)
        self._chancetree = param1.add_child(self._chancetreeFunc)
        self._agilitytree = param1.add_child(self._agilitytreeFunc)
        self._intelligencetree = param1.add_child(self._intelligencetreeFunc)
        self._rangetree = param1.add_child(self._rangetreeFunc)
        self._summonableCreaturesBoosttree = param1.add_child(self._summonableCreaturesBoosttreeFunc)
        self._reflecttree = param1.add_child(self._reflecttreeFunc)
        self._criticalHittree = param1.add_child(self._criticalHittreeFunc)
        param1.add_child(self._criticalHitWeaponFunc)
        self._criticalMisstree = param1.add_child(self._criticalMisstreeFunc)
        self._healBonustree = param1.add_child(self._healBonustreeFunc)
        self._allDamagesBonustree = param1.add_child(self._allDamagesBonustreeFunc)
        self._weaponDamagesBonusPercenttree = param1.add_child(self._weaponDamagesBonusPercenttreeFunc)
        self._damagesBonusPercenttree = param1.add_child(self._damagesBonusPercenttreeFunc)
        self._trapBonustree = param1.add_child(self._trapBonustreeFunc)
        self._trapBonusPercenttree = param1.add_child(self._trapBonusPercenttreeFunc)
        self._glyphBonusPercenttree = param1.add_child(self._glyphBonusPercenttreeFunc)
        self._runeBonusPercenttree = param1.add_child(self._runeBonusPercenttreeFunc)
        self._permanentDamagePercenttree = param1.add_child(self._permanentDamagePercenttreeFunc)
        self._tackleBlocktree = param1.add_child(self._tackleBlocktreeFunc)
        self._tackleEvadetree = param1.add_child(self._tackleEvadetreeFunc)
        self._PAAttacktree = param1.add_child(self._PAAttacktreeFunc)
        self._PMAttacktree = param1.add_child(self._PMAttacktreeFunc)
        self._pushDamageBonustree = param1.add_child(self._pushDamageBonustreeFunc)
        self._criticalDamageBonustree = param1.add_child(self._criticalDamageBonustreeFunc)
        self._neutralDamageBonustree = param1.add_child(self._neutralDamageBonustreeFunc)
        self._earthDamageBonustree = param1.add_child(self._earthDamageBonustreeFunc)
        self._waterDamageBonustree = param1.add_child(self._waterDamageBonustreeFunc)
        self._airDamageBonustree = param1.add_child(self._airDamageBonustreeFunc)
        self._fireDamageBonustree = param1.add_child(self._fireDamageBonustreeFunc)
        self._dodgePALostProbabilitytree = param1.add_child(self._dodgePALostProbabilitytreeFunc)
        self._dodgePMLostProbabilitytree = param1.add_child(self._dodgePMLostProbabilitytreeFunc)
        self._neutralElementResistPercenttree = param1.add_child(self._neutralElementResistPercenttreeFunc)
        self._earthElementResistPercenttree = param1.add_child(self._earthElementResistPercenttreeFunc)
        self._waterElementResistPercenttree = param1.add_child(self._waterElementResistPercenttreeFunc)
        self._airElementResistPercenttree = param1.add_child(self._airElementResistPercenttreeFunc)
        self._fireElementResistPercenttree = param1.add_child(self._fireElementResistPercenttreeFunc)
        self._neutralElementReductiontree = param1.add_child(self._neutralElementReductiontreeFunc)
        self._earthElementReductiontree = param1.add_child(self._earthElementReductiontreeFunc)
        self._waterElementReductiontree = param1.add_child(self._waterElementReductiontreeFunc)
        self._airElementReductiontree = param1.add_child(self._airElementReductiontreeFunc)
        self._fireElementReductiontree = param1.add_child(self._fireElementReductiontreeFunc)
        self._pushDamageReductiontree = param1.add_child(self._pushDamageReductiontreeFunc)
        self._criticalDamageReductiontree = param1.add_child(self._criticalDamageReductiontreeFunc)
        self._pvpNeutralElementResistPercenttree = param1.add_child(self._pvpNeutralElementResistPercenttreeFunc)
        self._pvpEarthElementResistPercenttree = param1.add_child(self._pvpEarthElementResistPercenttreeFunc)
        self._pvpWaterElementResistPercenttree = param1.add_child(self._pvpWaterElementResistPercenttreeFunc)
        self._pvpAirElementResistPercenttree = param1.add_child(self._pvpAirElementResistPercenttreeFunc)
        self._pvpFireElementResistPercenttree = param1.add_child(self._pvpFireElementResistPercenttreeFunc)
        self._pvpNeutralElementReductiontree = param1.add_child(self._pvpNeutralElementReductiontreeFunc)
        self._pvpEarthElementReductiontree = param1.add_child(self._pvpEarthElementReductiontreeFunc)
        self._pvpWaterElementReductiontree = param1.add_child(self._pvpWaterElementReductiontreeFunc)
        self._pvpAirElementReductiontree = param1.add_child(self._pvpAirElementReductiontreeFunc)
        self._pvpFireElementReductiontree = param1.add_child(self._pvpFireElementReductiontreeFunc)
        self._meleeDamageDonePercenttree = param1.add_child(self._meleeDamageDonePercenttreeFunc)
        self._meleeDamageReceivedPercenttree = param1.add_child(self._meleeDamageReceivedPercenttreeFunc)
        self._rangedDamageDonePercenttree = param1.add_child(self._rangedDamageDonePercenttreeFunc)
        self._rangedDamageReceivedPercenttree = param1.add_child(self._rangedDamageReceivedPercenttreeFunc)
        self._weaponDamageDonePercenttree = param1.add_child(self._weaponDamageDonePercenttreeFunc)
        self._weaponDamageReceivedPercenttree = param1.add_child(self._weaponDamageReceivedPercenttreeFunc)
        self._spellDamageDonePercenttree = param1.add_child(self._spellDamageDonePercenttreeFunc)
        self._spellDamageReceivedPercenttree = param1.add_child(self._spellDamageReceivedPercenttreeFunc)
        self._spellModificationstree = param1.add_child(self._spellModificationstreeFunc)
        param1.add_child(self._probationTimeFunc)

    def _experienceFunc(self, param1):
        self.experience = param1.read_var_uh_long()
        if self.experience < 0 or self.experience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element of CharacterCharacteristicsInformations.experience.")

    def _experienceLevelFloorFunc(self, param1):
        self.experienceLevelFloor = param1.read_var_uh_long()
        if self.experienceLevelFloor < 0 or self.experienceLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceLevelFloor) + ") on element of CharacterCharacteristicsInformations.experienceLevelFloor.")

    def _experienceNextLevelFloorFunc(self, param1):
        self.experienceNextLevelFloor = param1.read_var_uh_long()
        if self.experienceNextLevelFloor < 0 or self.experienceNextLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceNextLevelFloor) + ") on element of CharacterCharacteristicsInformations.experienceNextLevelFloor.")

    def _experienceBonusLimitFunc(self, param1):
        self.experienceBonusLimit = param1.read_var_uh_long()
        if self.experienceBonusLimit < 0 or self.experienceBonusLimit > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceBonusLimit) + ") on element of CharacterCharacteristicsInformations.experienceBonusLimit.")

    def _kamasFunc(self, param1):
        self.kamas = param1.read_var_uh_long()
        if self.kamas < 0 or self.kamas > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element of CharacterCharacteristicsInformations.kamas.")

    def _statsPointsFunc(self, param1):
        self.statsPoints = param1.read_var_uh_short()
        if self.statsPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.statsPoints) + ") on element of CharacterCharacteristicsInformations.statsPoints.")

    def _additionnalPointsFunc(self, param1):
        self.additionnalPoints = param1.read_var_uh_short()
        if self.additionnalPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.additionnalPoints) + ") on element of CharacterCharacteristicsInformations.additionnalPoints.")

    def _spellsPointsFunc(self, param1):
        self.spellsPoints = param1.read_var_uh_short()
        if self.spellsPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellsPoints) + ") on element of CharacterCharacteristicsInformations.spellsPoints.")

    def _alignmentInfostreeFunc(self, param1):
        self.alignmentInfos = ActorExtendedAlignmentInformations()
        self.alignmentInfos.deserializeAsync(self._alignmentInfostree)

    def _lifePointsFunc(self, param1):
        self.lifePoints = param1.read_var_uh_int()
        if self.lifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element of CharacterCharacteristicsInformations.lifePoints.")

    def _maxLifePointsFunc(self, param1):
        self.maxLifePoints = param1.read_var_uh_int()
        if self.maxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element of CharacterCharacteristicsInformations.maxLifePoints.")

    def _energyPointsFunc(self, param1):
        self.energyPoints = param1.read_var_uh_short()
        if self.energyPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.energyPoints) + ") on element of CharacterCharacteristicsInformations.energyPoints.")

    def _maxEnergyPointsFunc(self, param1):
        self.maxEnergyPoints = param1.read_var_uh_short()
        if self.maxEnergyPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxEnergyPoints) + ") on element of CharacterCharacteristicsInformations.maxEnergyPoints.")

    def _actionPointsCurrentFunc(self, param1):
        self.actionPointsCurrent = param1.read_var_short()

    def _movementPointsCurrentFunc(self, param1):
        self.movementPointsCurrent = param1.read_var_short()

    def _initiativetreeFunc(self, param1):
        self.initiative = CharacterBaseCharacteristic()
        self.initiative.deserializeAsync(self._initiativetree)

    def _prospectingtreeFunc(self, param1):
        self.prospecting = CharacterBaseCharacteristic()
        self.prospecting.deserializeAsync(self._prospectingtree)

    def _actionPointstreeFunc(self, param1):
        self.actionPoints = CharacterBaseCharacteristic()
        self.actionPoints.deserializeAsync(self._actionPointstree)

    def _movementPointstreeFunc(self, param1):
        self.movementPoints = CharacterBaseCharacteristic()
        self.movementPoints.deserializeAsync(self._movementPointstree)

    def _strengthtreeFunc(self, param1):
        self.strength = CharacterBaseCharacteristic()
        self.strength.deserializeAsync(self._strengthtree)

    def _vitalitytreeFunc(self, param1):
        self.vitality = CharacterBaseCharacteristic()
        self.vitality.deserializeAsync(self._vitalitytree)

    def _wisdomtreeFunc(self, param1):
        self.wisdom = CharacterBaseCharacteristic()
        self.wisdom.deserializeAsync(self._wisdomtree)

    def _chancetreeFunc(self, param1):
        self.chance = CharacterBaseCharacteristic()
        self.chance.deserializeAsync(self._chancetree)

    def _agilitytreeFunc(self, param1):
        self.agility = CharacterBaseCharacteristic()
        self.agility.deserializeAsync(self._agilitytree)

    def _intelligencetreeFunc(self, param1):
        self.intelligence = CharacterBaseCharacteristic()
        self.intelligence.deserializeAsync(self._intelligencetree)

    def _rangetreeFunc(self, param1):
        self.range = CharacterBaseCharacteristic()
        self.range.deserializeAsync(self._rangetree)

    def _summonableCreaturesBoosttreeFunc(self, param1):
        self.summonableCreaturesBoost = CharacterBaseCharacteristic()
        self.summonableCreaturesBoost.deserializeAsync(self._summonableCreaturesBoosttree)

    def _reflecttreeFunc(self, param1):
        self.reflect = CharacterBaseCharacteristic()
        self.reflect.deserializeAsync(self._reflecttree)

    def _criticalHittreeFunc(self, param1):
        self.criticalHit = CharacterBaseCharacteristic()
        self.criticalHit.deserializeAsync(self._criticalHittree)

    def _criticalHitWeaponFunc(self, param1):
        self.criticalHitWeapon = param1.read_var_uh_short()
        if self.criticalHitWeapon < 0:
            raise RuntimeError("Forbidden value (" + str(self.criticalHitWeapon) + ") on element of CharacterCharacteristicsInformations.criticalHitWeapon.")

    def _criticalMisstreeFunc(self, param1):
        self.criticalMiss = CharacterBaseCharacteristic()
        self.criticalMiss.deserializeAsync(self._criticalMisstree)

    def _healBonustreeFunc(self, param1):
        self.healBonus = CharacterBaseCharacteristic()
        self.healBonus.deserializeAsync(self._healBonustree)

    def _allDamagesBonustreeFunc(self, param1):
        self.allDamagesBonus = CharacterBaseCharacteristic()
        self.allDamagesBonus.deserializeAsync(self._allDamagesBonustree)

    def _weaponDamagesBonusPercenttreeFunc(self, param1):
        self.weaponDamagesBonusPercent = CharacterBaseCharacteristic()
        self.weaponDamagesBonusPercent.deserializeAsync(self._weaponDamagesBonusPercenttree)

    def _damagesBonusPercenttreeFunc(self, param1):
        self.damagesBonusPercent = CharacterBaseCharacteristic()
        self.damagesBonusPercent.deserializeAsync(self._damagesBonusPercenttree)

    def _trapBonustreeFunc(self, param1):
        self.trapBonus = CharacterBaseCharacteristic()
        self.trapBonus.deserializeAsync(self._trapBonustree)

    def _trapBonusPercenttreeFunc(self, param1):
        self.trapBonusPercent = CharacterBaseCharacteristic()
        self.trapBonusPercent.deserializeAsync(self._trapBonusPercenttree)

    def _glyphBonusPercenttreeFunc(self, param1):
        self.glyphBonusPercent = CharacterBaseCharacteristic()
        self.glyphBonusPercent.deserializeAsync(self._glyphBonusPercenttree)

    def _runeBonusPercenttreeFunc(self, param1):
        self.runeBonusPercent = CharacterBaseCharacteristic()
        self.runeBonusPercent.deserializeAsync(self._runeBonusPercenttree)

    def _permanentDamagePercenttreeFunc(self, param1):
        self.permanentDamagePercent = CharacterBaseCharacteristic()
        self.permanentDamagePercent.deserializeAsync(self._permanentDamagePercenttree)

    def _tackleBlocktreeFunc(self, param1):
        self.tackleBlock = CharacterBaseCharacteristic()
        self.tackleBlock.deserializeAsync(self._tackleBlocktree)

    def _tackleEvadetreeFunc(self, param1):
        self.tackleEvade = CharacterBaseCharacteristic()
        self.tackleEvade.deserializeAsync(self._tackleEvadetree)

    def _PAAttacktreeFunc(self, param1):
        self.PAAttack = CharacterBaseCharacteristic()
        self.PAAttack.deserializeAsync(self._PAAttacktree)

    def _PMAttacktreeFunc(self, param1):
        self.PMAttack = CharacterBaseCharacteristic()
        self.PMAttack.deserializeAsync(self._PMAttacktree)

    def _pushDamageBonustreeFunc(self, param1):
        self.pushDamageBonus = CharacterBaseCharacteristic()
        self.pushDamageBonus.deserializeAsync(self._pushDamageBonustree)

    def _criticalDamageBonustreeFunc(self, param1):
        self.criticalDamageBonus = CharacterBaseCharacteristic()
        self.criticalDamageBonus.deserializeAsync(self._criticalDamageBonustree)

    def _neutralDamageBonustreeFunc(self, param1):
        self.neutralDamageBonus = CharacterBaseCharacteristic()
        self.neutralDamageBonus.deserializeAsync(self._neutralDamageBonustree)

    def _earthDamageBonustreeFunc(self, param1):
        self.earthDamageBonus = CharacterBaseCharacteristic()
        self.earthDamageBonus.deserializeAsync(self._earthDamageBonustree)

    def _waterDamageBonustreeFunc(self, param1):
        self.waterDamageBonus = CharacterBaseCharacteristic()
        self.waterDamageBonus.deserializeAsync(self._waterDamageBonustree)

    def _airDamageBonustreeFunc(self, param1):
        self.airDamageBonus = CharacterBaseCharacteristic()
        self.airDamageBonus.deserializeAsync(self._airDamageBonustree)

    def _fireDamageBonustreeFunc(self, param1):
        self.fireDamageBonus = CharacterBaseCharacteristic()
        self.fireDamageBonus.deserializeAsync(self._fireDamageBonustree)

    def _dodgePALostProbabilitytreeFunc(self, param1):
        self.dodgePALostProbability = CharacterBaseCharacteristic()
        self.dodgePALostProbability.deserializeAsync(self._dodgePALostProbabilitytree)

    def _dodgePMLostProbabilitytreeFunc(self, param1):
        self.dodgePMLostProbability = CharacterBaseCharacteristic()
        self.dodgePMLostProbability.deserializeAsync(self._dodgePMLostProbabilitytree)

    def _neutralElementResistPercenttreeFunc(self, param1):
        self.neutralElementResistPercent = CharacterBaseCharacteristic()
        self.neutralElementResistPercent.deserializeAsync(self._neutralElementResistPercenttree)

    def _earthElementResistPercenttreeFunc(self, param1):
        self.earthElementResistPercent = CharacterBaseCharacteristic()
        self.earthElementResistPercent.deserializeAsync(self._earthElementResistPercenttree)

    def _waterElementResistPercenttreeFunc(self, param1):
        self.waterElementResistPercent = CharacterBaseCharacteristic()
        self.waterElementResistPercent.deserializeAsync(self._waterElementResistPercenttree)

    def _airElementResistPercenttreeFunc(self, param1):
        self.airElementResistPercent = CharacterBaseCharacteristic()
        self.airElementResistPercent.deserializeAsync(self._airElementResistPercenttree)

    def _fireElementResistPercenttreeFunc(self, param1):
        self.fireElementResistPercent = CharacterBaseCharacteristic()
        self.fireElementResistPercent.deserializeAsync(self._fireElementResistPercenttree)

    def _neutralElementReductiontreeFunc(self, param1):
        self.neutralElementReduction = CharacterBaseCharacteristic()
        self.neutralElementReduction.deserializeAsync(self._neutralElementReductiontree)

    def _earthElementReductiontreeFunc(self, param1):
        self.earthElementReduction = CharacterBaseCharacteristic()
        self.earthElementReduction.deserializeAsync(self._earthElementReductiontree)

    def _waterElementReductiontreeFunc(self, param1):
        self.waterElementReduction = CharacterBaseCharacteristic()
        self.waterElementReduction.deserializeAsync(self._waterElementReductiontree)

    def _airElementReductiontreeFunc(self, param1):
        self.airElementReduction = CharacterBaseCharacteristic()
        self.airElementReduction.deserializeAsync(self._airElementReductiontree)

    def _fireElementReductiontreeFunc(self, param1):
        self.fireElementReduction = CharacterBaseCharacteristic()
        self.fireElementReduction.deserializeAsync(self._fireElementReductiontree)

    def _pushDamageReductiontreeFunc(self, param1):
        self.pushDamageReduction = CharacterBaseCharacteristic()
        self.pushDamageReduction.deserializeAsync(self._pushDamageReductiontree)

    def _criticalDamageReductiontreeFunc(self, param1):
        self.criticalDamageReduction = CharacterBaseCharacteristic()
        self.criticalDamageReduction.deserializeAsync(self._criticalDamageReductiontree)

    def _pvpNeutralElementResistPercenttreeFunc(self, param1):
        self.pvpNeutralElementResistPercent = CharacterBaseCharacteristic()
        self.pvpNeutralElementResistPercent.deserializeAsync(self._pvpNeutralElementResistPercenttree)

    def _pvpEarthElementResistPercenttreeFunc(self, param1):
        self.pvpEarthElementResistPercent = CharacterBaseCharacteristic()
        self.pvpEarthElementResistPercent.deserializeAsync(self._pvpEarthElementResistPercenttree)

    def _pvpWaterElementResistPercenttreeFunc(self, param1):
        self.pvpWaterElementResistPercent = CharacterBaseCharacteristic()
        self.pvpWaterElementResistPercent.deserializeAsync(self._pvpWaterElementResistPercenttree)

    def _pvpAirElementResistPercenttreeFunc(self, param1):
        self.pvpAirElementResistPercent = CharacterBaseCharacteristic()
        self.pvpAirElementResistPercent.deserializeAsync(self._pvpAirElementResistPercenttree)

    def _pvpFireElementResistPercenttreeFunc(self, param1):
        self.pvpFireElementResistPercent = CharacterBaseCharacteristic()
        self.pvpFireElementResistPercent.deserializeAsync(self._pvpFireElementResistPercenttree)

    def _pvpNeutralElementReductiontreeFunc(self, param1):
        self.pvpNeutralElementReduction = CharacterBaseCharacteristic()
        self.pvpNeutralElementReduction.deserializeAsync(self._pvpNeutralElementReductiontree)

    def _pvpEarthElementReductiontreeFunc(self, param1):
        self.pvpEarthElementReduction = CharacterBaseCharacteristic()
        self.pvpEarthElementReduction.deserializeAsync(self._pvpEarthElementReductiontree)

    def _pvpWaterElementReductiontreeFunc(self, param1):
        self.pvpWaterElementReduction = CharacterBaseCharacteristic()
        self.pvpWaterElementReduction.deserializeAsync(self._pvpWaterElementReductiontree)

    def _pvpAirElementReductiontreeFunc(self, param1):
        self.pvpAirElementReduction = CharacterBaseCharacteristic()
        self.pvpAirElementReduction.deserializeAsync(self._pvpAirElementReductiontree)

    def _pvpFireElementReductiontreeFunc(self, param1):
        self.pvpFireElementReduction = CharacterBaseCharacteristic()
        self.pvpFireElementReduction.deserializeAsync(self._pvpFireElementReductiontree)

    def _meleeDamageDonePercenttreeFunc(self, param1):
        self.meleeDamageDonePercent = CharacterBaseCharacteristic()
        self.meleeDamageDonePercent.deserializeAsync(self._meleeDamageDonePercenttree)

    def _meleeDamageReceivedPercenttreeFunc(self, param1):
        self.meleeDamageReceivedPercent = CharacterBaseCharacteristic()
        self.meleeDamageReceivedPercent.deserializeAsync(self._meleeDamageReceivedPercenttree)

    def _rangedDamageDonePercenttreeFunc(self, param1):
        self.rangedDamageDonePercent = CharacterBaseCharacteristic()
        self.rangedDamageDonePercent.deserializeAsync(self._rangedDamageDonePercenttree)

    def _rangedDamageReceivedPercenttreeFunc(self, param1):
        self.rangedDamageReceivedPercent = CharacterBaseCharacteristic()
        self.rangedDamageReceivedPercent.deserializeAsync(self._rangedDamageReceivedPercenttree)

    def _weaponDamageDonePercenttreeFunc(self, param1):
        self.weaponDamageDonePercent = CharacterBaseCharacteristic()
        self.weaponDamageDonePercent.deserializeAsync(self._weaponDamageDonePercenttree)

    def _weaponDamageReceivedPercenttreeFunc(self, param1):
        self.weaponDamageReceivedPercent = CharacterBaseCharacteristic()
        self.weaponDamageReceivedPercent.deserializeAsync(self._weaponDamageReceivedPercenttree)

    def _spellDamageDonePercenttreeFunc(self, param1):
        self.spellDamageDonePercent = CharacterBaseCharacteristic()
        self.spellDamageDonePercent.deserializeAsync(self._spellDamageDonePercenttree)

    def _spellDamageReceivedPercenttreeFunc(self, param1):
        self.spellDamageReceivedPercent = CharacterBaseCharacteristic()
        self.spellDamageReceivedPercent.deserializeAsync(self._spellDamageReceivedPercenttree)

    def _spellModificationstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._spellModificationstree.add_child(self._spellModificationsFunc)
            _loc3_ += 1

    def _spellModificationsFunc(self, param1):
        _loc2_ = CharacterSpellModification()
        _loc2_.deserialize(param1)
        self.spellModifications.append(_loc2_)

    def _probationTimeFunc(self, param1):
        self.probationTime = param1.read_int()
        if self.probationTime < 0:
            raise RuntimeError("Forbidden value (" + str(self.probationTime) + ") on element of CharacterCharacteristicsInformations.probationTime.")


class CharacterSpellModification():
    protocolId = 215

    def __init__(self):
        super().__init__()
        self.modificationType = 0
        self.spellId = 0
        self.value = CharacterBaseCharacteristic()
        self._valuetree = FuncTree()

    def getTypeId(self):
        return 215

    def initCharacterSpellModification(self, param1=0, param2=0, param3=None):
        self.modificationType = param1
        self.spellId = param2
        self.value = param3
        return self

    def reset(self):
        self.modificationType = 0
        self.spellId = 0
        self.value = CharacterBaseCharacteristic()

    def serialize(self, param1):
        self.serializeAs_CharacterSpellModification(param1)

    def serializeAs_CharacterSpellModification(self, param1):
        param1.write_byte(self.modificationType)
        if self.spellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element spellId.")
        param1.write_var_short(self.spellId)
        self.value.serializeAs_CharacterBaseCharacteristic(param1)

    def deserialize(self, param1):
        self.deserializeAs_CharacterSpellModification(param1)

    def deserializeAs_CharacterSpellModification(self, param1):
        self._modificationTypeFunc(param1)
        self._spellIdFunc(param1)
        self.value = CharacterBaseCharacteristic()
        self.value.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterSpellModification(param1)

    def deserializeAsyncAs_CharacterSpellModification(self, param1):
        param1.add_child(self._modificationTypeFunc)
        param1.add_child(self._spellIdFunc)
        self._valuetree = param1.add_child(self._valuetreeFunc)

    def _modificationTypeFunc(self, param1):
        self.modificationType = param1.read_byte()
        if self.modificationType < 0:
            raise RuntimeError("Forbidden value (" + str(self.modificationType) + ") on element of CharacterSpellModification.modificationType.")

    def _spellIdFunc(self, param1):
        self.spellId = param1.read_var_uh_short()
        if self.spellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of CharacterSpellModification.spellId.")

    def _valuetreeFunc(self, param1):
        self.value = CharacterBaseCharacteristic()
        self.value.deserializeAsync(self._valuetree)


class RemodelingInformation():
    protocolId = 480

    def __init__(self):
        super().__init__()
        self.name = ""
        self.breed = 0
        self.sex = False
        self.cosmeticId = 0
        self.colors = []
        self._colorstree = FuncTree()

    def getTypeId(self):
        return 480

    def initRemodelingInformation(self, param1="", param2=0, param3=False, param4=0, param5=[]):
        self.name = param1
        self.breed = param2
        self.sex = param3
        self.cosmeticId = param4
        self.colors = param5
        return self

    def reset(self):
        self.name = ""
        self.breed = 0
        self.sex = False
        self.cosmeticId = 0
        self.colors = []

    def serialize(self, param1):
        self.serializeAs_RemodelingInformation(param1)

    def serializeAs_RemodelingInformation(self, param1):
        param1.write_utf(self.name)
        param1.write_byte(self.breed)
        param1.write_boolean(self.sex)
        if self.cosmeticId < 0:
            raise RuntimeError("Forbidden value (" + str(self.cosmeticId) + ") on element cosmeticId.")
        param1.write_var_short(self.cosmeticId)
        param1.write_short(len(self.colors))
        _loc2_ = 0
        while _loc2_ < len(self.colors):
            param1.write_int(self.colors[_loc2_])
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_RemodelingInformation(param1)

    def deserializeAs_RemodelingInformation(self, param1):
        _loc4_ = 0
        self._nameFunc(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)
        self._cosmeticIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_int()
            self.colors.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_RemodelingInformation(param1)

    def deserializeAsyncAs_RemodelingInformation(self, param1):
        param1.add_child(self._nameFunc)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)
        param1.add_child(self._cosmeticIdFunc)
        self._colorstree = param1.add_child(self._colorstreeFunc)

    def _nameFunc(self, param1):
        self.name = param1.read_utf()

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()

    def _cosmeticIdFunc(self, param1):
        self.cosmeticId = param1.read_var_uh_short()
        if self.cosmeticId < 0:
            raise RuntimeError("Forbidden value (" + str(self.cosmeticId) + ") on element of RemodelingInformation.cosmeticId.")

    def _colorstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._colorstree.add_child(self._colorsFunc)
            _loc3_ += 1

    def _colorsFunc(self, param1):
        _loc2_ = param1.read_int()
        self.colors.append(_loc2_)


class ActorRestrictionsInformations():
    protocolId = 204

    def __init__(self):
        super().__init__()
        self.cantBeAggressed = False
        self.cantBeChallenged = False
        self.cantTrade = False
        self.cantBeAttackedByMutant = False
        self.cantRun = False
        self.forceSlowWalk = False
        self.cantMinimize = False
        self.cantMove = False
        self.cantAggress = False
        self.cantChallenge = False
        self.cantExchange = False
        self.cantAttack = False
        self.cantChat = False
        self.cantBeMerchant = False
        self.cantUseObject = False
        self.cantUseTaxCollector = False
        self.cantUseInteractive = False
        self.cantSpeakToNPC = False
        self.cantChangeZone = False
        self.cantAttackMonster = False
        self.cantWalk8Directions = False

    def getTypeId(self):
        return 204

    def initActorRestrictionsInformations(self, param1=False, param2=False, param3=False, param4=False, param5=False, param6=False, param7=False, param8=False, param9=False, param10=False, param11=False, param12=False, param13=False, param14=False, param15=False, param16=False, param17=False, param18=False, param19=False, param20=False, param21=False):
        self.cantBeAggressed = param1
        self.cantBeChallenged = param2
        self.cantTrade = param3
        self.cantBeAttackedByMutant = param4
        self.cantRun = param5
        self.forceSlowWalk = param6
        self.cantMinimize = param7
        self.cantMove = param8
        self.cantAggress = param9
        self.cantChallenge = param10
        self.cantExchange = param11
        self.cantAttack = param12
        self.cantChat = param13
        self.cantBeMerchant = param14
        self.cantUseObject = param15
        self.cantUseTaxCollector = param16
        self.cantUseInteractive = param17
        self.cantSpeakToNPC = param18
        self.cantChangeZone = param19
        self.cantAttackMonster = param20
        self.cantWalk8Directions = param21
        return self

    def reset(self):
        self.cantBeAggressed = False
        self.cantBeChallenged = False
        self.cantTrade = False
        self.cantBeAttackedByMutant = False
        self.cantRun = False
        self.forceSlowWalk = False
        self.cantMinimize = False
        self.cantMove = False
        self.cantAggress = False
        self.cantChallenge = False
        self.cantExchange = False
        self.cantAttack = False
        self.cantChat = False
        self.cantBeMerchant = False
        self.cantUseObject = False
        self.cantUseTaxCollector = False
        self.cantUseInteractive = False
        self.cantSpeakToNPC = False
        self.cantChangeZone = False
        self.cantAttackMonster = False
        self.cantWalk8Directions = False

    def serialize(self, param1):
        self.serializeAs_ActorRestrictionsInformations(param1)

    def serializeAs_ActorRestrictionsInformations(self, param1):
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.cantBeAggressed)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.cantBeChallenged)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,2,self.cantTrade)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,3,self.cantBeAttackedByMutant)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,4,self.cantRun)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,5,self.forceSlowWalk)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,6,self.cantMinimize)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,7,self.cantMove)
        param1.write_byte(_loc2_)
        _loc3_ = 0
        _loc3_ = BooleanByteWrapper.set_flag(_loc3_,0,self.cantAggress)
        _loc3_ = BooleanByteWrapper.set_flag(_loc3_,1,self.cantChallenge)
        _loc3_ = BooleanByteWrapper.set_flag(_loc3_,2,self.cantExchange)
        _loc3_ = BooleanByteWrapper.set_flag(_loc3_,3,self.cantAttack)
        _loc3_ = BooleanByteWrapper.set_flag(_loc3_,4,self.cantChat)
        _loc3_ = BooleanByteWrapper.set_flag(_loc3_,5,self.cantBeMerchant)
        _loc3_ = BooleanByteWrapper.set_flag(_loc3_,6,self.cantUseObject)
        _loc3_ = BooleanByteWrapper.set_flag(_loc3_,7,self.cantUseTaxCollector)
        param1.write_byte(_loc3_)
        _loc4_ = 0
        _loc4_ = BooleanByteWrapper.set_flag(_loc4_,0,self.cantUseInteractive)
        _loc4_ = BooleanByteWrapper.set_flag(_loc4_,1,self.cantSpeakToNPC)
        _loc4_ = BooleanByteWrapper.set_flag(_loc4_,2,self.cantChangeZone)
        _loc4_ = BooleanByteWrapper.set_flag(_loc4_,3,self.cantAttackMonster)
        _loc4_ = BooleanByteWrapper.set_flag(_loc4_,4,self.cantWalk8Directions)
        param1.write_byte(_loc4_)

    def deserialize(self, param1):
        self.deserializeAs_ActorRestrictionsInformations(param1)

    def deserializeAs_ActorRestrictionsInformations(self, param1):
        self.deserializeByteBoxes(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ActorRestrictionsInformations(param1)

    def deserializeAsyncAs_ActorRestrictionsInformations(self, param1):
        param1.add_child(self.deserializeByteBoxes)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.cantBeAggressed = BooleanByteWrapper.get_flag(_loc2_,0)
        self.cantBeChallenged = BooleanByteWrapper.get_flag(_loc2_,1)
        self.cantTrade = BooleanByteWrapper.get_flag(_loc2_,2)
        self.cantBeAttackedByMutant = BooleanByteWrapper.get_flag(_loc2_,3)
        self.cantRun = BooleanByteWrapper.get_flag(_loc2_,4)
        self.forceSlowWalk = BooleanByteWrapper.get_flag(_loc2_,5)
        self.cantMinimize = BooleanByteWrapper.get_flag(_loc2_,6)
        self.cantMove = BooleanByteWrapper.get_flag(_loc2_,7)
        _loc3_ = param1.read_byte()
        self.cantAggress = BooleanByteWrapper.get_flag(_loc3_,0)
        self.cantChallenge = BooleanByteWrapper.get_flag(_loc3_,1)
        self.cantExchange = BooleanByteWrapper.get_flag(_loc3_,2)
        self.cantAttack = BooleanByteWrapper.get_flag(_loc3_,3)
        self.cantChat = BooleanByteWrapper.get_flag(_loc3_,4)
        self.cantBeMerchant = BooleanByteWrapper.get_flag(_loc3_,5)
        self.cantUseObject = BooleanByteWrapper.get_flag(_loc3_,6)
        self.cantUseTaxCollector = BooleanByteWrapper.get_flag(_loc3_,7)
        _loc4_ = param1.read_byte()
        self.cantUseInteractive = BooleanByteWrapper.get_flag(_loc4_,0)
        self.cantSpeakToNPC = BooleanByteWrapper.get_flag(_loc4_,1)
        self.cantChangeZone = BooleanByteWrapper.get_flag(_loc4_,2)
        self.cantAttackMonster = BooleanByteWrapper.get_flag(_loc4_,3)
        self.cantWalk8Directions = BooleanByteWrapper.get_flag(_loc4_,4)


class PlayerStatus():
    protocolId = 415

    def __init__(self):
        super().__init__()
        self.statusId = 1

    def getTypeId(self):
        return 415

    def initPlayerStatus(self, param1=1):
        self.statusId = param1
        return self

    def reset(self):
        self.statusId = 1

    def serialize(self, param1):
        self.serializeAs_PlayerStatus(param1)

    def serializeAs_PlayerStatus(self, param1):
        param1.write_byte(self.statusId)

    def deserialize(self, param1):
        self.deserializeAs_PlayerStatus(param1)

    def deserializeAs_PlayerStatus(self, param1):
        self._statusIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PlayerStatus(param1)

    def deserializeAsyncAs_PlayerStatus(self, param1):
        param1.add_child(self._statusIdFunc)

    def _statusIdFunc(self, param1):
        self.statusId = param1.read_byte()
        if self.statusId < 0:
            raise RuntimeError("Forbidden value (" + str(self.statusId) + ") on element of PlayerStatus.statusId.")


class ActorOrientation():
    protocolId = 353

    def __init__(self):
        super().__init__()
        self.id = 0
        self.direction = 1

    def getTypeId(self):
        return 353

    def initActorOrientation(self, param1=0, param2=1):
        self.id = param1
        self.direction = param2
        return self

    def reset(self):
        self.id = 0
        self.direction = 1

    def serialize(self, param1):
        self.serializeAs_ActorOrientation(param1)

    def serializeAs_ActorOrientation(self, param1):
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_double(self.id)
        param1.write_byte(self.direction)

    def deserialize(self, param1):
        self.deserializeAs_ActorOrientation(param1)

    def deserializeAs_ActorOrientation(self, param1):
        self._idFunc(param1)
        self._directionFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ActorOrientation(param1)

    def deserializeAsyncAs_ActorOrientation(self, param1):
        param1.add_child(self._idFunc)
        param1.add_child(self._directionFunc)

    def _idFunc(self, param1):
        self.id = param1.read_double()
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of ActorOrientation.id.")

    def _directionFunc(self, param1):
        self.direction = param1.read_byte()
        if self.direction < 0:
            raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of ActorOrientation.direction.")


class EntityDispositionInformations():
    protocolId = 60

    def __init__(self):
        super().__init__()
        self.cellId = 0
        self.direction = 1

    def getTypeId(self):
        return 60

    def initEntityDispositionInformations(self, param1=0, param2=1):
        self.cellId = param1
        self.direction = param2
        return self

    def reset(self):
        self.cellId = 0
        self.direction = 1

    def serialize(self, param1):
        self.serializeAs_EntityDispositionInformations(param1)

    def serializeAs_EntityDispositionInformations(self, param1):
        if self.cellId < -1 or self.cellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element cellId.")
        param1.write_short(self.cellId)
        param1.write_byte(self.direction)

    def deserialize(self, param1):
        self.deserializeAs_EntityDispositionInformations(param1)

    def deserializeAs_EntityDispositionInformations(self, param1):
        self._cellIdFunc(param1)
        self._directionFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_EntityDispositionInformations(param1)

    def deserializeAsyncAs_EntityDispositionInformations(self, param1):
        param1.add_child(self._cellIdFunc)
        param1.add_child(self._directionFunc)

    def _cellIdFunc(self, param1):
        self.cellId = param1.read_short()
        if self.cellId < -1 or self.cellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of EntityDispositionInformations.cellId.")

    def _directionFunc(self, param1):
        self.direction = param1.read_byte()
        if self.direction < 0:
            raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of EntityDispositionInformations.direction.")


class EntityMovementInformations():
    protocolId = 63

    def __init__(self):
        super().__init__()
        self.id = 0
        self.steps = []
        self._stepstree = FuncTree()

    def getTypeId(self):
        return 63

    def initEntityMovementInformations(self, param1=0, param2=[]):
        self.id = param1
        self.steps = param2
        return self

    def reset(self):
        self.id = 0
        self.steps = []

    def serialize(self, param1):
        self.serializeAs_EntityMovementInformations(param1)

    def serializeAs_EntityMovementInformations(self, param1):
        param1.write_int(self.id)
        param1.write_short(len(self.steps))
        _loc2_ = 0
        while _loc2_ < len(self.steps):
            param1.write_byte(self.steps[_loc2_])
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_EntityMovementInformations(param1)

    def deserializeAs_EntityMovementInformations(self, param1):
        _loc4_ = 0
        self._idFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_byte()
            self.steps.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_EntityMovementInformations(param1)

    def deserializeAsyncAs_EntityMovementInformations(self, param1):
        param1.add_child(self._idFunc)
        self._stepstree = param1.add_child(self._stepstreeFunc)

    def _idFunc(self, param1):
        self.id = param1.read_int()

    def _stepstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._stepstree.add_child(self._stepsFunc)
            _loc3_ += 1

    def _stepsFunc(self, param1):
        _loc2_ = param1.read_byte()
        self.steps.append(_loc2_)


class GameContextActorInformations():
    protocolId = 150

    def __init__(self):
        super().__init__()
        self.contextualId = 0
        self.look = EntityLook()
        self.disposition = EntityDispositionInformations()
        self._looktree = FuncTree()
        self._dispositiontree = FuncTree()

    def getTypeId(self):
        return 150

    def initGameContextActorInformations(self, param1=0, param2=None, param3=None):
        self.contextualId = param1
        self.look = param2
        self.disposition = param3
        return self

    def reset(self):
        self.contextualId = 0
        self.look = EntityLook()

    def serialize(self, param1):
        self.serializeAs_GameContextActorInformations(param1)

    def serializeAs_GameContextActorInformations(self, param1):
        if self.contextualId < -9007199254740990 or self.contextualId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.contextualId) + ") on element contextualId.")
        param1.write_double(self.contextualId)
        self.look.serializeAs_EntityLook(param1)
        param1.write_short(self.disposition.getTypeId())
        self.disposition.serialize(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameContextActorInformations(param1)

    def deserializeAs_GameContextActorInformations(self, param1):
        self._contextualIdFunc(param1)
        self.look = EntityLook()
        self.look.deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        self.disposition = ProtocolTypeManager.get_instance(EntityDispositionInformations,_loc2_)
        self.disposition.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameContextActorInformations(param1)

    def deserializeAsyncAs_GameContextActorInformations(self, param1):
        param1.add_child(self._contextualIdFunc)
        self._looktree = param1.add_child(self._looktreeFunc)
        self._dispositiontree = param1.add_child(self._dispositiontreeFunc)

    def _contextualIdFunc(self, param1):
        self.contextualId = param1.read_double()
        if self.contextualId < -9007199254740990 or self.contextualId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.contextualId) + ") on element of GameContextActorInformations.contextualId.")

    def _looktreeFunc(self, param1):
        self.look = EntityLook()
        self.look.deserializeAsync(self._looktree)

    def _dispositiontreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.disposition = ProtocolTypeManager.get_instance(EntityDispositionInformations,_loc2_)
        self.disposition.deserializeAsync(self._dispositiontree)


class MapCoordinates():
    protocolId = 174

    def __init__(self):
        super().__init__()
        self.worldX = 0
        self.worldY = 0

    def getTypeId(self):
        return 174

    def initMapCoordinates(self, param1=0, param2=0):
        self.worldX = param1
        self.worldY = param2
        return self

    def reset(self):
        self.worldX = 0
        self.worldY = 0

    def serialize(self, param1):
        self.serializeAs_MapCoordinates(param1)

    def serializeAs_MapCoordinates(self, param1):
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)

    def deserialize(self, param1):
        self.deserializeAs_MapCoordinates(param1)

    def deserializeAs_MapCoordinates(self, param1):
        self._worldXFunc(param1)
        self._worldYFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MapCoordinates(param1)

    def deserializeAsyncAs_MapCoordinates(self, param1):
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of MapCoordinates.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of MapCoordinates.worldY.")


class TaxCollectorStaticInformations():
    protocolId = 147

    def __init__(self):
        super().__init__()
        self.firstNameId = 0
        self.lastNameId = 0
        self.guildIdentity = GuildInformations()
        self._guildIdentitytree = FuncTree()

    def getTypeId(self):
        return 147

    def initTaxCollectorStaticInformations(self, param1=0, param2=0, param3=None):
        self.firstNameId = param1
        self.lastNameId = param2
        self.guildIdentity = param3
        return self

    def reset(self):
        self.firstNameId = 0
        self.lastNameId = 0
        self.guildIdentity = GuildInformations()

    def serialize(self, param1):
        self.serializeAs_TaxCollectorStaticInformations(param1)

    def serializeAs_TaxCollectorStaticInformations(self, param1):
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element firstNameId.")
        param1.write_var_short(self.firstNameId)
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element lastNameId.")
        param1.write_var_short(self.lastNameId)
        self.guildIdentity.serializeAs_GuildInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorStaticInformations(param1)

    def deserializeAs_TaxCollectorStaticInformations(self, param1):
        self._firstNameIdFunc(param1)
        self._lastNameIdFunc(param1)
        self.guildIdentity = GuildInformations()
        self.guildIdentity.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorStaticInformations(param1)

    def deserializeAsyncAs_TaxCollectorStaticInformations(self, param1):
        param1.add_child(self._firstNameIdFunc)
        param1.add_child(self._lastNameIdFunc)
        self._guildIdentitytree = param1.add_child(self._guildIdentitytreeFunc)

    def _firstNameIdFunc(self, param1):
        self.firstNameId = param1.read_var_uh_short()
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of TaxCollectorStaticInformations.firstNameId.")

    def _lastNameIdFunc(self, param1):
        self.lastNameId = param1.read_var_uh_short()
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of TaxCollectorStaticInformations.lastNameId.")

    def _guildIdentitytreeFunc(self, param1):
        self.guildIdentity = GuildInformations()
        self.guildIdentity.deserializeAsync(self._guildIdentitytree)


class AbstractFightTeamInformations():
    protocolId = 116

    def __init__(self):
        super().__init__()
        self.teamId = 2
        self.leaderId = 0
        self.teamSide = 0
        self.teamTypeId = 0
        self.nbWaves = 0

    def getTypeId(self):
        return 116

    def initAbstractFightTeamInformations(self, param1=2, param2=0, param3=0, param4=0, param5=0):
        self.teamId = param1
        self.leaderId = param2
        self.teamSide = param3
        self.teamTypeId = param4
        self.nbWaves = param5
        return self

    def reset(self):
        self.teamId = 2
        self.leaderId = 0
        self.teamSide = 0
        self.teamTypeId = 0
        self.nbWaves = 0

    def serialize(self, param1):
        self.serializeAs_AbstractFightTeamInformations(param1)

    def serializeAs_AbstractFightTeamInformations(self, param1):
        param1.write_byte(self.teamId)
        if self.leaderId < -9007199254740990 or self.leaderId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.leaderId) + ") on element leaderId.")
        param1.write_double(self.leaderId)
        param1.write_byte(self.teamSide)
        param1.write_byte(self.teamTypeId)
        if self.nbWaves < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbWaves) + ") on element nbWaves.")
        param1.write_byte(self.nbWaves)

    def deserialize(self, param1):
        self.deserializeAs_AbstractFightTeamInformations(param1)

    def deserializeAs_AbstractFightTeamInformations(self, param1):
        self._teamIdFunc(param1)
        self._leaderIdFunc(param1)
        self._teamSideFunc(param1)
        self._teamTypeIdFunc(param1)
        self._nbWavesFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AbstractFightTeamInformations(param1)

    def deserializeAsyncAs_AbstractFightTeamInformations(self, param1):
        param1.add_child(self._teamIdFunc)
        param1.add_child(self._leaderIdFunc)
        param1.add_child(self._teamSideFunc)
        param1.add_child(self._teamTypeIdFunc)
        param1.add_child(self._nbWavesFunc)

    def _teamIdFunc(self, param1):
        self.teamId = param1.read_byte()
        if self.teamId < 0:
            raise RuntimeError("Forbidden value (" + str(self.teamId) + ") on element of AbstractFightTeamInformations.teamId.")

    def _leaderIdFunc(self, param1):
        self.leaderId = param1.read_double()
        if self.leaderId < -9007199254740990 or self.leaderId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.leaderId) + ") on element of AbstractFightTeamInformations.leaderId.")

    def _teamSideFunc(self, param1):
        self.teamSide = param1.read_byte()

    def _teamTypeIdFunc(self, param1):
        self.teamTypeId = param1.read_byte()
        if self.teamTypeId < 0:
            raise RuntimeError("Forbidden value (" + str(self.teamTypeId) + ") on element of AbstractFightTeamInformations.teamTypeId.")

    def _nbWavesFunc(self, param1):
        self.nbWaves = param1.read_byte()
        if self.nbWaves < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbWaves) + ") on element of AbstractFightTeamInformations.nbWaves.")


class FightCommonInformations():
    protocolId = 43

    def __init__(self):
        super().__init__()
        self.fightId = 0
        self.fightType = 0
        self.fightTeams = []
        self.fightTeamsPositions = []
        self.fightTeamsOptions = []
        self._fightTeamstree = FuncTree()
        self._fightTeamsPositionstree = FuncTree()
        self._fightTeamsOptionstree = FuncTree()

    def getTypeId(self):
        return 43

    def initFightCommonInformations(self, param1=0, param2=0, param3=[], param4=[], param5=[]):
        self.fightId = param1
        self.fightType = param2
        self.fightTeams = param3
        self.fightTeamsPositions = param4
        self.fightTeamsOptions = param5
        return self

    def reset(self):
        self.fightId = 0
        self.fightType = 0
        self.fightTeams = []
        self.fightTeamsPositions = []
        self.fightTeamsOptions = []

    def serialize(self, param1):
        self.serializeAs_FightCommonInformations(param1)

    def serializeAs_FightCommonInformations(self, param1):
        param1.write_int(self.fightId)
        param1.write_byte(self.fightType)
        param1.write_short(len(self.fightTeams))
        _loc2_ = 0
        while _loc2_ < len(self.fightTeams):
            param1.write_short(as_parent(self.fightTeams[_loc2_], FightTeamInformations).getTypeId())
            as_parent(self.fightTeams[_loc2_], FightTeamInformations).serialize(param1)
            _loc2_ += 1
        param1.write_short(len(self.fightTeamsPositions))
        _loc3_ = 0
        while _loc3_ < len(self.fightTeamsPositions):
            if self.fightTeamsPositions[_loc3_] < 0 or self.fightTeamsPositions[_loc3_] > 559:
                raise RuntimeError("Forbidden value (" + str(self.fightTeamsPositions[_loc3_]) + ") on element 4 (starting at 1) of fightTeamsPositions.")
            param1.write_var_short(self.fightTeamsPositions[_loc3_])
            _loc3_ += 1
        param1.write_short(len(self.fightTeamsOptions))
        _loc4_ = 0
        while _loc4_ < len(self.fightTeamsOptions):
            as_parent(self.fightTeamsOptions[_loc4_], FightOptionsInformations).serializeAs_FightOptionsInformations(param1)
            _loc4_ += 1

    def deserialize(self, param1):
        self.deserializeAs_FightCommonInformations(param1)

    def deserializeAs_FightCommonInformations(self, param1):
        _loc8_ = 0
        _loc9_ = None
        _loc10_ = 0
        _loc11_ = None
        self._fightIdFunc(param1)
        self._fightTypeFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc8_ = param1.read_unsigned_short()
            _loc9_ = ProtocolTypeManager.get_instance(FightTeamInformations,_loc8_)
            _loc9_.deserialize(param1)
            self.fightTeams.append(_loc9_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc10_ = param1.read_var_uh_short()
            if _loc10_ < 0 or _loc10_ > 559:
                raise RuntimeError("Forbidden value (" + str(_loc10_) + ") on elements of fightTeamsPositions.")
            self.fightTeamsPositions.append(_loc10_)
            _loc5_ += 1
        _loc6_ = param1.read_unsigned_short()
        _loc7_ = 0
        while _loc7_ < _loc6_:
            _loc11_ = FightOptionsInformations()
            _loc11_.deserialize(param1)
            self.fightTeamsOptions.append(_loc11_)
            _loc7_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightCommonInformations(param1)

    def deserializeAsyncAs_FightCommonInformations(self, param1):
        param1.add_child(self._fightIdFunc)
        param1.add_child(self._fightTypeFunc)
        self._fightTeamstree = param1.add_child(self._fightTeamstreeFunc)
        self._fightTeamsPositionstree = param1.add_child(self._fightTeamsPositionstreeFunc)
        self._fightTeamsOptionstree = param1.add_child(self._fightTeamsOptionstreeFunc)

    def _fightIdFunc(self, param1):
        self.fightId = param1.read_int()

    def _fightTypeFunc(self, param1):
        self.fightType = param1.read_byte()
        if self.fightType < 0:
            raise RuntimeError("Forbidden value (" + str(self.fightType) + ") on element of FightCommonInformations.fightType.")

    def _fightTeamstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._fightTeamstree.add_child(self._fightTeamsFunc)
            _loc3_ += 1

    def _fightTeamsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(FightTeamInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.fightTeams.append(_loc3_)

    def _fightTeamsPositionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._fightTeamsPositionstree.add_child(self._fightTeamsPositionsFunc)
            _loc3_ += 1

    def _fightTeamsPositionsFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0 or _loc2_ > 559:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of fightTeamsPositions.")
        self.fightTeamsPositions.append(_loc2_)

    def _fightTeamsOptionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._fightTeamsOptionstree.add_child(self._fightTeamsOptionsFunc)
            _loc3_ += 1

    def _fightTeamsOptionsFunc(self, param1):
        _loc2_ = FightOptionsInformations()
        _loc2_.deserialize(param1)
        self.fightTeamsOptions.append(_loc2_)


class FightExternalInformations():
    protocolId = 117

    def __init__(self):
        super().__init__()
        self.fightId = 0
        self.fightType = 0
        self.fightStart = 0
        self.fightSpectatorLocked = False
        self.fightTeams = []
        self.fightTeamsOptions = []
        self._fightTeamstree = FuncTree()
        self._fightTeamsindex = 0
        self._fightTeamsOptionstree = FuncTree()
        self._fightTeamsOptionsindex = 0

    def getTypeId(self):
        return 117

    def initFightExternalInformations(self, param1=0, param2=0, param3=0, param4=False, param5=[], param6=[]):
        self.fightId = param1
        self.fightType = param2
        self.fightStart = param3
        self.fightSpectatorLocked = param4
        self.fightTeams = param5
        self.fightTeamsOptions = param6
        return self

    def reset(self):
        self.fightId = 0
        self.fightType = 0
        self.fightStart = 0
        self.fightSpectatorLocked = False
        self.fightTeams = []
        self.fightTeamsOptions = []

    def serialize(self, param1):
        self.serializeAs_FightExternalInformations(param1)

    def serializeAs_FightExternalInformations(self, param1):
        param1.write_int(self.fightId)
        param1.write_byte(self.fightType)
        if self.fightStart < 0:
            raise RuntimeError("Forbidden value (" + str(self.fightStart) + ") on element fightStart.")
        param1.write_int(self.fightStart)
        param1.write_boolean(self.fightSpectatorLocked)
        _loc2_ = 0
        while _loc2_ < 2:
            self.fightTeams[_loc2_].serializeAs_FightTeamLightInformations(param1)
            _loc2_ += 1
        _loc3_ = 0
        while _loc3_ < 2:
            self.fightTeamsOptions[_loc3_].serializeAs_FightOptionsInformations(param1)
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_FightExternalInformations(param1)

    def deserializeAs_FightExternalInformations(self, param1):
        self._fightIdFunc(param1)
        self._fightTypeFunc(param1)
        self._fightStartFunc(param1)
        self._fightSpectatorLockedFunc(param1)
        _loc2_ = 0
        while _loc2_ < 2:
            self.fightTeams.append(FightTeamLightInformations())
            self.fightTeams[_loc2_].deserialize(param1)
            _loc2_ += 1
        _loc3_ = 0
        while _loc3_ < 2:
            self.fightTeamsOptions.append(FightOptionsInformations())
            self.fightTeamsOptions[_loc3_].deserialize(param1)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightExternalInformations(param1)

    def deserializeAsyncAs_FightExternalInformations(self, param1):
        param1.add_child(self._fightIdFunc)
        param1.add_child(self._fightTypeFunc)
        param1.add_child(self._fightStartFunc)
        param1.add_child(self._fightSpectatorLockedFunc)
        self._fightTeamstree = param1.add_child(self._fightTeamstreeFunc)
        self._fightTeamsOptionstree = param1.add_child(self._fightTeamsOptionstreeFunc)

    def _fightIdFunc(self, param1):
        self.fightId = param1.read_int()

    def _fightTypeFunc(self, param1):
        self.fightType = param1.read_byte()
        if self.fightType < 0:
            raise RuntimeError("Forbidden value (" + str(self.fightType) + ") on element of FightExternalInformations.fightType.")

    def _fightStartFunc(self, param1):
        self.fightStart = param1.read_int()
        if self.fightStart < 0:
            raise RuntimeError("Forbidden value (" + str(self.fightStart) + ") on element of FightExternalInformations.fightStart.")

    def _fightSpectatorLockedFunc(self, param1):
        self.fightSpectatorLocked = param1.read_boolean()

    def _fightTeamstreeFunc(self, param1):
        _loc2_ = 0
        while _loc2_ < 2:
            self._fightTeamstree.add_child(self._fightTeamsFunc)
            _loc2_ += 1

    def _fightTeamsFunc(self, param1):
        self.fightTeams[self._fightTeamsindex] = FightTeamLightInformations()
        self.fightTeams[self._fightTeamsindex].deserializeAsync(self._fightTeamstree.children[self._fightTeamsindex])
        self._fightTeamsindex += 1

    def _fightTeamsOptionstreeFunc(self, param1):
        _loc2_ = 0
        while _loc2_ < 2:
            self._fightTeamsOptionstree.add_child(self._fightTeamsOptionsFunc)
            _loc2_ += 1

    def _fightTeamsOptionsFunc(self, param1):
        self.fightTeamsOptions[self._fightTeamsOptionsindex] = FightOptionsInformations()
        self.fightTeamsOptions[self._fightTeamsOptionsindex].deserializeAsync(self._fightTeamsOptionstree.children[self._fightTeamsOptionsindex])
        self._fightTeamsOptionsindex += 1


class FightLoot():
    protocolId = 41

    def __init__(self):
        super().__init__()
        self.objects = []
        self.kamas = 0
        self._objectstree = FuncTree()

    def getTypeId(self):
        return 41

    def initFightLoot(self, param1=[], param2=0):
        self.objects = param1
        self.kamas = param2
        return self

    def reset(self):
        self.objects = []
        self.kamas = 0

    def serialize(self, param1):
        self.serializeAs_FightLoot(param1)

    def serializeAs_FightLoot(self, param1):
        param1.write_short(len(self.objects))
        _loc2_ = 0
        while _loc2_ < len(self.objects):
            if self.objects[_loc2_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.objects[_loc2_]) + ") on element 1 (starting at 1) of objects.")
            param1.write_var_short(self.objects[_loc2_])
            _loc2_ += 1
        if self.kamas < 0 or self.kamas > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element kamas.")
        param1.write_var_long(self.kamas)

    def deserialize(self, param1):
        self.deserializeAs_FightLoot(param1)

    def deserializeAs_FightLoot(self, param1):
        _loc4_ = 0
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_var_uh_short()
            if _loc4_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc4_) + ") on elements of objects.")
            self.objects.append(_loc4_)
            _loc3_ += 1
        self._kamasFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightLoot(param1)

    def deserializeAsyncAs_FightLoot(self, param1):
        self._objectstree = param1.add_child(self._objectstreeFunc)
        param1.add_child(self._kamasFunc)

    def _objectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._objectstree.add_child(self._objectsFunc)
            _loc3_ += 1

    def _objectsFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of objects.")
        self.objects.append(_loc2_)

    def _kamasFunc(self, param1):
        self.kamas = param1.read_var_uh_long()
        if self.kamas < 0 or self.kamas > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element of FightLoot.kamas.")


class FightOptionsInformations():
    protocolId = 20

    def __init__(self):
        super().__init__()
        self.isSecret = False
        self.isRestrictedToPartyOnly = False
        self.isClosed = False
        self.isAskingForHelp = False

    def getTypeId(self):
        return 20

    def initFightOptionsInformations(self, param1=False, param2=False, param3=False, param4=False):
        self.isSecret = param1
        self.isRestrictedToPartyOnly = param2
        self.isClosed = param3
        self.isAskingForHelp = param4
        return self

    def reset(self):
        self.isSecret = False
        self.isRestrictedToPartyOnly = False
        self.isClosed = False
        self.isAskingForHelp = False

    def serialize(self, param1):
        self.serializeAs_FightOptionsInformations(param1)

    def serializeAs_FightOptionsInformations(self, param1):
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.isSecret)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.isRestrictedToPartyOnly)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,2,self.isClosed)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,3,self.isAskingForHelp)
        param1.write_byte(_loc2_)

    def deserialize(self, param1):
        self.deserializeAs_FightOptionsInformations(param1)

    def deserializeAs_FightOptionsInformations(self, param1):
        self.deserializeByteBoxes(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightOptionsInformations(param1)

    def deserializeAsyncAs_FightOptionsInformations(self, param1):
        param1.add_child(self.deserializeByteBoxes)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.isSecret = BooleanByteWrapper.get_flag(_loc2_,0)
        self.isRestrictedToPartyOnly = BooleanByteWrapper.get_flag(_loc2_,1)
        self.isClosed = BooleanByteWrapper.get_flag(_loc2_,2)
        self.isAskingForHelp = BooleanByteWrapper.get_flag(_loc2_,3)


class FightResultAdditionalData():
    protocolId = 191

    def getTypeId(self):
        return 191

    def initFightResultAdditionalData(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_FightResultAdditionalData(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_FightResultAdditionalData(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_FightResultAdditionalData(self, param1):
        pass


class FightResultListEntry():
    protocolId = 16

    def __init__(self):
        super().__init__()
        self.outcome = 0
        self.wave = 0
        self.rewards = FightLoot()
        self._rewardstree = FuncTree()

    def getTypeId(self):
        return 16

    def initFightResultListEntry(self, param1=0, param2=0, param3=None):
        self.outcome = param1
        self.wave = param2
        self.rewards = param3
        return self

    def reset(self):
        self.outcome = 0
        self.wave = 0
        self.rewards = FightLoot()

    def serialize(self, param1):
        self.serializeAs_FightResultListEntry(param1)

    def serializeAs_FightResultListEntry(self, param1):
        param1.write_var_short(self.outcome)
        if self.wave < 0:
            raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element wave.")
        param1.write_byte(self.wave)
        self.rewards.serializeAs_FightLoot(param1)

    def deserialize(self, param1):
        self.deserializeAs_FightResultListEntry(param1)

    def deserializeAs_FightResultListEntry(self, param1):
        self._outcomeFunc(param1)
        self._waveFunc(param1)
        self.rewards = FightLoot()
        self.rewards.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightResultListEntry(param1)

    def deserializeAsyncAs_FightResultListEntry(self, param1):
        param1.add_child(self._outcomeFunc)
        param1.add_child(self._waveFunc)
        self._rewardstree = param1.add_child(self._rewardstreeFunc)

    def _outcomeFunc(self, param1):
        self.outcome = param1.read_var_uh_short()
        if self.outcome < 0:
            raise RuntimeError("Forbidden value (" + str(self.outcome) + ") on element of FightResultListEntry.outcome.")

    def _waveFunc(self, param1):
        self.wave = param1.read_byte()
        if self.wave < 0:
            raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element of FightResultListEntry.wave.")

    def _rewardstreeFunc(self, param1):
        self.rewards = FightLoot()
        self.rewards.deserializeAsync(self._rewardstree)


class FightStartingPositions():
    protocolId = 513

    def __init__(self):
        super().__init__()
        self.positionsForChallengers = []
        self.positionsForDefenders = []
        self._positionsForChallengerstree = FuncTree()
        self._positionsForDefenderstree = FuncTree()

    def getTypeId(self):
        return 513

    def initFightStartingPositions(self, param1=[], param2=[]):
        self.positionsForChallengers = param1
        self.positionsForDefenders = param2
        return self

    def reset(self):
        self.positionsForChallengers = []
        self.positionsForDefenders = []

    def serialize(self, param1):
        self.serializeAs_FightStartingPositions(param1)

    def serializeAs_FightStartingPositions(self, param1):
        param1.write_short(len(self.positionsForChallengers))
        _loc2_ = 0
        while _loc2_ < len(self.positionsForChallengers):
            if self.positionsForChallengers[_loc2_] < 0 or self.positionsForChallengers[_loc2_] > 559:
                raise RuntimeError("Forbidden value (" + str(self.positionsForChallengers[_loc2_]) + ") on element 1 (starting at 1) of positionsForChallengers.")
            param1.write_var_short(self.positionsForChallengers[_loc2_])
            _loc2_ += 1
        param1.write_short(len(self.positionsForDefenders))
        _loc3_ = 0
        while _loc3_ < len(self.positionsForDefenders):
            if self.positionsForDefenders[_loc3_] < 0 or self.positionsForDefenders[_loc3_] > 559:
                raise RuntimeError("Forbidden value (" + str(self.positionsForDefenders[_loc3_]) + ") on element 2 (starting at 1) of positionsForDefenders.")
            param1.write_var_short(self.positionsForDefenders[_loc3_])
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_FightStartingPositions(param1)

    def deserializeAs_FightStartingPositions(self, param1):
        _loc6_ = 0
        _loc7_ = 0
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_var_uh_short()
            if _loc6_ < 0 or _loc6_ > 559:
                raise RuntimeError("Forbidden value (" + str(_loc6_) + ") on elements of positionsForChallengers.")
            self.positionsForChallengers.append(_loc6_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc7_ = param1.read_var_uh_short()
            if _loc7_ < 0 or _loc7_ > 559:
                raise RuntimeError("Forbidden value (" + str(_loc7_) + ") on elements of positionsForDefenders.")
            self.positionsForDefenders.append(_loc7_)
            _loc5_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightStartingPositions(param1)

    def deserializeAsyncAs_FightStartingPositions(self, param1):
        self._positionsForChallengerstree = param1.add_child(self._positionsForChallengerstreeFunc)
        self._positionsForDefenderstree = param1.add_child(self._positionsForDefenderstreeFunc)

    def _positionsForChallengerstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._positionsForChallengerstree.add_child(self._positionsForChallengersFunc)
            _loc3_ += 1

    def _positionsForChallengersFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0 or _loc2_ > 559:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of positionsForChallengers.")
        self.positionsForChallengers.append(_loc2_)

    def _positionsForDefenderstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._positionsForDefenderstree.add_child(self._positionsForDefendersFunc)
            _loc3_ += 1

    def _positionsForDefendersFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0 or _loc2_ > 559:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of positionsForDefenders.")
        self.positionsForDefenders.append(_loc2_)


class FightTeamMemberInformations():
    protocolId = 44

    def __init__(self):
        super().__init__()
        self.id = 0

    def getTypeId(self):
        return 44

    def initFightTeamMemberInformations(self, param1=0):
        self.id = param1
        return self

    def reset(self):
        self.id = 0

    def serialize(self, param1):
        self.serializeAs_FightTeamMemberInformations(param1)

    def serializeAs_FightTeamMemberInformations(self, param1):
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_double(self.id)

    def deserialize(self, param1):
        self.deserializeAs_FightTeamMemberInformations(param1)

    def deserializeAs_FightTeamMemberInformations(self, param1):
        self._idFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTeamMemberInformations(param1)

    def deserializeAsyncAs_FightTeamMemberInformations(self, param1):
        param1.add_child(self._idFunc)

    def _idFunc(self, param1):
        self.id = param1.read_double()
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of FightTeamMemberInformations.id.")


class GameFightFighterLightInformations():
    protocolId = 413

    def __init__(self):
        super().__init__()
        self.id = 0
        self.wave = 0
        self.level = 0
        self.breed = 0
        self.sex = False
        self.alive = False

    def getTypeId(self):
        return 413

    def initGameFightFighterLightInformations(self, param1=0, param2=0, param3=0, param4=0, param5=False, param6=False):
        self.id = param1
        self.wave = param2
        self.level = param3
        self.breed = param4
        self.sex = param5
        self.alive = param6
        return self

    def reset(self):
        self.id = 0
        self.wave = 0
        self.level = 0
        self.breed = 0
        self.sex = False
        self.alive = False

    def serialize(self, param1):
        self.serializeAs_GameFightFighterLightInformations(param1)

    def serializeAs_GameFightFighterLightInformations(self, param1):
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.sex)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.alive)
        param1.write_byte(_loc2_)
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_double(self.id)
        if self.wave < 0:
            raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element wave.")
        param1.write_byte(self.wave)
        if self.level < 0:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_var_short(self.level)
        param1.write_byte(self.breed)

    def deserialize(self, param1):
        self.deserializeAs_GameFightFighterLightInformations(param1)

    def deserializeAs_GameFightFighterLightInformations(self, param1):
        self.deserializeByteBoxes(param1)
        self._idFunc(param1)
        self._waveFunc(param1)
        self._levelFunc(param1)
        self._breedFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightFighterLightInformations(param1)

    def deserializeAsyncAs_GameFightFighterLightInformations(self, param1):
        param1.add_child(self.deserializeByteBoxes)
        param1.add_child(self._idFunc)
        param1.add_child(self._waveFunc)
        param1.add_child(self._levelFunc)
        param1.add_child(self._breedFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.sex = BooleanByteWrapper.get_flag(_loc2_,0)
        self.alive = BooleanByteWrapper.get_flag(_loc2_,1)

    def _idFunc(self, param1):
        self.id = param1.read_double()
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of GameFightFighterLightInformations.id.")

    def _waveFunc(self, param1):
        self.wave = param1.read_byte()
        if self.wave < 0:
            raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element of GameFightFighterLightInformations.wave.")

    def _levelFunc(self, param1):
        self.level = param1.read_var_uh_short()
        if self.level < 0:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of GameFightFighterLightInformations.level.")

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()


class GameFightMinimalStats():
    protocolId = 31

    def __init__(self):
        super().__init__()
        self.lifePoints = 0
        self.maxLifePoints = 0
        self.baseMaxLifePoints = 0
        self.permanentDamagePercent = 0
        self.shieldPoints = 0
        self.actionPoints = 0
        self.maxActionPoints = 0
        self.movementPoints = 0
        self.maxMovementPoints = 0
        self.summoner = 0
        self.summoned = False
        self.neutralElementResistPercent = 0
        self.earthElementResistPercent = 0
        self.waterElementResistPercent = 0
        self.airElementResistPercent = 0
        self.fireElementResistPercent = 0
        self.neutralElementReduction = 0
        self.earthElementReduction = 0
        self.waterElementReduction = 0
        self.airElementReduction = 0
        self.fireElementReduction = 0
        self.criticalDamageFixedResist = 0
        self.pushDamageFixedResist = 0
        self.pvpNeutralElementResistPercent = 0
        self.pvpEarthElementResistPercent = 0
        self.pvpWaterElementResistPercent = 0
        self.pvpAirElementResistPercent = 0
        self.pvpFireElementResistPercent = 0
        self.pvpNeutralElementReduction = 0
        self.pvpEarthElementReduction = 0
        self.pvpWaterElementReduction = 0
        self.pvpAirElementReduction = 0
        self.pvpFireElementReduction = 0
        self.dodgePALostProbability = 0
        self.dodgePMLostProbability = 0
        self.tackleBlock = 0
        self.tackleEvade = 0
        self.fixedDamageReflection = 0
        self.invisibilityState = 0
        self.meleeDamageReceivedPercent = 0
        self.rangedDamageReceivedPercent = 0
        self.weaponDamageReceivedPercent = 0
        self.spellDamageReceivedPercent = 0

    def getTypeId(self):
        return 31

    def initGameFightMinimalStats(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0, param8=0, param9=0, param10=0, param11=False, param12=0, param13=0, param14=0, param15=0, param16=0, param17=0, param18=0, param19=0, param20=0, param21=0, param22=0, param23=0, param24=0, param25=0, param26=0, param27=0, param28=0, param29=0, param30=0, param31=0, param32=0, param33=0, param34=0, param35=0, param36=0, param37=0, param38=0, param39=0, param40=0, param41=0, param42=0, param43=0):
        self.lifePoints = param1
        self.maxLifePoints = param2
        self.baseMaxLifePoints = param3
        self.permanentDamagePercent = param4
        self.shieldPoints = param5
        self.actionPoints = param6
        self.maxActionPoints = param7
        self.movementPoints = param8
        self.maxMovementPoints = param9
        self.summoner = param10
        self.summoned = param11
        self.neutralElementResistPercent = param12
        self.earthElementResistPercent = param13
        self.waterElementResistPercent = param14
        self.airElementResistPercent = param15
        self.fireElementResistPercent = param16
        self.neutralElementReduction = param17
        self.earthElementReduction = param18
        self.waterElementReduction = param19
        self.airElementReduction = param20
        self.fireElementReduction = param21
        self.criticalDamageFixedResist = param22
        self.pushDamageFixedResist = param23
        self.pvpNeutralElementResistPercent = param24
        self.pvpEarthElementResistPercent = param25
        self.pvpWaterElementResistPercent = param26
        self.pvpAirElementResistPercent = param27
        self.pvpFireElementResistPercent = param28
        self.pvpNeutralElementReduction = param29
        self.pvpEarthElementReduction = param30
        self.pvpWaterElementReduction = param31
        self.pvpAirElementReduction = param32
        self.pvpFireElementReduction = param33
        self.dodgePALostProbability = param34
        self.dodgePMLostProbability = param35
        self.tackleBlock = param36
        self.tackleEvade = param37
        self.fixedDamageReflection = param38
        self.invisibilityState = param39
        self.meleeDamageReceivedPercent = param40
        self.rangedDamageReceivedPercent = param41
        self.weaponDamageReceivedPercent = param42
        self.spellDamageReceivedPercent = param43
        return self

    def reset(self):
        self.lifePoints = 0
        self.maxLifePoints = 0
        self.baseMaxLifePoints = 0
        self.permanentDamagePercent = 0
        self.shieldPoints = 0
        self.actionPoints = 0
        self.maxActionPoints = 0
        self.movementPoints = 0
        self.maxMovementPoints = 0
        self.summoner = 0
        self.summoned = False
        self.neutralElementResistPercent = 0
        self.earthElementResistPercent = 0
        self.waterElementResistPercent = 0
        self.airElementResistPercent = 0
        self.fireElementResistPercent = 0
        self.neutralElementReduction = 0
        self.earthElementReduction = 0
        self.waterElementReduction = 0
        self.airElementReduction = 0
        self.fireElementReduction = 0
        self.criticalDamageFixedResist = 0
        self.pushDamageFixedResist = 0
        self.pvpNeutralElementResistPercent = 0
        self.pvpEarthElementResistPercent = 0
        self.pvpWaterElementResistPercent = 0
        self.pvpAirElementResistPercent = 0
        self.pvpFireElementResistPercent = 0
        self.pvpNeutralElementReduction = 0
        self.pvpEarthElementReduction = 0
        self.pvpWaterElementReduction = 0
        self.pvpAirElementReduction = 0
        self.pvpFireElementReduction = 0
        self.dodgePALostProbability = 0
        self.dodgePMLostProbability = 0
        self.tackleBlock = 0
        self.tackleEvade = 0
        self.fixedDamageReflection = 0
        self.invisibilityState = 0
        self.meleeDamageReceivedPercent = 0
        self.rangedDamageReceivedPercent = 0
        self.weaponDamageReceivedPercent = 0
        self.spellDamageReceivedPercent = 0

    def serialize(self, param1):
        self.serializeAs_GameFightMinimalStats(param1)

    def serializeAs_GameFightMinimalStats(self, param1):
        if self.lifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element lifePoints.")
        param1.write_var_int(self.lifePoints)
        if self.maxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element maxLifePoints.")
        param1.write_var_int(self.maxLifePoints)
        if self.baseMaxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.baseMaxLifePoints) + ") on element baseMaxLifePoints.")
        param1.write_var_int(self.baseMaxLifePoints)
        if self.permanentDamagePercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.permanentDamagePercent) + ") on element permanentDamagePercent.")
        param1.write_var_int(self.permanentDamagePercent)
        if self.shieldPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.shieldPoints) + ") on element shieldPoints.")
        param1.write_var_int(self.shieldPoints)
        param1.write_var_short(self.actionPoints)
        param1.write_var_short(self.maxActionPoints)
        param1.write_var_short(self.movementPoints)
        param1.write_var_short(self.maxMovementPoints)
        if self.summoner < -9007199254740990 or self.summoner > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.summoner) + ") on element summoner.")
        param1.write_double(self.summoner)
        param1.write_boolean(self.summoned)
        param1.write_var_short(self.neutralElementResistPercent)
        param1.write_var_short(self.earthElementResistPercent)
        param1.write_var_short(self.waterElementResistPercent)
        param1.write_var_short(self.airElementResistPercent)
        param1.write_var_short(self.fireElementResistPercent)
        param1.write_var_short(self.neutralElementReduction)
        param1.write_var_short(self.earthElementReduction)
        param1.write_var_short(self.waterElementReduction)
        param1.write_var_short(self.airElementReduction)
        param1.write_var_short(self.fireElementReduction)
        param1.write_var_short(self.criticalDamageFixedResist)
        param1.write_var_short(self.pushDamageFixedResist)
        param1.write_var_short(self.pvpNeutralElementResistPercent)
        param1.write_var_short(self.pvpEarthElementResistPercent)
        param1.write_var_short(self.pvpWaterElementResistPercent)
        param1.write_var_short(self.pvpAirElementResistPercent)
        param1.write_var_short(self.pvpFireElementResistPercent)
        param1.write_var_short(self.pvpNeutralElementReduction)
        param1.write_var_short(self.pvpEarthElementReduction)
        param1.write_var_short(self.pvpWaterElementReduction)
        param1.write_var_short(self.pvpAirElementReduction)
        param1.write_var_short(self.pvpFireElementReduction)
        if self.dodgePALostProbability < 0:
            raise RuntimeError("Forbidden value (" + str(self.dodgePALostProbability) + ") on element dodgePALostProbability.")
        param1.write_var_short(self.dodgePALostProbability)
        if self.dodgePMLostProbability < 0:
            raise RuntimeError("Forbidden value (" + str(self.dodgePMLostProbability) + ") on element dodgePMLostProbability.")
        param1.write_var_short(self.dodgePMLostProbability)
        param1.write_var_short(self.tackleBlock)
        param1.write_var_short(self.tackleEvade)
        param1.write_var_short(self.fixedDamageReflection)
        param1.write_byte(self.invisibilityState)
        if self.meleeDamageReceivedPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.meleeDamageReceivedPercent) + ") on element meleeDamageReceivedPercent.")
        param1.write_var_short(self.meleeDamageReceivedPercent)
        if self.rangedDamageReceivedPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.rangedDamageReceivedPercent) + ") on element rangedDamageReceivedPercent.")
        param1.write_var_short(self.rangedDamageReceivedPercent)
        if self.weaponDamageReceivedPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.weaponDamageReceivedPercent) + ") on element weaponDamageReceivedPercent.")
        param1.write_var_short(self.weaponDamageReceivedPercent)
        if self.spellDamageReceivedPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellDamageReceivedPercent) + ") on element spellDamageReceivedPercent.")
        param1.write_var_short(self.spellDamageReceivedPercent)

    def deserialize(self, param1):
        self.deserializeAs_GameFightMinimalStats(param1)

    def deserializeAs_GameFightMinimalStats(self, param1):
        self._lifePointsFunc(param1)
        self._maxLifePointsFunc(param1)
        self._baseMaxLifePointsFunc(param1)
        self._permanentDamagePercentFunc(param1)
        self._shieldPointsFunc(param1)
        self._actionPointsFunc(param1)
        self._maxActionPointsFunc(param1)
        self._movementPointsFunc(param1)
        self._maxMovementPointsFunc(param1)
        self._summonerFunc(param1)
        self._summonedFunc(param1)
        self._neutralElementResistPercentFunc(param1)
        self._earthElementResistPercentFunc(param1)
        self._waterElementResistPercentFunc(param1)
        self._airElementResistPercentFunc(param1)
        self._fireElementResistPercentFunc(param1)
        self._neutralElementReductionFunc(param1)
        self._earthElementReductionFunc(param1)
        self._waterElementReductionFunc(param1)
        self._airElementReductionFunc(param1)
        self._fireElementReductionFunc(param1)
        self._criticalDamageFixedResistFunc(param1)
        self._pushDamageFixedResistFunc(param1)
        self._pvpNeutralElementResistPercentFunc(param1)
        self._pvpEarthElementResistPercentFunc(param1)
        self._pvpWaterElementResistPercentFunc(param1)
        self._pvpAirElementResistPercentFunc(param1)
        self._pvpFireElementResistPercentFunc(param1)
        self._pvpNeutralElementReductionFunc(param1)
        self._pvpEarthElementReductionFunc(param1)
        self._pvpWaterElementReductionFunc(param1)
        self._pvpAirElementReductionFunc(param1)
        self._pvpFireElementReductionFunc(param1)
        self._dodgePALostProbabilityFunc(param1)
        self._dodgePMLostProbabilityFunc(param1)
        self._tackleBlockFunc(param1)
        self._tackleEvadeFunc(param1)
        self._fixedDamageReflectionFunc(param1)
        self._invisibilityStateFunc(param1)
        self._meleeDamageReceivedPercentFunc(param1)
        self._rangedDamageReceivedPercentFunc(param1)
        self._weaponDamageReceivedPercentFunc(param1)
        self._spellDamageReceivedPercentFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightMinimalStats(param1)

    def deserializeAsyncAs_GameFightMinimalStats(self, param1):
        param1.add_child(self._lifePointsFunc)
        param1.add_child(self._maxLifePointsFunc)
        param1.add_child(self._baseMaxLifePointsFunc)
        param1.add_child(self._permanentDamagePercentFunc)
        param1.add_child(self._shieldPointsFunc)
        param1.add_child(self._actionPointsFunc)
        param1.add_child(self._maxActionPointsFunc)
        param1.add_child(self._movementPointsFunc)
        param1.add_child(self._maxMovementPointsFunc)
        param1.add_child(self._summonerFunc)
        param1.add_child(self._summonedFunc)
        param1.add_child(self._neutralElementResistPercentFunc)
        param1.add_child(self._earthElementResistPercentFunc)
        param1.add_child(self._waterElementResistPercentFunc)
        param1.add_child(self._airElementResistPercentFunc)
        param1.add_child(self._fireElementResistPercentFunc)
        param1.add_child(self._neutralElementReductionFunc)
        param1.add_child(self._earthElementReductionFunc)
        param1.add_child(self._waterElementReductionFunc)
        param1.add_child(self._airElementReductionFunc)
        param1.add_child(self._fireElementReductionFunc)
        param1.add_child(self._criticalDamageFixedResistFunc)
        param1.add_child(self._pushDamageFixedResistFunc)
        param1.add_child(self._pvpNeutralElementResistPercentFunc)
        param1.add_child(self._pvpEarthElementResistPercentFunc)
        param1.add_child(self._pvpWaterElementResistPercentFunc)
        param1.add_child(self._pvpAirElementResistPercentFunc)
        param1.add_child(self._pvpFireElementResistPercentFunc)
        param1.add_child(self._pvpNeutralElementReductionFunc)
        param1.add_child(self._pvpEarthElementReductionFunc)
        param1.add_child(self._pvpWaterElementReductionFunc)
        param1.add_child(self._pvpAirElementReductionFunc)
        param1.add_child(self._pvpFireElementReductionFunc)
        param1.add_child(self._dodgePALostProbabilityFunc)
        param1.add_child(self._dodgePMLostProbabilityFunc)
        param1.add_child(self._tackleBlockFunc)
        param1.add_child(self._tackleEvadeFunc)
        param1.add_child(self._fixedDamageReflectionFunc)
        param1.add_child(self._invisibilityStateFunc)
        param1.add_child(self._meleeDamageReceivedPercentFunc)
        param1.add_child(self._rangedDamageReceivedPercentFunc)
        param1.add_child(self._weaponDamageReceivedPercentFunc)
        param1.add_child(self._spellDamageReceivedPercentFunc)

    def _lifePointsFunc(self, param1):
        self.lifePoints = param1.read_var_uh_int()
        if self.lifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element of GameFightMinimalStats.lifePoints.")

    def _maxLifePointsFunc(self, param1):
        self.maxLifePoints = param1.read_var_uh_int()
        if self.maxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element of GameFightMinimalStats.maxLifePoints.")

    def _baseMaxLifePointsFunc(self, param1):
        self.baseMaxLifePoints = param1.read_var_uh_int()
        if self.baseMaxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.baseMaxLifePoints) + ") on element of GameFightMinimalStats.baseMaxLifePoints.")

    def _permanentDamagePercentFunc(self, param1):
        self.permanentDamagePercent = param1.read_var_uh_int()
        if self.permanentDamagePercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.permanentDamagePercent) + ") on element of GameFightMinimalStats.permanentDamagePercent.")

    def _shieldPointsFunc(self, param1):
        self.shieldPoints = param1.read_var_uh_int()
        if self.shieldPoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.shieldPoints) + ") on element of GameFightMinimalStats.shieldPoints.")

    def _actionPointsFunc(self, param1):
        self.actionPoints = param1.read_var_short()

    def _maxActionPointsFunc(self, param1):
        self.maxActionPoints = param1.read_var_short()

    def _movementPointsFunc(self, param1):
        self.movementPoints = param1.read_var_short()

    def _maxMovementPointsFunc(self, param1):
        self.maxMovementPoints = param1.read_var_short()

    def _summonerFunc(self, param1):
        self.summoner = param1.read_double()
        if self.summoner < -9007199254740990 or self.summoner > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.summoner) + ") on element of GameFightMinimalStats.summoner.")

    def _summonedFunc(self, param1):
        self.summoned = param1.read_boolean()

    def _neutralElementResistPercentFunc(self, param1):
        self.neutralElementResistPercent = param1.read_var_short()

    def _earthElementResistPercentFunc(self, param1):
        self.earthElementResistPercent = param1.read_var_short()

    def _waterElementResistPercentFunc(self, param1):
        self.waterElementResistPercent = param1.read_var_short()

    def _airElementResistPercentFunc(self, param1):
        self.airElementResistPercent = param1.read_var_short()

    def _fireElementResistPercentFunc(self, param1):
        self.fireElementResistPercent = param1.read_var_short()

    def _neutralElementReductionFunc(self, param1):
        self.neutralElementReduction = param1.read_var_short()

    def _earthElementReductionFunc(self, param1):
        self.earthElementReduction = param1.read_var_short()

    def _waterElementReductionFunc(self, param1):
        self.waterElementReduction = param1.read_var_short()

    def _airElementReductionFunc(self, param1):
        self.airElementReduction = param1.read_var_short()

    def _fireElementReductionFunc(self, param1):
        self.fireElementReduction = param1.read_var_short()

    def _criticalDamageFixedResistFunc(self, param1):
        self.criticalDamageFixedResist = param1.read_var_short()

    def _pushDamageFixedResistFunc(self, param1):
        self.pushDamageFixedResist = param1.read_var_short()

    def _pvpNeutralElementResistPercentFunc(self, param1):
        self.pvpNeutralElementResistPercent = param1.read_var_short()

    def _pvpEarthElementResistPercentFunc(self, param1):
        self.pvpEarthElementResistPercent = param1.read_var_short()

    def _pvpWaterElementResistPercentFunc(self, param1):
        self.pvpWaterElementResistPercent = param1.read_var_short()

    def _pvpAirElementResistPercentFunc(self, param1):
        self.pvpAirElementResistPercent = param1.read_var_short()

    def _pvpFireElementResistPercentFunc(self, param1):
        self.pvpFireElementResistPercent = param1.read_var_short()

    def _pvpNeutralElementReductionFunc(self, param1):
        self.pvpNeutralElementReduction = param1.read_var_short()

    def _pvpEarthElementReductionFunc(self, param1):
        self.pvpEarthElementReduction = param1.read_var_short()

    def _pvpWaterElementReductionFunc(self, param1):
        self.pvpWaterElementReduction = param1.read_var_short()

    def _pvpAirElementReductionFunc(self, param1):
        self.pvpAirElementReduction = param1.read_var_short()

    def _pvpFireElementReductionFunc(self, param1):
        self.pvpFireElementReduction = param1.read_var_short()

    def _dodgePALostProbabilityFunc(self, param1):
        self.dodgePALostProbability = param1.read_var_uh_short()
        if self.dodgePALostProbability < 0:
            raise RuntimeError("Forbidden value (" + str(self.dodgePALostProbability) + ") on element of GameFightMinimalStats.dodgePALostProbability.")

    def _dodgePMLostProbabilityFunc(self, param1):
        self.dodgePMLostProbability = param1.read_var_uh_short()
        if self.dodgePMLostProbability < 0:
            raise RuntimeError("Forbidden value (" + str(self.dodgePMLostProbability) + ") on element of GameFightMinimalStats.dodgePMLostProbability.")

    def _tackleBlockFunc(self, param1):
        self.tackleBlock = param1.read_var_short()

    def _tackleEvadeFunc(self, param1):
        self.tackleEvade = param1.read_var_short()

    def _fixedDamageReflectionFunc(self, param1):
        self.fixedDamageReflection = param1.read_var_short()

    def _invisibilityStateFunc(self, param1):
        self.invisibilityState = param1.read_byte()
        if self.invisibilityState < 0:
            raise RuntimeError("Forbidden value (" + str(self.invisibilityState) + ") on element of GameFightMinimalStats.invisibilityState.")

    def _meleeDamageReceivedPercentFunc(self, param1):
        self.meleeDamageReceivedPercent = param1.read_var_uh_short()
        if self.meleeDamageReceivedPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.meleeDamageReceivedPercent) + ") on element of GameFightMinimalStats.meleeDamageReceivedPercent.")

    def _rangedDamageReceivedPercentFunc(self, param1):
        self.rangedDamageReceivedPercent = param1.read_var_uh_short()
        if self.rangedDamageReceivedPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.rangedDamageReceivedPercent) + ") on element of GameFightMinimalStats.rangedDamageReceivedPercent.")

    def _weaponDamageReceivedPercentFunc(self, param1):
        self.weaponDamageReceivedPercent = param1.read_var_uh_short()
        if self.weaponDamageReceivedPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.weaponDamageReceivedPercent) + ") on element of GameFightMinimalStats.weaponDamageReceivedPercent.")

    def _spellDamageReceivedPercentFunc(self, param1):
        self.spellDamageReceivedPercent = param1.read_var_uh_short()
        if self.spellDamageReceivedPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellDamageReceivedPercent) + ") on element of GameFightMinimalStats.spellDamageReceivedPercent.")


class GameFightResumeSlaveInfo():
    protocolId = 364

    def __init__(self):
        super().__init__()
        self.slaveId = 0
        self.spellCooldowns = []
        self.summonCount = 0
        self.bombCount = 0
        self._spellCooldownstree = FuncTree()

    def getTypeId(self):
        return 364

    def initGameFightResumeSlaveInfo(self, param1=0, param2=[], param3=0, param4=0):
        self.slaveId = param1
        self.spellCooldowns = param2
        self.summonCount = param3
        self.bombCount = param4
        return self

    def reset(self):
        self.slaveId = 0
        self.spellCooldowns = []
        self.summonCount = 0
        self.bombCount = 0

    def serialize(self, param1):
        self.serializeAs_GameFightResumeSlaveInfo(param1)

    def serializeAs_GameFightResumeSlaveInfo(self, param1):
        if self.slaveId < -9007199254740990 or self.slaveId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.slaveId) + ") on element slaveId.")
        param1.write_double(self.slaveId)
        param1.write_short(len(self.spellCooldowns))
        _loc2_ = 0
        while _loc2_ < len(self.spellCooldowns):
            as_parent(self.spellCooldowns[_loc2_], GameFightSpellCooldown).serializeAs_GameFightSpellCooldown(param1)
            _loc2_ += 1
        if self.summonCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.summonCount) + ") on element summonCount.")
        param1.write_byte(self.summonCount)
        if self.bombCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.bombCount) + ") on element bombCount.")
        param1.write_byte(self.bombCount)

    def deserialize(self, param1):
        self.deserializeAs_GameFightResumeSlaveInfo(param1)

    def deserializeAs_GameFightResumeSlaveInfo(self, param1):
        _loc4_ = None
        self._slaveIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = GameFightSpellCooldown()
            _loc4_.deserialize(param1)
            self.spellCooldowns.append(_loc4_)
            _loc3_ += 1
        self._summonCountFunc(param1)
        self._bombCountFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightResumeSlaveInfo(param1)

    def deserializeAsyncAs_GameFightResumeSlaveInfo(self, param1):
        param1.add_child(self._slaveIdFunc)
        self._spellCooldownstree = param1.add_child(self._spellCooldownstreeFunc)
        param1.add_child(self._summonCountFunc)
        param1.add_child(self._bombCountFunc)

    def _slaveIdFunc(self, param1):
        self.slaveId = param1.read_double()
        if self.slaveId < -9007199254740990 or self.slaveId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.slaveId) + ") on element of GameFightResumeSlaveInfo.slaveId.")

    def _spellCooldownstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._spellCooldownstree.add_child(self._spellCooldownsFunc)
            _loc3_ += 1

    def _spellCooldownsFunc(self, param1):
        _loc2_ = GameFightSpellCooldown()
        _loc2_.deserialize(param1)
        self.spellCooldowns.append(_loc2_)

    def _summonCountFunc(self, param1):
        self.summonCount = param1.read_byte()
        if self.summonCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.summonCount) + ") on element of GameFightResumeSlaveInfo.summonCount.")

    def _bombCountFunc(self, param1):
        self.bombCount = param1.read_byte()
        if self.bombCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.bombCount) + ") on element of GameFightResumeSlaveInfo.bombCount.")


class GameFightSpellCooldown():
    protocolId = 205

    def __init__(self):
        super().__init__()
        self.spellId = 0
        self.cooldown = 0

    def getTypeId(self):
        return 205

    def initGameFightSpellCooldown(self, param1=0, param2=0):
        self.spellId = param1
        self.cooldown = param2
        return self

    def reset(self):
        self.spellId = 0
        self.cooldown = 0

    def serialize(self, param1):
        self.serializeAs_GameFightSpellCooldown(param1)

    def serializeAs_GameFightSpellCooldown(self, param1):
        param1.write_int(self.spellId)
        if self.cooldown < 0:
            raise RuntimeError("Forbidden value (" + str(self.cooldown) + ") on element cooldown.")
        param1.write_byte(self.cooldown)

    def deserialize(self, param1):
        self.deserializeAs_GameFightSpellCooldown(param1)

    def deserializeAs_GameFightSpellCooldown(self, param1):
        self._spellIdFunc(param1)
        self._cooldownFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightSpellCooldown(param1)

    def deserializeAsyncAs_GameFightSpellCooldown(self, param1):
        param1.add_child(self._spellIdFunc)
        param1.add_child(self._cooldownFunc)

    def _spellIdFunc(self, param1):
        self.spellId = param1.read_int()

    def _cooldownFunc(self, param1):
        self.cooldown = param1.read_byte()
        if self.cooldown < 0:
            raise RuntimeError("Forbidden value (" + str(self.cooldown) + ") on element of GameFightSpellCooldown.cooldown.")


class AlternativeMonstersInGroupLightInformations():
    protocolId = 394

    def __init__(self):
        super().__init__()
        self.playerCount = 0
        self.monsters = []
        self._monsterstree = FuncTree()

    def getTypeId(self):
        return 394

    def initAlternativeMonstersInGroupLightInformations(self, param1=0, param2=[]):
        self.playerCount = param1
        self.monsters = param2
        return self

    def reset(self):
        self.playerCount = 0
        self.monsters = []

    def serialize(self, param1):
        self.serializeAs_AlternativeMonstersInGroupLightInformations(param1)

    def serializeAs_AlternativeMonstersInGroupLightInformations(self, param1):
        param1.write_int(self.playerCount)
        param1.write_short(len(self.monsters))
        _loc2_ = 0
        while _loc2_ < len(self.monsters):
            as_parent(self.monsters[_loc2_], MonsterInGroupLightInformations).serializeAs_MonsterInGroupLightInformations(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_AlternativeMonstersInGroupLightInformations(param1)

    def deserializeAs_AlternativeMonstersInGroupLightInformations(self, param1):
        _loc4_ = None
        self._playerCountFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = MonsterInGroupLightInformations()
            _loc4_.deserialize(param1)
            self.monsters.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AlternativeMonstersInGroupLightInformations(param1)

    def deserializeAsyncAs_AlternativeMonstersInGroupLightInformations(self, param1):
        param1.add_child(self._playerCountFunc)
        self._monsterstree = param1.add_child(self._monsterstreeFunc)

    def _playerCountFunc(self, param1):
        self.playerCount = param1.read_int()

    def _monsterstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._monsterstree.add_child(self._monstersFunc)
            _loc3_ += 1

    def _monstersFunc(self, param1):
        _loc2_ = MonsterInGroupLightInformations()
        _loc2_.deserialize(param1)
        self.monsters.append(_loc2_)


class AtlasPointsInformations():
    protocolId = 175

    def __init__(self):
        super().__init__()
        self.type = 0
        self.coords = []
        self._coordstree = FuncTree()

    def getTypeId(self):
        return 175

    def initAtlasPointsInformations(self, param1=0, param2=[]):
        self.type = param1
        self.coords = param2
        return self

    def reset(self):
        self.type = 0
        self.coords = []

    def serialize(self, param1):
        self.serializeAs_AtlasPointsInformations(param1)

    def serializeAs_AtlasPointsInformations(self, param1):
        param1.write_byte(self.type)
        param1.write_short(len(self.coords))
        _loc2_ = 0
        while _loc2_ < len(self.coords):
            as_parent(self.coords[_loc2_], MapCoordinatesExtended).serializeAs_MapCoordinatesExtended(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_AtlasPointsInformations(param1)

    def deserializeAs_AtlasPointsInformations(self, param1):
        _loc4_ = None
        self._typeFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = MapCoordinatesExtended()
            _loc4_.deserialize(param1)
            self.coords.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AtlasPointsInformations(param1)

    def deserializeAsyncAs_AtlasPointsInformations(self, param1):
        param1.add_child(self._typeFunc)
        self._coordstree = param1.add_child(self._coordstreeFunc)

    def _typeFunc(self, param1):
        self.type = param1.read_byte()
        if self.type < 0:
            raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of AtlasPointsInformations.type.")

    def _coordstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._coordstree.add_child(self._coordsFunc)
            _loc3_ += 1

    def _coordsFunc(self, param1):
        _loc2_ = MapCoordinatesExtended()
        _loc2_.deserialize(param1)
        self.coords.append(_loc2_)


class GroupMonsterStaticInformations():
    protocolId = 140

    def __init__(self):
        super().__init__()
        self.mainCreatureLightInfos = MonsterInGroupLightInformations()
        self.underlings = []
        self._mainCreatureLightInfostree = FuncTree()
        self._underlingstree = FuncTree()

    def getTypeId(self):
        return 140

    def initGroupMonsterStaticInformations(self, param1=None, param2=[]):
        self.mainCreatureLightInfos = param1
        self.underlings = param2
        return self

    def reset(self):
        self.mainCreatureLightInfos = MonsterInGroupLightInformations()

    def serialize(self, param1):
        self.serializeAs_GroupMonsterStaticInformations(param1)

    def serializeAs_GroupMonsterStaticInformations(self, param1):
        self.mainCreatureLightInfos.serializeAs_MonsterInGroupLightInformations(param1)
        param1.write_short(len(self.underlings))
        _loc2_ = 0
        while _loc2_ < len(self.underlings):
            as_parent(self.underlings[_loc2_], MonsterInGroupInformations).serializeAs_MonsterInGroupInformations(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_GroupMonsterStaticInformations(param1)

    def deserializeAs_GroupMonsterStaticInformations(self, param1):
        _loc4_ = None
        self.mainCreatureLightInfos = MonsterInGroupLightInformations()
        self.mainCreatureLightInfos.deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = MonsterInGroupInformations()
            _loc4_.deserialize(param1)
            self.underlings.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GroupMonsterStaticInformations(param1)

    def deserializeAsyncAs_GroupMonsterStaticInformations(self, param1):
        self._mainCreatureLightInfostree = param1.add_child(self._mainCreatureLightInfostreeFunc)
        self._underlingstree = param1.add_child(self._underlingstreeFunc)

    def _mainCreatureLightInfostreeFunc(self, param1):
        self.mainCreatureLightInfos = MonsterInGroupLightInformations()
        self.mainCreatureLightInfos.deserializeAsync(self._mainCreatureLightInfostree)

    def _underlingstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._underlingstree.add_child(self._underlingsFunc)
            _loc3_ += 1

    def _underlingsFunc(self, param1):
        _loc2_ = MonsterInGroupInformations()
        _loc2_.deserialize(param1)
        self.underlings.append(_loc2_)


class HumanInformations():
    protocolId = 157

    def __init__(self):
        super().__init__()
        self.restrictions = ActorRestrictionsInformations()
        self.sex = False
        self.options = []
        self._restrictionstree = FuncTree()
        self._optionstree = FuncTree()

    def getTypeId(self):
        return 157

    def initHumanInformations(self, param1=None, param2=False, param3=[]):
        self.restrictions = param1
        self.sex = param2
        self.options = param3
        return self

    def reset(self):
        self.restrictions = ActorRestrictionsInformations()
        self.options = []

    def serialize(self, param1):
        self.serializeAs_HumanInformations(param1)

    def serializeAs_HumanInformations(self, param1):
        self.restrictions.serializeAs_ActorRestrictionsInformations(param1)
        param1.write_boolean(self.sex)
        param1.write_short(len(self.options))
        _loc2_ = 0
        while _loc2_ < len(self.options):
            param1.write_short(as_parent(self.options[_loc2_], HumanOption).getTypeId())
            as_parent(self.options[_loc2_], HumanOption).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_HumanInformations(param1)

    def deserializeAs_HumanInformations(self, param1):
        _loc4_ = 0
        _loc5_ = None
        self.restrictions = ActorRestrictionsInformations()
        self.restrictions.deserialize(param1)
        self._sexFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(HumanOption,_loc4_)
            _loc5_.deserialize(param1)
            self.options.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanInformations(param1)

    def deserializeAsyncAs_HumanInformations(self, param1):
        self._restrictionstree = param1.add_child(self._restrictionstreeFunc)
        param1.add_child(self._sexFunc)
        self._optionstree = param1.add_child(self._optionstreeFunc)

    def _restrictionstreeFunc(self, param1):
        self.restrictions = ActorRestrictionsInformations()
        self.restrictions.deserializeAsync(self._restrictionstree)

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()

    def _optionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._optionstree.add_child(self._optionsFunc)
            _loc3_ += 1

    def _optionsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(HumanOption,_loc2_)
        _loc3_.deserialize(param1)
        self.options.append(_loc3_)


class HumanOption():
    protocolId = 406

    def getTypeId(self):
        return 406

    def initHumanOption(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_HumanOption(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_HumanOption(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_HumanOption(self, param1):
        pass


class MonsterBoosts():
    protocolId = 497

    def __init__(self):
        super().__init__()
        self.id = 0
        self.xpBoost = 0
        self.dropBoost = 0

    def getTypeId(self):
        return 497

    def initMonsterBoosts(self, param1=0, param2=0, param3=0):
        self.id = param1
        self.xpBoost = param2
        self.dropBoost = param3
        return self

    def reset(self):
        self.id = 0
        self.xpBoost = 0
        self.dropBoost = 0

    def serialize(self, param1):
        self.serializeAs_MonsterBoosts(param1)

    def serializeAs_MonsterBoosts(self, param1):
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_var_int(self.id)
        if self.xpBoost < 0:
            raise RuntimeError("Forbidden value (" + str(self.xpBoost) + ") on element xpBoost.")
        param1.write_var_short(self.xpBoost)
        if self.dropBoost < 0:
            raise RuntimeError("Forbidden value (" + str(self.dropBoost) + ") on element dropBoost.")
        param1.write_var_short(self.dropBoost)

    def deserialize(self, param1):
        self.deserializeAs_MonsterBoosts(param1)

    def deserializeAs_MonsterBoosts(self, param1):
        self._idFunc(param1)
        self._xpBoostFunc(param1)
        self._dropBoostFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MonsterBoosts(param1)

    def deserializeAsyncAs_MonsterBoosts(self, param1):
        param1.add_child(self._idFunc)
        param1.add_child(self._xpBoostFunc)
        param1.add_child(self._dropBoostFunc)

    def _idFunc(self, param1):
        self.id = param1.read_var_uh_int()
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of MonsterBoosts.id.")

    def _xpBoostFunc(self, param1):
        self.xpBoost = param1.read_var_uh_short()
        if self.xpBoost < 0:
            raise RuntimeError("Forbidden value (" + str(self.xpBoost) + ") on element of MonsterBoosts.xpBoost.")

    def _dropBoostFunc(self, param1):
        self.dropBoost = param1.read_var_uh_short()
        if self.dropBoost < 0:
            raise RuntimeError("Forbidden value (" + str(self.dropBoost) + ") on element of MonsterBoosts.dropBoost.")


class MonsterInGroupLightInformations():
    protocolId = 395

    def __init__(self):
        super().__init__()
        self.creatureGenericId = 0
        self.grade = 0

    def getTypeId(self):
        return 395

    def initMonsterInGroupLightInformations(self, param1=0, param2=0):
        self.creatureGenericId = param1
        self.grade = param2
        return self

    def reset(self):
        self.creatureGenericId = 0
        self.grade = 0

    def serialize(self, param1):
        self.serializeAs_MonsterInGroupLightInformations(param1)

    def serializeAs_MonsterInGroupLightInformations(self, param1):
        param1.write_int(self.creatureGenericId)
        if self.grade < 0:
            raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element grade.")
        param1.write_byte(self.grade)

    def deserialize(self, param1):
        self.deserializeAs_MonsterInGroupLightInformations(param1)

    def deserializeAs_MonsterInGroupLightInformations(self, param1):
        self._creatureGenericIdFunc(param1)
        self._gradeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MonsterInGroupLightInformations(param1)

    def deserializeAsyncAs_MonsterInGroupLightInformations(self, param1):
        param1.add_child(self._creatureGenericIdFunc)
        param1.add_child(self._gradeFunc)

    def _creatureGenericIdFunc(self, param1):
        self.creatureGenericId = param1.read_int()

    def _gradeFunc(self, param1):
        self.grade = param1.read_byte()
        if self.grade < 0:
            raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element of MonsterInGroupLightInformations.grade.")


class ObjectItemInRolePlay():
    protocolId = 198

    def __init__(self):
        super().__init__()
        self.cellId = 0
        self.objectGID = 0

    def getTypeId(self):
        return 198

    def initObjectItemInRolePlay(self, param1=0, param2=0):
        self.cellId = param1
        self.objectGID = param2
        return self

    def reset(self):
        self.cellId = 0
        self.objectGID = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemInRolePlay(param1)

    def serializeAs_ObjectItemInRolePlay(self, param1):
        if self.cellId < 0 or self.cellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element cellId.")
        param1.write_var_short(self.cellId)
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element objectGID.")
        param1.write_var_short(self.objectGID)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemInRolePlay(param1)

    def deserializeAs_ObjectItemInRolePlay(self, param1):
        self._cellIdFunc(param1)
        self._objectGIDFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemInRolePlay(param1)

    def deserializeAsyncAs_ObjectItemInRolePlay(self, param1):
        param1.add_child(self._cellIdFunc)
        param1.add_child(self._objectGIDFunc)

    def _cellIdFunc(self, param1):
        self.cellId = param1.read_var_uh_short()
        if self.cellId < 0 or self.cellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of ObjectItemInRolePlay.cellId.")

    def _objectGIDFunc(self, param1):
        self.objectGID = param1.read_var_uh_short()
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItemInRolePlay.objectGID.")


class ArenaRankInfos():
    protocolId = 499

    def __init__(self):
        super().__init__()
        self.rank = 0
        self.bestRank = 0
        self.victoryCount = 0
        self.fightcount = 0

    def getTypeId(self):
        return 499

    def initArenaRankInfos(self, param1=0, param2=0, param3=0, param4=0):
        self.rank = param1
        self.bestRank = param2
        self.victoryCount = param3
        self.fightcount = param4
        return self

    def reset(self):
        self.rank = 0
        self.bestRank = 0
        self.victoryCount = 0
        self.fightcount = 0

    def serialize(self, param1):
        self.serializeAs_ArenaRankInfos(param1)

    def serializeAs_ArenaRankInfos(self, param1):
        if self.rank < 0 or self.rank > 20000:
            raise RuntimeError("Forbidden value (" + str(self.rank) + ") on element rank.")
        param1.write_var_short(self.rank)
        if self.bestRank < 0 or self.bestRank > 20000:
            raise RuntimeError("Forbidden value (" + str(self.bestRank) + ") on element bestRank.")
        param1.write_var_short(self.bestRank)
        if self.victoryCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.victoryCount) + ") on element victoryCount.")
        param1.write_var_short(self.victoryCount)
        if self.fightcount < 0:
            raise RuntimeError("Forbidden value (" + str(self.fightcount) + ") on element fightcount.")
        param1.write_var_short(self.fightcount)

    def deserialize(self, param1):
        self.deserializeAs_ArenaRankInfos(param1)

    def deserializeAs_ArenaRankInfos(self, param1):
        self._rankFunc(param1)
        self._bestRankFunc(param1)
        self._victoryCountFunc(param1)
        self._fightcountFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ArenaRankInfos(param1)

    def deserializeAsyncAs_ArenaRankInfos(self, param1):
        param1.add_child(self._rankFunc)
        param1.add_child(self._bestRankFunc)
        param1.add_child(self._victoryCountFunc)
        param1.add_child(self._fightcountFunc)

    def _rankFunc(self, param1):
        self.rank = param1.read_var_uh_short()
        if self.rank < 0 or self.rank > 20000:
            raise RuntimeError("Forbidden value (" + str(self.rank) + ") on element of ArenaRankInfos.rank.")

    def _bestRankFunc(self, param1):
        self.bestRank = param1.read_var_uh_short()
        if self.bestRank < 0 or self.bestRank > 20000:
            raise RuntimeError("Forbidden value (" + str(self.bestRank) + ") on element of ArenaRankInfos.bestRank.")

    def _victoryCountFunc(self, param1):
        self.victoryCount = param1.read_var_uh_short()
        if self.victoryCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.victoryCount) + ") on element of ArenaRankInfos.victoryCount.")

    def _fightcountFunc(self, param1):
        self.fightcount = param1.read_var_uh_short()
        if self.fightcount < 0:
            raise RuntimeError("Forbidden value (" + str(self.fightcount) + ") on element of ArenaRankInfos.fightcount.")


class DecraftedItemStackInfo():
    protocolId = 481

    def __init__(self):
        super().__init__()
        self.objectUID = 0
        self.bonusMin = 0
        self.bonusMax = 0
        self.runesId = []
        self.runesQty = []
        self._runesIdtree = FuncTree()
        self._runesQtytree = FuncTree()

    def getTypeId(self):
        return 481

    def initDecraftedItemStackInfo(self, param1=0, param2=0, param3=0, param4=[], param5=[]):
        self.objectUID = param1
        self.bonusMin = param2
        self.bonusMax = param3
        self.runesId = param4
        self.runesQty = param5
        return self

    def reset(self):
        self.objectUID = 0
        self.bonusMin = 0
        self.bonusMax = 0
        self.runesId = []
        self.runesQty = []

    def serialize(self, param1):
        self.serializeAs_DecraftedItemStackInfo(param1)

    def serializeAs_DecraftedItemStackInfo(self, param1):
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element objectUID.")
        param1.write_var_int(self.objectUID)
        param1.write_float(self.bonusMin)
        param1.write_float(self.bonusMax)
        param1.write_short(len(self.runesId))
        _loc2_ = 0
        while _loc2_ < len(self.runesId):
            if self.runesId[_loc2_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.runesId[_loc2_]) + ") on element 4 (starting at 1) of runesId.")
            param1.write_var_short(self.runesId[_loc2_])
            _loc2_ += 1
        param1.write_short(len(self.runesQty))
        _loc3_ = 0
        while _loc3_ < len(self.runesQty):
            if self.runesQty[_loc3_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.runesQty[_loc3_]) + ") on element 5 (starting at 1) of runesQty.")
            param1.write_var_int(self.runesQty[_loc3_])
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_DecraftedItemStackInfo(param1)

    def deserializeAs_DecraftedItemStackInfo(self, param1):
        _loc6_ = 0
        _loc7_ = 0
        self._objectUIDFunc(param1)
        self._bonusMinFunc(param1)
        self._bonusMaxFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_var_uh_short()
            if _loc6_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc6_) + ") on elements of runesId.")
            self.runesId.append(_loc6_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc7_ = param1.read_var_uh_int()
            if _loc7_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc7_) + ") on elements of runesQty.")
            self.runesQty.append(_loc7_)
            _loc5_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_DecraftedItemStackInfo(param1)

    def deserializeAsyncAs_DecraftedItemStackInfo(self, param1):
        param1.add_child(self._objectUIDFunc)
        param1.add_child(self._bonusMinFunc)
        param1.add_child(self._bonusMaxFunc)
        self._runesIdtree = param1.add_child(self._runesIdtreeFunc)
        self._runesQtytree = param1.add_child(self._runesQtytreeFunc)

    def _objectUIDFunc(self, param1):
        self.objectUID = param1.read_var_uh_int()
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of DecraftedItemStackInfo.objectUID.")

    def _bonusMinFunc(self, param1):
        self.bonusMin = param1.read_float()

    def _bonusMaxFunc(self, param1):
        self.bonusMax = param1.read_float()

    def _runesIdtreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._runesIdtree.add_child(self._runesIdFunc)
            _loc3_ += 1

    def _runesIdFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of runesId.")
        self.runesId.append(_loc2_)

    def _runesQtytreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._runesQtytree.add_child(self._runesQtyFunc)
            _loc3_ += 1

    def _runesQtyFunc(self, param1):
        _loc2_ = param1.read_var_uh_int()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of runesQty.")
        self.runesQty.append(_loc2_)


class JobBookSubscription():
    protocolId = 500

    def __init__(self):
        super().__init__()
        self.jobId = 0
        self.subscribed = False

    def getTypeId(self):
        return 500

    def initJobBookSubscription(self, param1=0, param2=False):
        self.jobId = param1
        self.subscribed = param2
        return self

    def reset(self):
        self.jobId = 0
        self.subscribed = False

    def serialize(self, param1):
        self.serializeAs_JobBookSubscription(param1)

    def serializeAs_JobBookSubscription(self, param1):
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element jobId.")
        param1.write_byte(self.jobId)
        param1.write_boolean(self.subscribed)

    def deserialize(self, param1):
        self.deserializeAs_JobBookSubscription(param1)

    def deserializeAs_JobBookSubscription(self, param1):
        self._jobIdFunc(param1)
        self._subscribedFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_JobBookSubscription(param1)

    def deserializeAsyncAs_JobBookSubscription(self, param1):
        param1.add_child(self._jobIdFunc)
        param1.add_child(self._subscribedFunc)

    def _jobIdFunc(self, param1):
        self.jobId = param1.read_byte()
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobBookSubscription.jobId.")

    def _subscribedFunc(self, param1):
        self.subscribed = param1.read_boolean()


class JobCrafterDirectoryEntryJobInfo():
    protocolId = 195

    def __init__(self):
        super().__init__()
        self.jobId = 0
        self.jobLevel = 0
        self.free = False
        self.minLevel = 0

    def getTypeId(self):
        return 195

    def initJobCrafterDirectoryEntryJobInfo(self, param1=0, param2=0, param3=False, param4=0):
        self.jobId = param1
        self.jobLevel = param2
        self.free = param3
        self.minLevel = param4
        return self

    def reset(self):
        self.jobId = 0
        self.jobLevel = 0
        self.free = False
        self.minLevel = 0

    def serialize(self, param1):
        self.serializeAs_JobCrafterDirectoryEntryJobInfo(param1)

    def serializeAs_JobCrafterDirectoryEntryJobInfo(self, param1):
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element jobId.")
        param1.write_byte(self.jobId)
        if self.jobLevel < 1 or self.jobLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.jobLevel) + ") on element jobLevel.")
        param1.write_byte(self.jobLevel)
        param1.write_boolean(self.free)
        if self.minLevel < 0 or self.minLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.minLevel) + ") on element minLevel.")
        param1.write_byte(self.minLevel)

    def deserialize(self, param1):
        self.deserializeAs_JobCrafterDirectoryEntryJobInfo(param1)

    def deserializeAs_JobCrafterDirectoryEntryJobInfo(self, param1):
        self._jobIdFunc(param1)
        self._jobLevelFunc(param1)
        self._freeFunc(param1)
        self._minLevelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_JobCrafterDirectoryEntryJobInfo(param1)

    def deserializeAsyncAs_JobCrafterDirectoryEntryJobInfo(self, param1):
        param1.add_child(self._jobIdFunc)
        param1.add_child(self._jobLevelFunc)
        param1.add_child(self._freeFunc)
        param1.add_child(self._minLevelFunc)

    def _jobIdFunc(self, param1):
        self.jobId = param1.read_byte()
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobCrafterDirectoryEntryJobInfo.jobId.")

    def _jobLevelFunc(self, param1):
        self.jobLevel = param1.read_unsigned_byte()
        if self.jobLevel < 1 or self.jobLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.jobLevel) + ") on element of JobCrafterDirectoryEntryJobInfo.jobLevel.")

    def _freeFunc(self, param1):
        self.free = param1.read_boolean()

    def _minLevelFunc(self, param1):
        self.minLevel = param1.read_unsigned_byte()
        if self.minLevel < 0 or self.minLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.minLevel) + ") on element of JobCrafterDirectoryEntryJobInfo.minLevel.")


class JobCrafterDirectoryEntryPlayerInfo():
    protocolId = 194

    def __init__(self):
        super().__init__()
        self.playerId = 0
        self.playerName = ""
        self.alignmentSide = 0
        self.breed = 0
        self.sex = False
        self.isInWorkshop = False
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.status = PlayerStatus()
        self._statustree = FuncTree()

    def getTypeId(self):
        return 194

    def initJobCrafterDirectoryEntryPlayerInfo(self, param1=0, param2="", param3=0, param4=0, param5=False, param6=False, param7=0, param8=0, param9=0, param10=0, param11=None):
        self.playerId = param1
        self.playerName = param2
        self.alignmentSide = param3
        self.breed = param4
        self.sex = param5
        self.isInWorkshop = param6
        self.worldX = param7
        self.worldY = param8
        self.mapId = param9
        self.subAreaId = param10
        self.status = param11
        return self

    def reset(self):
        self.playerId = 0
        self.playerName = ""
        self.alignmentSide = 0
        self.breed = 0
        self.sex = False
        self.isInWorkshop = False
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.status = PlayerStatus()

    def serialize(self, param1):
        self.serializeAs_JobCrafterDirectoryEntryPlayerInfo(param1)

    def serializeAs_JobCrafterDirectoryEntryPlayerInfo(self, param1):
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element playerId.")
        param1.write_var_long(self.playerId)
        param1.write_utf(self.playerName)
        param1.write_byte(self.alignmentSide)
        param1.write_byte(self.breed)
        param1.write_boolean(self.sex)
        param1.write_boolean(self.isInWorkshop)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        param1.write_short(self.status.getTypeId())
        self.status.serialize(param1)

    def deserialize(self, param1):
        self.deserializeAs_JobCrafterDirectoryEntryPlayerInfo(param1)

    def deserializeAs_JobCrafterDirectoryEntryPlayerInfo(self, param1):
        self._playerIdFunc(param1)
        self._playerNameFunc(param1)
        self._alignmentSideFunc(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)
        self._isInWorkshopFunc(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_JobCrafterDirectoryEntryPlayerInfo(param1)

    def deserializeAsyncAs_JobCrafterDirectoryEntryPlayerInfo(self, param1):
        param1.add_child(self._playerIdFunc)
        param1.add_child(self._playerNameFunc)
        param1.add_child(self._alignmentSideFunc)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)
        param1.add_child(self._isInWorkshopFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)
        self._statustree = param1.add_child(self._statustreeFunc)

    def _playerIdFunc(self, param1):
        self.playerId = param1.read_var_uh_long()
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of JobCrafterDirectoryEntryPlayerInfo.playerId.")

    def _playerNameFunc(self, param1):
        self.playerName = param1.read_utf()

    def _alignmentSideFunc(self, param1):
        self.alignmentSide = param1.read_byte()

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()
        if self.breed < PlayableBreedEnum.Feca or self.breed > PlayableBreedEnum.Ouginak:
            raise RuntimeError("Forbidden value (" + str(self.breed) + ") on element of JobCrafterDirectoryEntryPlayerInfo.breed.")

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()

    def _isInWorkshopFunc(self, param1):
        self.isInWorkshop = param1.read_boolean()

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of JobCrafterDirectoryEntryPlayerInfo.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of JobCrafterDirectoryEntryPlayerInfo.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of JobCrafterDirectoryEntryPlayerInfo.subAreaId.")

    def _statustreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserializeAsync(self._statustree)


class JobCrafterDirectoryListEntry():
    protocolId = 196

    def __init__(self):
        super().__init__()
        self.playerInfo = JobCrafterDirectoryEntryPlayerInfo()
        self.jobInfo = JobCrafterDirectoryEntryJobInfo()
        self._playerInfotree = FuncTree()
        self._jobInfotree = FuncTree()

    def getTypeId(self):
        return 196

    def initJobCrafterDirectoryListEntry(self, param1=None, param2=None):
        self.playerInfo = param1
        self.jobInfo = param2
        return self

    def reset(self):
        self.playerInfo = JobCrafterDirectoryEntryPlayerInfo()

    def serialize(self, param1):
        self.serializeAs_JobCrafterDirectoryListEntry(param1)

    def serializeAs_JobCrafterDirectoryListEntry(self, param1):
        self.playerInfo.serializeAs_JobCrafterDirectoryEntryPlayerInfo(param1)
        self.jobInfo.serializeAs_JobCrafterDirectoryEntryJobInfo(param1)

    def deserialize(self, param1):
        self.deserializeAs_JobCrafterDirectoryListEntry(param1)

    def deserializeAs_JobCrafterDirectoryListEntry(self, param1):
        self.playerInfo = JobCrafterDirectoryEntryPlayerInfo()
        self.playerInfo.deserialize(param1)
        self.jobInfo = JobCrafterDirectoryEntryJobInfo()
        self.jobInfo.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_JobCrafterDirectoryListEntry(param1)

    def deserializeAsyncAs_JobCrafterDirectoryListEntry(self, param1):
        self._playerInfotree = param1.add_child(self._playerInfotreeFunc)
        self._jobInfotree = param1.add_child(self._jobInfotreeFunc)

    def _playerInfotreeFunc(self, param1):
        self.playerInfo = JobCrafterDirectoryEntryPlayerInfo()
        self.playerInfo.deserializeAsync(self._playerInfotree)

    def _jobInfotreeFunc(self, param1):
        self.jobInfo = JobCrafterDirectoryEntryJobInfo()
        self.jobInfo.deserializeAsync(self._jobInfotree)


class JobCrafterDirectorySettings():
    protocolId = 97

    def __init__(self):
        super().__init__()
        self.jobId = 0
        self.minLevel = 0
        self.free = False

    def getTypeId(self):
        return 97

    def initJobCrafterDirectorySettings(self, param1=0, param2=0, param3=False):
        self.jobId = param1
        self.minLevel = param2
        self.free = param3
        return self

    def reset(self):
        self.jobId = 0
        self.minLevel = 0
        self.free = False

    def serialize(self, param1):
        self.serializeAs_JobCrafterDirectorySettings(param1)

    def serializeAs_JobCrafterDirectorySettings(self, param1):
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element jobId.")
        param1.write_byte(self.jobId)
        if self.minLevel < 0 or self.minLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.minLevel) + ") on element minLevel.")
        param1.write_byte(self.minLevel)
        param1.write_boolean(self.free)

    def deserialize(self, param1):
        self.deserializeAs_JobCrafterDirectorySettings(param1)

    def deserializeAs_JobCrafterDirectorySettings(self, param1):
        self._jobIdFunc(param1)
        self._minLevelFunc(param1)
        self._freeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_JobCrafterDirectorySettings(param1)

    def deserializeAsyncAs_JobCrafterDirectorySettings(self, param1):
        param1.add_child(self._jobIdFunc)
        param1.add_child(self._minLevelFunc)
        param1.add_child(self._freeFunc)

    def _jobIdFunc(self, param1):
        self.jobId = param1.read_byte()
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobCrafterDirectorySettings.jobId.")

    def _minLevelFunc(self, param1):
        self.minLevel = param1.read_unsigned_byte()
        if self.minLevel < 0 or self.minLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.minLevel) + ") on element of JobCrafterDirectorySettings.minLevel.")

    def _freeFunc(self, param1):
        self.free = param1.read_boolean()


class JobDescription():
    protocolId = 101

    def __init__(self):
        super().__init__()
        self.jobId = 0
        self.skills = []
        self._skillstree = FuncTree()

    def getTypeId(self):
        return 101

    def initJobDescription(self, param1=0, param2=[]):
        self.jobId = param1
        self.skills = param2
        return self

    def reset(self):
        self.jobId = 0
        self.skills = []

    def serialize(self, param1):
        self.serializeAs_JobDescription(param1)

    def serializeAs_JobDescription(self, param1):
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element jobId.")
        param1.write_byte(self.jobId)
        param1.write_short(len(self.skills))
        _loc2_ = 0
        while _loc2_ < len(self.skills):
            param1.write_short(as_parent(self.skills[_loc2_], SkillActionDescription).getTypeId())
            as_parent(self.skills[_loc2_], SkillActionDescription).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_JobDescription(param1)

    def deserializeAs_JobDescription(self, param1):
        _loc4_ = 0
        _loc5_ = None
        self._jobIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(SkillActionDescription,_loc4_)
            _loc5_.deserialize(param1)
            self.skills.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_JobDescription(param1)

    def deserializeAsyncAs_JobDescription(self, param1):
        param1.add_child(self._jobIdFunc)
        self._skillstree = param1.add_child(self._skillstreeFunc)

    def _jobIdFunc(self, param1):
        self.jobId = param1.read_byte()
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobDescription.jobId.")

    def _skillstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._skillstree.add_child(self._skillsFunc)
            _loc3_ += 1

    def _skillsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(SkillActionDescription,_loc2_)
        _loc3_.deserialize(param1)
        self.skills.append(_loc3_)


class JobExperience():
    protocolId = 98

    def __init__(self):
        super().__init__()
        self.jobId = 0
        self.jobLevel = 0
        self.jobXP = 0
        self.jobXpLevelFloor = 0
        self.jobXpNextLevelFloor = 0

    def getTypeId(self):
        return 98

    def initJobExperience(self, param1=0, param2=0, param3=0, param4=0, param5=0):
        self.jobId = param1
        self.jobLevel = param2
        self.jobXP = param3
        self.jobXpLevelFloor = param4
        self.jobXpNextLevelFloor = param5
        return self

    def reset(self):
        self.jobId = 0
        self.jobLevel = 0
        self.jobXP = 0
        self.jobXpLevelFloor = 0
        self.jobXpNextLevelFloor = 0

    def serialize(self, param1):
        self.serializeAs_JobExperience(param1)

    def serializeAs_JobExperience(self, param1):
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element jobId.")
        param1.write_byte(self.jobId)
        if self.jobLevel < 0 or self.jobLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.jobLevel) + ") on element jobLevel.")
        param1.write_byte(self.jobLevel)
        if self.jobXP < 0 or self.jobXP > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.jobXP) + ") on element jobXP.")
        param1.write_var_long(self.jobXP)
        if self.jobXpLevelFloor < 0 or self.jobXpLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.jobXpLevelFloor) + ") on element jobXpLevelFloor.")
        param1.write_var_long(self.jobXpLevelFloor)
        if self.jobXpNextLevelFloor < 0 or self.jobXpNextLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.jobXpNextLevelFloor) + ") on element jobXpNextLevelFloor.")
        param1.write_var_long(self.jobXpNextLevelFloor)

    def deserialize(self, param1):
        self.deserializeAs_JobExperience(param1)

    def deserializeAs_JobExperience(self, param1):
        self._jobIdFunc(param1)
        self._jobLevelFunc(param1)
        self._jobXPFunc(param1)
        self._jobXpLevelFloorFunc(param1)
        self._jobXpNextLevelFloorFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_JobExperience(param1)

    def deserializeAsyncAs_JobExperience(self, param1):
        param1.add_child(self._jobIdFunc)
        param1.add_child(self._jobLevelFunc)
        param1.add_child(self._jobXPFunc)
        param1.add_child(self._jobXpLevelFloorFunc)
        param1.add_child(self._jobXpNextLevelFloorFunc)

    def _jobIdFunc(self, param1):
        self.jobId = param1.read_byte()
        if self.jobId < 0:
            raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobExperience.jobId.")

    def _jobLevelFunc(self, param1):
        self.jobLevel = param1.read_unsigned_byte()
        if self.jobLevel < 0 or self.jobLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.jobLevel) + ") on element of JobExperience.jobLevel.")

    def _jobXPFunc(self, param1):
        self.jobXP = param1.read_var_uh_long()
        if self.jobXP < 0 or self.jobXP > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.jobXP) + ") on element of JobExperience.jobXP.")

    def _jobXpLevelFloorFunc(self, param1):
        self.jobXpLevelFloor = param1.read_var_uh_long()
        if self.jobXpLevelFloor < 0 or self.jobXpLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.jobXpLevelFloor) + ") on element of JobExperience.jobXpLevelFloor.")

    def _jobXpNextLevelFloorFunc(self, param1):
        self.jobXpNextLevelFloor = param1.read_var_uh_long()
        if self.jobXpNextLevelFloor < 0 or self.jobXpNextLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.jobXpNextLevelFloor) + ") on element of JobExperience.jobXpNextLevelFloor.")


class DungeonPartyFinderPlayer():
    protocolId = 373

    def __init__(self):
        super().__init__()
        self.playerId = 0
        self.playerName = ""
        self.breed = 0
        self.sex = False
        self.level = 0

    def getTypeId(self):
        return 373

    def initDungeonPartyFinderPlayer(self, param1=0, param2="", param3=0, param4=False, param5=0):
        self.playerId = param1
        self.playerName = param2
        self.breed = param3
        self.sex = param4
        self.level = param5
        return self

    def reset(self):
        self.playerId = 0
        self.playerName = ""
        self.breed = 0
        self.sex = False
        self.level = 0

    def serialize(self, param1):
        self.serializeAs_DungeonPartyFinderPlayer(param1)

    def serializeAs_DungeonPartyFinderPlayer(self, param1):
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element playerId.")
        param1.write_var_long(self.playerId)
        param1.write_utf(self.playerName)
        param1.write_byte(self.breed)
        param1.write_boolean(self.sex)
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)

    def deserialize(self, param1):
        self.deserializeAs_DungeonPartyFinderPlayer(param1)

    def deserializeAs_DungeonPartyFinderPlayer(self, param1):
        self._playerIdFunc(param1)
        self._playerNameFunc(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)
        self._levelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_DungeonPartyFinderPlayer(param1)

    def deserializeAsyncAs_DungeonPartyFinderPlayer(self, param1):
        param1.add_child(self._playerIdFunc)
        param1.add_child(self._playerNameFunc)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)
        param1.add_child(self._levelFunc)

    def _playerIdFunc(self, param1):
        self.playerId = param1.read_var_uh_long()
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of DungeonPartyFinderPlayer.playerId.")

    def _playerNameFunc(self, param1):
        self.playerName = param1.read_utf()

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()
        if self.breed < PlayableBreedEnum.Feca or self.breed > PlayableBreedEnum.Ouginak:
            raise RuntimeError("Forbidden value (" + str(self.breed) + ") on element of DungeonPartyFinderPlayer.breed.")

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of DungeonPartyFinderPlayer.level.")


class NamedPartyTeam():
    protocolId = 469

    def __init__(self):
        super().__init__()
        self.teamId = 2
        self.partyName = ""

    def getTypeId(self):
        return 469

    def initNamedPartyTeam(self, param1=2, param2=""):
        self.teamId = param1
        self.partyName = param2
        return self

    def reset(self):
        self.teamId = 2
        self.partyName = ""

    def serialize(self, param1):
        self.serializeAs_NamedPartyTeam(param1)

    def serializeAs_NamedPartyTeam(self, param1):
        param1.write_byte(self.teamId)
        param1.write_utf(self.partyName)

    def deserialize(self, param1):
        self.deserializeAs_NamedPartyTeam(param1)

    def deserializeAs_NamedPartyTeam(self, param1):
        self._teamIdFunc(param1)
        self._partyNameFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_NamedPartyTeam(param1)

    def deserializeAsyncAs_NamedPartyTeam(self, param1):
        param1.add_child(self._teamIdFunc)
        param1.add_child(self._partyNameFunc)

    def _teamIdFunc(self, param1):
        self.teamId = param1.read_byte()
        if self.teamId < 0:
            raise RuntimeError("Forbidden value (" + str(self.teamId) + ") on element of NamedPartyTeam.teamId.")

    def _partyNameFunc(self, param1):
        self.partyName = param1.read_utf()


class NamedPartyTeamWithOutcome():
    protocolId = 470

    def __init__(self):
        super().__init__()
        self.team = NamedPartyTeam()
        self.outcome = 0
        self._teamtree = FuncTree()

    def getTypeId(self):
        return 470

    def initNamedPartyTeamWithOutcome(self, param1=None, param2=0):
        self.team = param1
        self.outcome = param2
        return self

    def reset(self):
        self.team = NamedPartyTeam()

    def serialize(self, param1):
        self.serializeAs_NamedPartyTeamWithOutcome(param1)

    def serializeAs_NamedPartyTeamWithOutcome(self, param1):
        self.team.serializeAs_NamedPartyTeam(param1)
        param1.write_var_short(self.outcome)

    def deserialize(self, param1):
        self.deserializeAs_NamedPartyTeamWithOutcome(param1)

    def deserializeAs_NamedPartyTeamWithOutcome(self, param1):
        self.team = NamedPartyTeam()
        self.team.deserialize(param1)
        self._outcomeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_NamedPartyTeamWithOutcome(param1)

    def deserializeAsyncAs_NamedPartyTeamWithOutcome(self, param1):
        self._teamtree = param1.add_child(self._teamtreeFunc)
        param1.add_child(self._outcomeFunc)

    def _teamtreeFunc(self, param1):
        self.team = NamedPartyTeam()
        self.team.deserializeAsync(self._teamtree)

    def _outcomeFunc(self, param1):
        self.outcome = param1.read_var_uh_short()
        if self.outcome < 0:
            raise RuntimeError("Forbidden value (" + str(self.outcome) + ") on element of NamedPartyTeamWithOutcome.outcome.")


class PartyGuestInformations():
    protocolId = 374

    def __init__(self):
        super().__init__()
        self.guestId = 0
        self.hostId = 0
        self.name = ""
        self.guestLook = EntityLook()
        self.breed = 0
        self.sex = False
        self.status = PlayerStatus()
        self.companions = []
        self._guestLooktree = FuncTree()
        self._statustree = FuncTree()
        self._companionstree = FuncTree()

    def getTypeId(self):
        return 374

    def initPartyGuestInformations(self, param1=0, param2=0, param3="", param4=None, param5=0, param6=False, param7=None, param8=[]):
        self.guestId = param1
        self.hostId = param2
        self.name = param3
        self.guestLook = param4
        self.breed = param5
        self.sex = param6
        self.status = param7
        self.companions = param8
        return self

    def reset(self):
        self.guestId = 0
        self.hostId = 0
        self.name = ""
        self.guestLook = EntityLook()
        self.sex = False
        self.status = PlayerStatus()

    def serialize(self, param1):
        self.serializeAs_PartyGuestInformations(param1)

    def serializeAs_PartyGuestInformations(self, param1):
        if self.guestId < 0 or self.guestId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.guestId) + ") on element guestId.")
        param1.write_var_long(self.guestId)
        if self.hostId < 0 or self.hostId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.hostId) + ") on element hostId.")
        param1.write_var_long(self.hostId)
        param1.write_utf(self.name)
        self.guestLook.serializeAs_EntityLook(param1)
        param1.write_byte(self.breed)
        param1.write_boolean(self.sex)
        param1.write_short(self.status.getTypeId())
        self.status.serialize(param1)
        param1.write_short(len(self.companions))
        _loc2_ = 0
        while _loc2_ < len(self.companions):
            as_parent(self.companions[_loc2_], PartyCompanionBaseInformations).serializeAs_PartyCompanionBaseInformations(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_PartyGuestInformations(param1)

    def deserializeAs_PartyGuestInformations(self, param1):
        _loc5_ = None
        self._guestIdFunc(param1)
        self._hostIdFunc(param1)
        self._nameFunc(param1)
        self.guestLook = EntityLook()
        self.guestLook.deserialize(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserialize(param1)
        _loc3_ = param1.read_unsigned_short()
        _loc4_ = 0
        while _loc4_ < _loc3_:
            _loc5_ = PartyCompanionBaseInformations()
            _loc5_.deserialize(param1)
            self.companions.append(_loc5_)
            _loc4_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PartyGuestInformations(param1)

    def deserializeAsyncAs_PartyGuestInformations(self, param1):
        param1.add_child(self._guestIdFunc)
        param1.add_child(self._hostIdFunc)
        param1.add_child(self._nameFunc)
        self._guestLooktree = param1.add_child(self._guestLooktreeFunc)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)
        self._statustree = param1.add_child(self._statustreeFunc)
        self._companionstree = param1.add_child(self._companionstreeFunc)

    def _guestIdFunc(self, param1):
        self.guestId = param1.read_var_uh_long()
        if self.guestId < 0 or self.guestId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.guestId) + ") on element of PartyGuestInformations.guestId.")

    def _hostIdFunc(self, param1):
        self.hostId = param1.read_var_uh_long()
        if self.hostId < 0 or self.hostId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.hostId) + ") on element of PartyGuestInformations.hostId.")

    def _nameFunc(self, param1):
        self.name = param1.read_utf()

    def _guestLooktreeFunc(self, param1):
        self.guestLook = EntityLook()
        self.guestLook.deserializeAsync(self._guestLooktree)

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()

    def _statustreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserializeAsync(self._statustree)

    def _companionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._companionstree.add_child(self._companionsFunc)
            _loc3_ += 1

    def _companionsFunc(self, param1):
        _loc2_ = PartyCompanionBaseInformations()
        _loc2_.deserialize(param1)
        self.companions.append(_loc2_)


class PartyMemberGeoPosition():
    protocolId = 378

    def __init__(self):
        super().__init__()
        self.memberId = 0
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0

    def getTypeId(self):
        return 378

    def initPartyMemberGeoPosition(self, param1=0, param2=0, param3=0, param4=0, param5=0):
        self.memberId = param1
        self.worldX = param2
        self.worldY = param3
        self.mapId = param4
        self.subAreaId = param5
        return self

    def reset(self):
        self.memberId = 0
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0

    def serialize(self, param1):
        self.serializeAs_PartyMemberGeoPosition(param1)

    def serializeAs_PartyMemberGeoPosition(self, param1):
        if self.memberId < 0:
            raise RuntimeError("Forbidden value (" + str(self.memberId) + ") on element memberId.")
        param1.write_int(self.memberId)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)

    def deserialize(self, param1):
        self.deserializeAs_PartyMemberGeoPosition(param1)

    def deserializeAs_PartyMemberGeoPosition(self, param1):
        self._memberIdFunc(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PartyMemberGeoPosition(param1)

    def deserializeAsyncAs_PartyMemberGeoPosition(self, param1):
        param1.add_child(self._memberIdFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)

    def _memberIdFunc(self, param1):
        self.memberId = param1.read_int()
        if self.memberId < 0:
            raise RuntimeError("Forbidden value (" + str(self.memberId) + ") on element of PartyMemberGeoPosition.memberId.")

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PartyMemberGeoPosition.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PartyMemberGeoPosition.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PartyMemberGeoPosition.subAreaId.")


class PartyCompanionBaseInformations():
    protocolId = 453

    def __init__(self):
        super().__init__()
        self.indexId = 0
        self.companionGenericId = 0
        self.entityLook = EntityLook()
        self._entityLooktree = FuncTree()

    def getTypeId(self):
        return 453

    def initPartyCompanionBaseInformations(self, param1=0, param2=0, param3=None):
        self.indexId = param1
        self.companionGenericId = param2
        self.entityLook = param3
        return self

    def reset(self):
        self.indexId = 0
        self.companionGenericId = 0
        self.entityLook = EntityLook()

    def serialize(self, param1):
        self.serializeAs_PartyCompanionBaseInformations(param1)

    def serializeAs_PartyCompanionBaseInformations(self, param1):
        if self.indexId < 0:
            raise RuntimeError("Forbidden value (" + str(self.indexId) + ") on element indexId.")
        param1.write_byte(self.indexId)
        if self.companionGenericId < 0:
            raise RuntimeError("Forbidden value (" + str(self.companionGenericId) + ") on element companionGenericId.")
        param1.write_byte(self.companionGenericId)
        self.entityLook.serializeAs_EntityLook(param1)

    def deserialize(self, param1):
        self.deserializeAs_PartyCompanionBaseInformations(param1)

    def deserializeAs_PartyCompanionBaseInformations(self, param1):
        self._indexIdFunc(param1)
        self._companionGenericIdFunc(param1)
        self.entityLook = EntityLook()
        self.entityLook.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PartyCompanionBaseInformations(param1)

    def deserializeAsyncAs_PartyCompanionBaseInformations(self, param1):
        param1.add_child(self._indexIdFunc)
        param1.add_child(self._companionGenericIdFunc)
        self._entityLooktree = param1.add_child(self._entityLooktreeFunc)

    def _indexIdFunc(self, param1):
        self.indexId = param1.read_byte()
        if self.indexId < 0:
            raise RuntimeError("Forbidden value (" + str(self.indexId) + ") on element of PartyCompanionBaseInformations.indexId.")

    def _companionGenericIdFunc(self, param1):
        self.companionGenericId = param1.read_byte()
        if self.companionGenericId < 0:
            raise RuntimeError("Forbidden value (" + str(self.companionGenericId) + ") on element of PartyCompanionBaseInformations.companionGenericId.")

    def _entityLooktreeFunc(self, param1):
        self.entityLook = EntityLook()
        self.entityLook.deserializeAsync(self._entityLooktree)


class GameRolePlayNpcQuestFlag():
    protocolId = 384

    def __init__(self):
        super().__init__()
        self.questsToValidId = []
        self.questsToStartId = []
        self._questsToValidIdtree = FuncTree()
        self._questsToStartIdtree = FuncTree()

    def getTypeId(self):
        return 384

    def initGameRolePlayNpcQuestFlag(self, param1=[], param2=[]):
        self.questsToValidId = param1
        self.questsToStartId = param2
        return self

    def reset(self):
        self.questsToValidId = []
        self.questsToStartId = []

    def serialize(self, param1):
        self.serializeAs_GameRolePlayNpcQuestFlag(param1)

    def serializeAs_GameRolePlayNpcQuestFlag(self, param1):
        param1.write_short(len(self.questsToValidId))
        _loc2_ = 0
        while _loc2_ < len(self.questsToValidId):
            if self.questsToValidId[_loc2_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.questsToValidId[_loc2_]) + ") on element 1 (starting at 1) of questsToValidId.")
            param1.write_var_short(self.questsToValidId[_loc2_])
            _loc2_ += 1
        param1.write_short(len(self.questsToStartId))
        _loc3_ = 0
        while _loc3_ < len(self.questsToStartId):
            if self.questsToStartId[_loc3_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.questsToStartId[_loc3_]) + ") on element 2 (starting at 1) of questsToStartId.")
            param1.write_var_short(self.questsToStartId[_loc3_])
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayNpcQuestFlag(param1)

    def deserializeAs_GameRolePlayNpcQuestFlag(self, param1):
        _loc6_ = 0
        _loc7_ = 0
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_var_uh_short()
            if _loc6_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc6_) + ") on elements of questsToValidId.")
            self.questsToValidId.append(_loc6_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc7_ = param1.read_var_uh_short()
            if _loc7_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc7_) + ") on elements of questsToStartId.")
            self.questsToStartId.append(_loc7_)
            _loc5_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayNpcQuestFlag(param1)

    def deserializeAsyncAs_GameRolePlayNpcQuestFlag(self, param1):
        self._questsToValidIdtree = param1.add_child(self._questsToValidIdtreeFunc)
        self._questsToStartIdtree = param1.add_child(self._questsToStartIdtreeFunc)

    def _questsToValidIdtreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._questsToValidIdtree.add_child(self._questsToValidIdFunc)
            _loc3_ += 1

    def _questsToValidIdFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of questsToValidId.")
        self.questsToValidId.append(_loc2_)

    def _questsToStartIdtreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._questsToStartIdtree.add_child(self._questsToStartIdFunc)
            _loc3_ += 1

    def _questsToStartIdFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of questsToStartId.")
        self.questsToStartId.append(_loc2_)


class QuestActiveInformations():
    protocolId = 381

    def __init__(self):
        super().__init__()
        self.questId = 0

    def getTypeId(self):
        return 381

    def initQuestActiveInformations(self, param1=0):
        self.questId = param1
        return self

    def reset(self):
        self.questId = 0

    def serialize(self, param1):
        self.serializeAs_QuestActiveInformations(param1)

    def serializeAs_QuestActiveInformations(self, param1):
        if self.questId < 0:
            raise RuntimeError("Forbidden value (" + str(self.questId) + ") on element questId.")
        param1.write_var_short(self.questId)

    def deserialize(self, param1):
        self.deserializeAs_QuestActiveInformations(param1)

    def deserializeAs_QuestActiveInformations(self, param1):
        self._questIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_QuestActiveInformations(param1)

    def deserializeAsyncAs_QuestActiveInformations(self, param1):
        param1.add_child(self._questIdFunc)

    def _questIdFunc(self, param1):
        self.questId = param1.read_var_uh_short()
        if self.questId < 0:
            raise RuntimeError("Forbidden value (" + str(self.questId) + ") on element of QuestActiveInformations.questId.")


class QuestObjectiveInformations():
    protocolId = 385

    def __init__(self):
        super().__init__()
        self.objectiveId = 0
        self.objectiveStatus = False
        self.dialogParams = []
        self._dialogParamstree = FuncTree()

    def getTypeId(self):
        return 385

    def initQuestObjectiveInformations(self, param1=0, param2=False, param3=[]):
        self.objectiveId = param1
        self.objectiveStatus = param2
        self.dialogParams = param3
        return self

    def reset(self):
        self.objectiveId = 0
        self.objectiveStatus = False
        self.dialogParams = []

    def serialize(self, param1):
        self.serializeAs_QuestObjectiveInformations(param1)

    def serializeAs_QuestObjectiveInformations(self, param1):
        if self.objectiveId < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectiveId) + ") on element objectiveId.")
        param1.write_var_short(self.objectiveId)
        param1.write_boolean(self.objectiveStatus)
        param1.write_short(len(self.dialogParams))
        _loc2_ = 0
        while _loc2_ < len(self.dialogParams):
            param1.write_utf(self.dialogParams[_loc2_])
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_QuestObjectiveInformations(param1)

    def deserializeAs_QuestObjectiveInformations(self, param1):
        _loc4_ = None
        self._objectiveIdFunc(param1)
        self._objectiveStatusFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_utf()
            self.dialogParams.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_QuestObjectiveInformations(param1)

    def deserializeAsyncAs_QuestObjectiveInformations(self, param1):
        param1.add_child(self._objectiveIdFunc)
        param1.add_child(self._objectiveStatusFunc)
        self._dialogParamstree = param1.add_child(self._dialogParamstreeFunc)

    def _objectiveIdFunc(self, param1):
        self.objectiveId = param1.read_var_uh_short()
        if self.objectiveId < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectiveId) + ") on element of QuestObjectiveInformations.objectiveId.")

    def _objectiveStatusFunc(self, param1):
        self.objectiveStatus = param1.read_boolean()

    def _dialogParamstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._dialogParamstree.add_child(self._dialogParamsFunc)
            _loc3_ += 1

    def _dialogParamsFunc(self, param1):
        _loc2_ = param1.read_utf()
        self.dialogParams.append(_loc2_)


class PortalInformation():
    protocolId = 466

    def __init__(self):
        super().__init__()
        self.portalId = 0
        self.areaId = 0

    def getTypeId(self):
        return 466

    def initPortalInformation(self, param1=0, param2=0):
        self.portalId = param1
        self.areaId = param2
        return self

    def reset(self):
        self.portalId = 0
        self.areaId = 0

    def serialize(self, param1):
        self.serializeAs_PortalInformation(param1)

    def serializeAs_PortalInformation(self, param1):
        param1.write_int(self.portalId)
        param1.write_short(self.areaId)

    def deserialize(self, param1):
        self.deserializeAs_PortalInformation(param1)

    def deserializeAs_PortalInformation(self, param1):
        self._portalIdFunc(param1)
        self._areaIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PortalInformation(param1)

    def deserializeAsyncAs_PortalInformation(self, param1):
        param1.add_child(self._portalIdFunc)
        param1.add_child(self._areaIdFunc)

    def _portalIdFunc(self, param1):
        self.portalId = param1.read_int()

    def _areaIdFunc(self, param1):
        self.areaId = param1.read_short()


class TreasureHuntFlag():
    protocolId = 473

    def __init__(self):
        super().__init__()
        self.mapId = 0
        self.state = 0

    def getTypeId(self):
        return 473

    def initTreasureHuntFlag(self, param1=0, param2=0):
        self.mapId = param1
        self.state = param2
        return self

    def reset(self):
        self.mapId = 0
        self.state = 0

    def serialize(self, param1):
        self.serializeAs_TreasureHuntFlag(param1)

    def serializeAs_TreasureHuntFlag(self, param1):
        param1.write_int(self.mapId)
        param1.write_byte(self.state)

    def deserialize(self, param1):
        self.deserializeAs_TreasureHuntFlag(param1)

    def deserializeAs_TreasureHuntFlag(self, param1):
        self._mapIdFunc(param1)
        self._stateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TreasureHuntFlag(param1)

    def deserializeAsyncAs_TreasureHuntFlag(self, param1):
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._stateFunc)

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _stateFunc(self, param1):
        self.state = param1.read_byte()
        if self.state < 0:
            raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of TreasureHuntFlag.state.")


class TreasureHuntStep():
    protocolId = 463

    def getTypeId(self):
        return 463

    def initTreasureHuntStep(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_TreasureHuntStep(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_TreasureHuntStep(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_TreasureHuntStep(self, param1):
        pass


class DareCriteria():
    protocolId = 501

    def __init__(self):
        super().__init__()
        self.type = 0
        self.params = []
        self._paramstree = FuncTree()

    def getTypeId(self):
        return 501

    def initDareCriteria(self, param1=0, param2=[]):
        self.type = param1
        self.params = param2
        return self

    def reset(self):
        self.type = 0
        self.params = []

    def serialize(self, param1):
        self.serializeAs_DareCriteria(param1)

    def serializeAs_DareCriteria(self, param1):
        param1.write_byte(self.type)
        param1.write_short(len(self.params))
        _loc2_ = 0
        while _loc2_ < len(self.params):
            param1.write_int(self.params[_loc2_])
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_DareCriteria(param1)

    def deserializeAs_DareCriteria(self, param1):
        _loc4_ = 0
        self._typeFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_int()
            self.params.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_DareCriteria(param1)

    def deserializeAsyncAs_DareCriteria(self, param1):
        param1.add_child(self._typeFunc)
        self._paramstree = param1.add_child(self._paramstreeFunc)

    def _typeFunc(self, param1):
        self.type = param1.read_byte()
        if self.type < 0:
            raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of DareCriteria.type.")

    def _paramstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._paramstree.add_child(self._paramsFunc)
            _loc3_ += 1

    def _paramsFunc(self, param1):
        _loc2_ = param1.read_int()
        self.params.append(_loc2_)


class DareInformations():
    protocolId = 502

    def __init__(self):
        super().__init__()
        self.dareId = 0
        self.creator = CharacterBasicMinimalInformations()
        self.subscriptionFee = 0
        self.jackpot = 0
        self.maxCountWinners = 0
        self.endDate = 0
        self.isPrivate = False
        self.guildId = 0
        self.allianceId = 0
        self.criterions = []
        self.startDate = 0
        self._creatortree = FuncTree()
        self._criterionstree = FuncTree()

    def getTypeId(self):
        return 502

    def initDareInformations(self, param1=0, param2=None, param3=0, param4=0, param5=0, param6=0, param7=False, param8=0, param9=0, param10=[], param11=0):
        self.dareId = param1
        self.creator = param2
        self.subscriptionFee = param3
        self.jackpot = param4
        self.maxCountWinners = param5
        self.endDate = param6
        self.isPrivate = param7
        self.guildId = param8
        self.allianceId = param9
        self.criterions = param10
        self.startDate = param11
        return self

    def reset(self):
        self.dareId = 0
        self.creator = CharacterBasicMinimalInformations()
        self.jackpot = 0
        self.maxCountWinners = 0
        self.endDate = 0
        self.isPrivate = False
        self.guildId = 0
        self.allianceId = 0
        self.criterions = []
        self.startDate = 0

    def serialize(self, param1):
        self.serializeAs_DareInformations(param1)

    def serializeAs_DareInformations(self, param1):
        if self.dareId < 0 or self.dareId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.dareId) + ") on element dareId.")
        param1.write_double(self.dareId)
        self.creator.serializeAs_CharacterBasicMinimalInformations(param1)
        if self.subscriptionFee < 0 or self.subscriptionFee > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.subscriptionFee) + ") on element subscriptionFee.")
        param1.write_var_long(self.subscriptionFee)
        if self.jackpot < 0 or self.jackpot > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.jackpot) + ") on element jackpot.")
        param1.write_var_long(self.jackpot)
        if self.maxCountWinners < 0 or self.maxCountWinners > 65535:
            raise RuntimeError("Forbidden value (" + str(self.maxCountWinners) + ") on element maxCountWinners.")
        param1.write_short(self.maxCountWinners)
        if self.endDate < 0 or self.endDate > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.endDate) + ") on element endDate.")
        param1.write_double(self.endDate)
        param1.write_boolean(self.isPrivate)
        if self.guildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element guildId.")
        param1.write_var_int(self.guildId)
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element allianceId.")
        param1.write_var_int(self.allianceId)
        param1.write_short(len(self.criterions))
        _loc2_ = 0
        while _loc2_ < len(self.criterions):
            as_parent(self.criterions[_loc2_], DareCriteria).serializeAs_DareCriteria(param1)
            _loc2_ += 1
        if self.startDate < 0 or self.startDate > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.startDate) + ") on element startDate.")
        param1.write_double(self.startDate)

    def deserialize(self, param1):
        self.deserializeAs_DareInformations(param1)

    def deserializeAs_DareInformations(self, param1):
        _loc4_ = None
        self._dareIdFunc(param1)
        self.creator = CharacterBasicMinimalInformations()
        self.creator.deserialize(param1)
        self._subscriptionFeeFunc(param1)
        self._jackpotFunc(param1)
        self._maxCountWinnersFunc(param1)
        self._endDateFunc(param1)
        self._isPrivateFunc(param1)
        self._guildIdFunc(param1)
        self._allianceIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = DareCriteria()
            _loc4_.deserialize(param1)
            self.criterions.append(_loc4_)
            _loc3_ += 1
        self._startDateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_DareInformations(param1)

    def deserializeAsyncAs_DareInformations(self, param1):
        param1.add_child(self._dareIdFunc)
        self._creatortree = param1.add_child(self._creatortreeFunc)
        param1.add_child(self._subscriptionFeeFunc)
        param1.add_child(self._jackpotFunc)
        param1.add_child(self._maxCountWinnersFunc)
        param1.add_child(self._endDateFunc)
        param1.add_child(self._isPrivateFunc)
        param1.add_child(self._guildIdFunc)
        param1.add_child(self._allianceIdFunc)
        self._criterionstree = param1.add_child(self._criterionstreeFunc)
        param1.add_child(self._startDateFunc)

    def _dareIdFunc(self, param1):
        self.dareId = param1.read_double()
        if self.dareId < 0 or self.dareId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.dareId) + ") on element of DareInformations.dareId.")

    def _creatortreeFunc(self, param1):
        self.creator = CharacterBasicMinimalInformations()
        self.creator.deserializeAsync(self._creatortree)

    def _subscriptionFeeFunc(self, param1):
        self.subscriptionFee = param1.read_var_uh_long()
        if self.subscriptionFee < 0 or self.subscriptionFee > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.subscriptionFee) + ") on element of DareInformations.subscriptionFee.")

    def _jackpotFunc(self, param1):
        self.jackpot = param1.read_var_uh_long()
        if self.jackpot < 0 or self.jackpot > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.jackpot) + ") on element of DareInformations.jackpot.")

    def _maxCountWinnersFunc(self, param1):
        self.maxCountWinners = param1.read_unsigned_short()
        if self.maxCountWinners < 0 or self.maxCountWinners > 65535:
            raise RuntimeError("Forbidden value (" + str(self.maxCountWinners) + ") on element of DareInformations.maxCountWinners.")

    def _endDateFunc(self, param1):
        self.endDate = param1.read_double()
        if self.endDate < 0 or self.endDate > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.endDate) + ") on element of DareInformations.endDate.")

    def _isPrivateFunc(self, param1):
        self.isPrivate = param1.read_boolean()

    def _guildIdFunc(self, param1):
        self.guildId = param1.read_var_uh_int()
        if self.guildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of DareInformations.guildId.")

    def _allianceIdFunc(self, param1):
        self.allianceId = param1.read_var_uh_int()
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element of DareInformations.allianceId.")

    def _criterionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._criterionstree.add_child(self._criterionsFunc)
            _loc3_ += 1

    def _criterionsFunc(self, param1):
        _loc2_ = DareCriteria()
        _loc2_.deserialize(param1)
        self.criterions.append(_loc2_)

    def _startDateFunc(self, param1):
        self.startDate = param1.read_double()
        if self.startDate < 0 or self.startDate > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.startDate) + ") on element of DareInformations.startDate.")


class DareReward():
    protocolId = 505

    def __init__(self):
        super().__init__()
        self.type = 0
        self.monsterId = 0
        self.kamas = 0
        self.dareId = 0

    def getTypeId(self):
        return 505

    def initDareReward(self, param1=0, param2=0, param3=0, param4=0):
        self.type = param1
        self.monsterId = param2
        self.kamas = param3
        self.dareId = param4
        return self

    def reset(self):
        self.type = 0
        self.monsterId = 0
        self.kamas = 0
        self.dareId = 0

    def serialize(self, param1):
        self.serializeAs_DareReward(param1)

    def serializeAs_DareReward(self, param1):
        param1.write_byte(self.type)
        if self.monsterId < 0:
            raise RuntimeError("Forbidden value (" + str(self.monsterId) + ") on element monsterId.")
        param1.write_var_short(self.monsterId)
        if self.kamas < 0 or self.kamas > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element kamas.")
        param1.write_var_long(self.kamas)
        if self.dareId < 0 or self.dareId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.dareId) + ") on element dareId.")
        param1.write_double(self.dareId)

    def deserialize(self, param1):
        self.deserializeAs_DareReward(param1)

    def deserializeAs_DareReward(self, param1):
        self._typeFunc(param1)
        self._monsterIdFunc(param1)
        self._kamasFunc(param1)
        self._dareIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_DareReward(param1)

    def deserializeAsyncAs_DareReward(self, param1):
        param1.add_child(self._typeFunc)
        param1.add_child(self._monsterIdFunc)
        param1.add_child(self._kamasFunc)
        param1.add_child(self._dareIdFunc)

    def _typeFunc(self, param1):
        self.type = param1.read_byte()
        if self.type < 0:
            raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of DareReward.type.")

    def _monsterIdFunc(self, param1):
        self.monsterId = param1.read_var_uh_short()
        if self.monsterId < 0:
            raise RuntimeError("Forbidden value (" + str(self.monsterId) + ") on element of DareReward.monsterId.")

    def _kamasFunc(self, param1):
        self.kamas = param1.read_var_uh_long()
        if self.kamas < 0 or self.kamas > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element of DareReward.kamas.")

    def _dareIdFunc(self, param1):
        self.dareId = param1.read_double()
        if self.dareId < 0 or self.dareId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.dareId) + ") on element of DareReward.dareId.")


class DareVersatileInformations():
    protocolId = 504

    def __init__(self):
        super().__init__()
        self.dareId = 0
        self.countEntrants = 0
        self.countWinners = 0

    def getTypeId(self):
        return 504

    def initDareVersatileInformations(self, param1=0, param2=0, param3=0):
        self.dareId = param1
        self.countEntrants = param2
        self.countWinners = param3
        return self

    def reset(self):
        self.dareId = 0
        self.countEntrants = 0
        self.countWinners = 0

    def serialize(self, param1):
        self.serializeAs_DareVersatileInformations(param1)

    def serializeAs_DareVersatileInformations(self, param1):
        if self.dareId < 0 or self.dareId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.dareId) + ") on element dareId.")
        param1.write_double(self.dareId)
        if self.countEntrants < 0:
            raise RuntimeError("Forbidden value (" + str(self.countEntrants) + ") on element countEntrants.")
        param1.write_int(self.countEntrants)
        if self.countWinners < 0:
            raise RuntimeError("Forbidden value (" + str(self.countWinners) + ") on element countWinners.")
        param1.write_int(self.countWinners)

    def deserialize(self, param1):
        self.deserializeAs_DareVersatileInformations(param1)

    def deserializeAs_DareVersatileInformations(self, param1):
        self._dareIdFunc(param1)
        self._countEntrantsFunc(param1)
        self._countWinnersFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_DareVersatileInformations(param1)

    def deserializeAsyncAs_DareVersatileInformations(self, param1):
        param1.add_child(self._dareIdFunc)
        param1.add_child(self._countEntrantsFunc)
        param1.add_child(self._countWinnersFunc)

    def _dareIdFunc(self, param1):
        self.dareId = param1.read_double()
        if self.dareId < 0 or self.dareId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.dareId) + ") on element of DareVersatileInformations.dareId.")

    def _countEntrantsFunc(self, param1):
        self.countEntrants = param1.read_int()
        if self.countEntrants < 0:
            raise RuntimeError("Forbidden value (" + str(self.countEntrants) + ") on element of DareVersatileInformations.countEntrants.")

    def _countWinnersFunc(self, param1):
        self.countWinners = param1.read_int()
        if self.countWinners < 0:
            raise RuntimeError("Forbidden value (" + str(self.countWinners) + ") on element of DareVersatileInformations.countWinners.")


class BidExchangerObjectInfo():
    protocolId = 122

    def __init__(self):
        super().__init__()
        self.objectUID = 0
        self.effects = []
        self.prices = []
        self._effectstree = FuncTree()
        self._pricestree = FuncTree()

    def getTypeId(self):
        return 122

    def initBidExchangerObjectInfo(self, param1=0, param2=[], param3=[]):
        self.objectUID = param1
        self.effects = param2
        self.prices = param3
        return self

    def reset(self):
        self.objectUID = 0
        self.effects = []
        self.prices = []

    def serialize(self, param1):
        self.serializeAs_BidExchangerObjectInfo(param1)

    def serializeAs_BidExchangerObjectInfo(self, param1):
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element objectUID.")
        param1.write_var_int(self.objectUID)
        param1.write_short(len(self.effects))
        _loc2_ = 0
        while _loc2_ < len(self.effects):
            param1.write_short(as_parent(self.effects[_loc2_], ObjectEffect).getTypeId())
            as_parent(self.effects[_loc2_], ObjectEffect).serialize(param1)
            _loc2_ += 1
        param1.write_short(len(self.prices))
        _loc3_ = 0
        while _loc3_ < len(self.prices):
            if self.prices[_loc3_] < 0 or self.prices[_loc3_] > 9007199254740990:
                raise RuntimeError("Forbidden value (" + str(self.prices[_loc3_]) + ") on element 3 (starting at 1) of prices.")
            param1.write_var_long(self.prices[_loc3_])
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_BidExchangerObjectInfo(param1)

    def deserializeAs_BidExchangerObjectInfo(self, param1):
        _loc6_ = 0
        _loc7_ = None
        _loc8_ = None
        self._objectUIDFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_unsigned_short()
            _loc7_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc6_)
            _loc7_.deserialize(param1)
            self.effects.append(_loc7_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc8_ = param1.read_var_uh_long()
            if _loc8_ < 0 or _loc8_ > 9007199254740990:
                raise RuntimeError("Forbidden value (" + str(_loc8_) + ") on elements of prices.")
            self.prices.append(_loc8_)
            _loc5_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_BidExchangerObjectInfo(param1)

    def deserializeAsyncAs_BidExchangerObjectInfo(self, param1):
        param1.add_child(self._objectUIDFunc)
        self._effectstree = param1.add_child(self._effectstreeFunc)
        self._pricestree = param1.add_child(self._pricestreeFunc)

    def _objectUIDFunc(self, param1):
        self.objectUID = param1.read_var_uh_int()
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of BidExchangerObjectInfo.objectUID.")

    def _effectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._effectstree.add_child(self._effectsFunc)
            _loc3_ += 1

    def _effectsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc2_)
        _loc3_.deserialize(param1)
        self.effects.append(_loc3_)

    def _pricestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._pricestree.add_child(self._pricesFunc)
            _loc3_ += 1

    def _pricesFunc(self, param1):
        _loc2_ = param1.read_var_uh_long()
        if _loc2_ < 0 or _loc2_ > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of prices.")
        self.prices.append(_loc2_)


class Item():
    protocolId = 7

    def getTypeId(self):
        return 7

    def initItem(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_Item(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_Item(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_Item(self, param1):
        pass


class SellerBuyerDescriptor():
    protocolId = 121

    def __init__(self):
        super().__init__()
        self.quantities = []
        self.types = []
        self.taxPercentage = 0
        self.taxModificationPercentage = 0
        self.maxItemLevel = 0
        self.maxItemPerAccount = 0
        self.npcContextualId = 0
        self.unsoldDelay = 0
        self._quantitiestree = FuncTree()
        self._typestree = FuncTree()

    def getTypeId(self):
        return 121

    def initSellerBuyerDescriptor(self, param1=[], param2=[], param3=0, param4=0, param5=0, param6=0, param7=0, param8=0):
        self.quantities = param1
        self.types = param2
        self.taxPercentage = param3
        self.taxModificationPercentage = param4
        self.maxItemLevel = param5
        self.maxItemPerAccount = param6
        self.npcContextualId = param7
        self.unsoldDelay = param8
        return self

    def reset(self):
        self.quantities = []
        self.types = []
        self.taxPercentage = 0
        self.taxModificationPercentage = 0
        self.maxItemLevel = 0
        self.maxItemPerAccount = 0
        self.npcContextualId = 0
        self.unsoldDelay = 0

    def serialize(self, param1):
        self.serializeAs_SellerBuyerDescriptor(param1)

    def serializeAs_SellerBuyerDescriptor(self, param1):
        param1.write_short(len(self.quantities))
        _loc2_ = 0
        while _loc2_ < len(self.quantities):
            if self.quantities[_loc2_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.quantities[_loc2_]) + ") on element 1 (starting at 1) of quantities.")
            param1.write_var_int(self.quantities[_loc2_])
            _loc2_ += 1
        param1.write_short(len(self.types))
        _loc3_ = 0
        while _loc3_ < len(self.types):
            if self.types[_loc3_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.types[_loc3_]) + ") on element 2 (starting at 1) of types.")
            param1.write_var_int(self.types[_loc3_])
            _loc3_ += 1
        param1.write_float(self.taxPercentage)
        param1.write_float(self.taxModificationPercentage)
        if self.maxItemLevel < 0 or self.maxItemLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.maxItemLevel) + ") on element maxItemLevel.")
        param1.write_byte(self.maxItemLevel)
        if self.maxItemPerAccount < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxItemPerAccount) + ") on element maxItemPerAccount.")
        param1.write_var_int(self.maxItemPerAccount)
        param1.write_int(self.npcContextualId)
        if self.unsoldDelay < 0:
            raise RuntimeError("Forbidden value (" + str(self.unsoldDelay) + ") on element unsoldDelay.")
        param1.write_var_short(self.unsoldDelay)

    def deserialize(self, param1):
        self.deserializeAs_SellerBuyerDescriptor(param1)

    def deserializeAs_SellerBuyerDescriptor(self, param1):
        _loc6_ = 0
        _loc7_ = 0
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_var_uh_int()
            if _loc6_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc6_) + ") on elements of quantities.")
            self.quantities.append(_loc6_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc7_ = param1.read_var_uh_int()
            if _loc7_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc7_) + ") on elements of types.")
            self.types.append(_loc7_)
            _loc5_ += 1
        self._taxPercentageFunc(param1)
        self._taxModificationPercentageFunc(param1)
        self._maxItemLevelFunc(param1)
        self._maxItemPerAccountFunc(param1)
        self._npcContextualIdFunc(param1)
        self._unsoldDelayFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_SellerBuyerDescriptor(param1)

    def deserializeAsyncAs_SellerBuyerDescriptor(self, param1):
        self._quantitiestree = param1.add_child(self._quantitiestreeFunc)
        self._typestree = param1.add_child(self._typestreeFunc)
        param1.add_child(self._taxPercentageFunc)
        param1.add_child(self._taxModificationPercentageFunc)
        param1.add_child(self._maxItemLevelFunc)
        param1.add_child(self._maxItemPerAccountFunc)
        param1.add_child(self._npcContextualIdFunc)
        param1.add_child(self._unsoldDelayFunc)

    def _quantitiestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._quantitiestree.add_child(self._quantitiesFunc)
            _loc3_ += 1

    def _quantitiesFunc(self, param1):
        _loc2_ = param1.read_var_uh_int()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of quantities.")
        self.quantities.append(_loc2_)

    def _typestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._typestree.add_child(self._typesFunc)
            _loc3_ += 1

    def _typesFunc(self, param1):
        _loc2_ = param1.read_var_uh_int()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of types.")
        self.types.append(_loc2_)

    def _taxPercentageFunc(self, param1):
        self.taxPercentage = param1.read_float()

    def _taxModificationPercentageFunc(self, param1):
        self.taxModificationPercentage = param1.read_float()

    def _maxItemLevelFunc(self, param1):
        self.maxItemLevel = param1.read_unsigned_byte()
        if self.maxItemLevel < 0 or self.maxItemLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.maxItemLevel) + ") on element of SellerBuyerDescriptor.maxItemLevel.")

    def _maxItemPerAccountFunc(self, param1):
        self.maxItemPerAccount = param1.read_var_uh_int()
        if self.maxItemPerAccount < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxItemPerAccount) + ") on element of SellerBuyerDescriptor.maxItemPerAccount.")

    def _npcContextualIdFunc(self, param1):
        self.npcContextualId = param1.read_int()

    def _unsoldDelayFunc(self, param1):
        self.unsoldDelay = param1.read_var_uh_short()
        if self.unsoldDelay < 0:
            raise RuntimeError("Forbidden value (" + str(self.unsoldDelay) + ") on element of SellerBuyerDescriptor.unsoldDelay.")


class ObjectEffect():
    protocolId = 76

    def __init__(self):
        super().__init__()
        self.actionId = 0

    def getTypeId(self):
        return 76

    def initObjectEffect(self, param1=0):
        self.actionId = param1
        return self

    def reset(self):
        self.actionId = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffect(param1)

    def serializeAs_ObjectEffect(self, param1):
        if self.actionId < 0:
            raise RuntimeError("Forbidden value (" + str(self.actionId) + ") on element actionId.")
        param1.write_var_short(self.actionId)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffect(param1)

    def deserializeAs_ObjectEffect(self, param1):
        self._actionIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffect(param1)

    def deserializeAsyncAs_ObjectEffect(self, param1):
        param1.add_child(self._actionIdFunc)

    def _actionIdFunc(self, param1):
        self.actionId = param1.read_var_uh_short()
        if self.actionId < 0:
            raise RuntimeError("Forbidden value (" + str(self.actionId) + ") on element of ObjectEffect.actionId.")


class ProtectedEntityWaitingForHelpInfo():
    protocolId = 186

    def __init__(self):
        super().__init__()
        self.timeLeftBeforeFight = 0
        self.waitTimeForPlacement = 0
        self.nbPositionForDefensors = 0

    def getTypeId(self):
        return 186

    def initProtectedEntityWaitingForHelpInfo(self, param1=0, param2=0, param3=0):
        self.timeLeftBeforeFight = param1
        self.waitTimeForPlacement = param2
        self.nbPositionForDefensors = param3
        return self

    def reset(self):
        self.timeLeftBeforeFight = 0
        self.waitTimeForPlacement = 0
        self.nbPositionForDefensors = 0

    def serialize(self, param1):
        self.serializeAs_ProtectedEntityWaitingForHelpInfo(param1)

    def serializeAs_ProtectedEntityWaitingForHelpInfo(self, param1):
        param1.write_int(self.timeLeftBeforeFight)
        param1.write_int(self.waitTimeForPlacement)
        if self.nbPositionForDefensors < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbPositionForDefensors) + ") on element nbPositionForDefensors.")
        param1.write_byte(self.nbPositionForDefensors)

    def deserialize(self, param1):
        self.deserializeAs_ProtectedEntityWaitingForHelpInfo(param1)

    def deserializeAs_ProtectedEntityWaitingForHelpInfo(self, param1):
        self._timeLeftBeforeFightFunc(param1)
        self._waitTimeForPlacementFunc(param1)
        self._nbPositionForDefensorsFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ProtectedEntityWaitingForHelpInfo(param1)

    def deserializeAsyncAs_ProtectedEntityWaitingForHelpInfo(self, param1):
        param1.add_child(self._timeLeftBeforeFightFunc)
        param1.add_child(self._waitTimeForPlacementFunc)
        param1.add_child(self._nbPositionForDefensorsFunc)

    def _timeLeftBeforeFightFunc(self, param1):
        self.timeLeftBeforeFight = param1.read_int()

    def _waitTimeForPlacementFunc(self, param1):
        self.waitTimeForPlacement = param1.read_int()

    def _nbPositionForDefensorsFunc(self, param1):
        self.nbPositionForDefensors = param1.read_byte()
        if self.nbPositionForDefensors < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbPositionForDefensors) + ") on element of ProtectedEntityWaitingForHelpInfo.nbPositionForDefensors.")


class FinishMoveInformations():
    protocolId = 506

    def __init__(self):
        super().__init__()
        self.finishMoveId = 0
        self.finishMoveState = False

    def getTypeId(self):
        return 506

    def initFinishMoveInformations(self, param1=0, param2=False):
        self.finishMoveId = param1
        self.finishMoveState = param2
        return self

    def reset(self):
        self.finishMoveId = 0
        self.finishMoveState = False

    def serialize(self, param1):
        self.serializeAs_FinishMoveInformations(param1)

    def serializeAs_FinishMoveInformations(self, param1):
        if self.finishMoveId < 0:
            raise RuntimeError("Forbidden value (" + str(self.finishMoveId) + ") on element finishMoveId.")
        param1.write_int(self.finishMoveId)
        param1.write_boolean(self.finishMoveState)

    def deserialize(self, param1):
        self.deserializeAs_FinishMoveInformations(param1)

    def deserializeAs_FinishMoveInformations(self, param1):
        self._finishMoveIdFunc(param1)
        self._finishMoveStateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FinishMoveInformations(param1)

    def deserializeAsyncAs_FinishMoveInformations(self, param1):
        param1.add_child(self._finishMoveIdFunc)
        param1.add_child(self._finishMoveStateFunc)

    def _finishMoveIdFunc(self, param1):
        self.finishMoveId = param1.read_int()
        if self.finishMoveId < 0:
            raise RuntimeError("Forbidden value (" + str(self.finishMoveId) + ") on element of FinishMoveInformations.finishMoveId.")

    def _finishMoveStateFunc(self, param1):
        self.finishMoveState = param1.read_boolean()


class AbstractContactInformations():
    protocolId = 380

    def __init__(self):
        super().__init__()
        self.accountId = 0
        self.accountName = ""

    def getTypeId(self):
        return 380

    def initAbstractContactInformations(self, param1=0, param2=""):
        self.accountId = param1
        self.accountName = param2
        return self

    def reset(self):
        self.accountId = 0
        self.accountName = ""

    def serialize(self, param1):
        self.serializeAs_AbstractContactInformations(param1)

    def serializeAs_AbstractContactInformations(self, param1):
        if self.accountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element accountId.")
        param1.write_int(self.accountId)
        param1.write_utf(self.accountName)

    def deserialize(self, param1):
        self.deserializeAs_AbstractContactInformations(param1)

    def deserializeAs_AbstractContactInformations(self, param1):
        self._accountIdFunc(param1)
        self._accountNameFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AbstractContactInformations(param1)

    def deserializeAsyncAs_AbstractContactInformations(self, param1):
        param1.add_child(self._accountIdFunc)
        param1.add_child(self._accountNameFunc)

    def _accountIdFunc(self, param1):
        self.accountId = param1.read_int()
        if self.accountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of AbstractContactInformations.accountId.")

    def _accountNameFunc(self, param1):
        self.accountName = param1.read_utf()


class FriendSpouseInformations():
    protocolId = 77

    def __init__(self):
        super().__init__()
        self.spouseAccountId = 0
        self.spouseId = 0
        self.spouseName = ""
        self.spouseLevel = 0
        self.breed = 0
        self.sex = 0
        self.spouseEntityLook = EntityLook()
        self.guildInfo = GuildInformations()
        self.alignmentSide = 0
        self._spouseEntityLooktree = FuncTree()
        self._guildInfotree = FuncTree()

    def getTypeId(self):
        return 77

    def initFriendSpouseInformations(self, param1=0, param2=0, param3="", param4=0, param5=0, param6=0, param7=None, param8=None, param9=0):
        self.spouseAccountId = param1
        self.spouseId = param2
        self.spouseName = param3
        self.spouseLevel = param4
        self.breed = param5
        self.sex = param6
        self.spouseEntityLook = param7
        self.guildInfo = param8
        self.alignmentSide = param9
        return self

    def reset(self):
        self.spouseAccountId = 0
        self.spouseId = 0
        self.spouseName = ""
        self.spouseLevel = 0
        self.breed = 0
        self.sex = 0
        self.spouseEntityLook = EntityLook()

    def serialize(self, param1):
        self.serializeAs_FriendSpouseInformations(param1)

    def serializeAs_FriendSpouseInformations(self, param1):
        if self.spouseAccountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.spouseAccountId) + ") on element spouseAccountId.")
        param1.write_int(self.spouseAccountId)
        if self.spouseId < 0 or self.spouseId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.spouseId) + ") on element spouseId.")
        param1.write_var_long(self.spouseId)
        param1.write_utf(self.spouseName)
        if self.spouseLevel < 1 or self.spouseLevel > 206:
            raise RuntimeError("Forbidden value (" + str(self.spouseLevel) + ") on element spouseLevel.")
        param1.write_byte(self.spouseLevel)
        param1.write_byte(self.breed)
        param1.write_byte(self.sex)
        self.spouseEntityLook.serializeAs_EntityLook(param1)
        self.guildInfo.serializeAs_GuildInformations(param1)
        param1.write_byte(self.alignmentSide)

    def deserialize(self, param1):
        self.deserializeAs_FriendSpouseInformations(param1)

    def deserializeAs_FriendSpouseInformations(self, param1):
        self._spouseAccountIdFunc(param1)
        self._spouseIdFunc(param1)
        self._spouseNameFunc(param1)
        self._spouseLevelFunc(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)
        self.spouseEntityLook = EntityLook()
        self.spouseEntityLook.deserialize(param1)
        self.guildInfo = GuildInformations()
        self.guildInfo.deserialize(param1)
        self._alignmentSideFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FriendSpouseInformations(param1)

    def deserializeAsyncAs_FriendSpouseInformations(self, param1):
        param1.add_child(self._spouseAccountIdFunc)
        param1.add_child(self._spouseIdFunc)
        param1.add_child(self._spouseNameFunc)
        param1.add_child(self._spouseLevelFunc)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)
        self._spouseEntityLooktree = param1.add_child(self._spouseEntityLooktreeFunc)
        self._guildInfotree = param1.add_child(self._guildInfotreeFunc)
        param1.add_child(self._alignmentSideFunc)

    def _spouseAccountIdFunc(self, param1):
        self.spouseAccountId = param1.read_int()
        if self.spouseAccountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.spouseAccountId) + ") on element of FriendSpouseInformations.spouseAccountId.")

    def _spouseIdFunc(self, param1):
        self.spouseId = param1.read_var_uh_long()
        if self.spouseId < 0 or self.spouseId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.spouseId) + ") on element of FriendSpouseInformations.spouseId.")

    def _spouseNameFunc(self, param1):
        self.spouseName = param1.read_utf()

    def _spouseLevelFunc(self, param1):
        self.spouseLevel = param1.read_unsigned_byte()
        if self.spouseLevel < 1 or self.spouseLevel > 206:
            raise RuntimeError("Forbidden value (" + str(self.spouseLevel) + ") on element of FriendSpouseInformations.spouseLevel.")

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()

    def _sexFunc(self, param1):
        self.sex = param1.read_byte()

    def _spouseEntityLooktreeFunc(self, param1):
        self.spouseEntityLook = EntityLook()
        self.spouseEntityLook.deserializeAsync(self._spouseEntityLooktree)

    def _guildInfotreeFunc(self, param1):
        self.guildInfo = GuildInformations()
        self.guildInfo.deserializeAsync(self._guildInfotree)

    def _alignmentSideFunc(self, param1):
        self.alignmentSide = param1.read_byte()


class GuildEmblem():
    protocolId = 87

    def __init__(self):
        super().__init__()
        self.symbolShape = 0
        self.symbolColor = 0
        self.backgroundShape = 0
        self.backgroundColor = 0

    def getTypeId(self):
        return 87

    def initGuildEmblem(self, param1=0, param2=0, param3=0, param4=0):
        self.symbolShape = param1
        self.symbolColor = param2
        self.backgroundShape = param3
        self.backgroundColor = param4
        return self

    def reset(self):
        self.symbolShape = 0
        self.symbolColor = 0
        self.backgroundShape = 0
        self.backgroundColor = 0

    def serialize(self, param1):
        self.serializeAs_GuildEmblem(param1)

    def serializeAs_GuildEmblem(self, param1):
        if self.symbolShape < 0:
            raise RuntimeError("Forbidden value (" + str(self.symbolShape) + ") on element symbolShape.")
        param1.write_var_short(self.symbolShape)
        param1.write_int(self.symbolColor)
        if self.backgroundShape < 0:
            raise RuntimeError("Forbidden value (" + str(self.backgroundShape) + ") on element backgroundShape.")
        param1.write_byte(self.backgroundShape)
        param1.write_int(self.backgroundColor)

    def deserialize(self, param1):
        self.deserializeAs_GuildEmblem(param1)

    def deserializeAs_GuildEmblem(self, param1):
        self._symbolShapeFunc(param1)
        self._symbolColorFunc(param1)
        self._backgroundShapeFunc(param1)
        self._backgroundColorFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GuildEmblem(param1)

    def deserializeAsyncAs_GuildEmblem(self, param1):
        param1.add_child(self._symbolShapeFunc)
        param1.add_child(self._symbolColorFunc)
        param1.add_child(self._backgroundShapeFunc)
        param1.add_child(self._backgroundColorFunc)

    def _symbolShapeFunc(self, param1):
        self.symbolShape = param1.read_var_uh_short()
        if self.symbolShape < 0:
            raise RuntimeError("Forbidden value (" + str(self.symbolShape) + ") on element of GuildEmblem.symbolShape.")

    def _symbolColorFunc(self, param1):
        self.symbolColor = param1.read_int()

    def _backgroundShapeFunc(self, param1):
        self.backgroundShape = param1.read_byte()
        if self.backgroundShape < 0:
            raise RuntimeError("Forbidden value (" + str(self.backgroundShape) + ") on element of GuildEmblem.backgroundShape.")

    def _backgroundColorFunc(self, param1):
        self.backgroundColor = param1.read_int()


class HavenBagFurnitureInformation():
    protocolId = 498

    def __init__(self):
        super().__init__()
        self.cellId = 0
        self.funitureId = 0
        self.orientation = 0

    def getTypeId(self):
        return 498

    def initHavenBagFurnitureInformation(self, param1=0, param2=0, param3=0):
        self.cellId = param1
        self.funitureId = param2
        self.orientation = param3
        return self

    def reset(self):
        self.cellId = 0
        self.funitureId = 0
        self.orientation = 0

    def serialize(self, param1):
        self.serializeAs_HavenBagFurnitureInformation(param1)

    def serializeAs_HavenBagFurnitureInformation(self, param1):
        if self.cellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element cellId.")
        param1.write_var_short(self.cellId)
        param1.write_int(self.funitureId)
        if self.orientation < 0:
            raise RuntimeError("Forbidden value (" + str(self.orientation) + ") on element orientation.")
        param1.write_byte(self.orientation)

    def deserialize(self, param1):
        self.deserializeAs_HavenBagFurnitureInformation(param1)

    def deserializeAs_HavenBagFurnitureInformation(self, param1):
        self._cellIdFunc(param1)
        self._funitureIdFunc(param1)
        self._orientationFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HavenBagFurnitureInformation(param1)

    def deserializeAsyncAs_HavenBagFurnitureInformation(self, param1):
        param1.add_child(self._cellIdFunc)
        param1.add_child(self._funitureIdFunc)
        param1.add_child(self._orientationFunc)

    def _cellIdFunc(self, param1):
        self.cellId = param1.read_var_uh_short()
        if self.cellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of HavenBagFurnitureInformation.cellId.")

    def _funitureIdFunc(self, param1):
        self.funitureId = param1.read_int()

    def _orientationFunc(self, param1):
        self.orientation = param1.read_byte()
        if self.orientation < 0:
            raise RuntimeError("Forbidden value (" + str(self.orientation) + ") on element of HavenBagFurnitureInformation.orientation.")


class AdditionalTaxCollectorInformations():
    protocolId = 165

    def __init__(self):
        super().__init__()
        self.collectorCallerName = ""
        self.date = 0

    def getTypeId(self):
        return 165

    def initAdditionalTaxCollectorInformations(self, param1="", param2=0):
        self.collectorCallerName = param1
        self.date = param2
        return self

    def reset(self):
        self.collectorCallerName = ""
        self.date = 0

    def serialize(self, param1):
        self.serializeAs_AdditionalTaxCollectorInformations(param1)

    def serializeAs_AdditionalTaxCollectorInformations(self, param1):
        param1.write_utf(self.collectorCallerName)
        if self.date < 0:
            raise RuntimeError("Forbidden value (" + str(self.date) + ") on element date.")
        param1.write_int(self.date)

    def deserialize(self, param1):
        self.deserializeAs_AdditionalTaxCollectorInformations(param1)

    def deserializeAs_AdditionalTaxCollectorInformations(self, param1):
        self._collectorCallerNameFunc(param1)
        self._dateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AdditionalTaxCollectorInformations(param1)

    def deserializeAsyncAs_AdditionalTaxCollectorInformations(self, param1):
        param1.add_child(self._collectorCallerNameFunc)
        param1.add_child(self._dateFunc)

    def _collectorCallerNameFunc(self, param1):
        self.collectorCallerName = param1.read_utf()

    def _dateFunc(self, param1):
        self.date = param1.read_int()
        if self.date < 0:
            raise RuntimeError("Forbidden value (" + str(self.date) + ") on element of AdditionalTaxCollectorInformations.date.")


class TaxCollectorBasicInformations():
    protocolId = 96

    def __init__(self):
        super().__init__()
        self.firstNameId = 0
        self.lastNameId = 0
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0

    def getTypeId(self):
        return 96

    def initTaxCollectorBasicInformations(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0):
        self.firstNameId = param1
        self.lastNameId = param2
        self.worldX = param3
        self.worldY = param4
        self.mapId = param5
        self.subAreaId = param6
        return self

    def reset(self):
        self.firstNameId = 0
        self.lastNameId = 0
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0

    def serialize(self, param1):
        self.serializeAs_TaxCollectorBasicInformations(param1)

    def serializeAs_TaxCollectorBasicInformations(self, param1):
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element firstNameId.")
        param1.write_var_short(self.firstNameId)
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element lastNameId.")
        param1.write_var_short(self.lastNameId)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorBasicInformations(param1)

    def deserializeAs_TaxCollectorBasicInformations(self, param1):
        self._firstNameIdFunc(param1)
        self._lastNameIdFunc(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorBasicInformations(param1)

    def deserializeAsyncAs_TaxCollectorBasicInformations(self, param1):
        param1.add_child(self._firstNameIdFunc)
        param1.add_child(self._lastNameIdFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)

    def _firstNameIdFunc(self, param1):
        self.firstNameId = param1.read_var_uh_short()
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of TaxCollectorBasicInformations.firstNameId.")

    def _lastNameIdFunc(self, param1):
        self.lastNameId = param1.read_var_uh_short()
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of TaxCollectorBasicInformations.lastNameId.")

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of TaxCollectorBasicInformations.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of TaxCollectorBasicInformations.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of TaxCollectorBasicInformations.subAreaId.")


class TaxCollectorComplementaryInformations():
    protocolId = 448

    def getTypeId(self):
        return 448

    def initTaxCollectorComplementaryInformations(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_TaxCollectorComplementaryInformations(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_TaxCollectorComplementaryInformations(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_TaxCollectorComplementaryInformations(self, param1):
        pass


class TaxCollectorFightersInformation():
    protocolId = 169

    def __init__(self):
        super().__init__()
        self.collectorId = 0
        self.allyCharactersInformations = []
        self.enemyCharactersInformations = []
        self._allyCharactersInformationstree = FuncTree()
        self._enemyCharactersInformationstree = FuncTree()

    def getTypeId(self):
        return 169

    def initTaxCollectorFightersInformation(self, param1=0, param2=[], param3=[]):
        self.collectorId = param1
        self.allyCharactersInformations = param2
        self.enemyCharactersInformations = param3
        return self

    def reset(self):
        self.collectorId = 0
        self.allyCharactersInformations = []
        self.enemyCharactersInformations = []

    def serialize(self, param1):
        self.serializeAs_TaxCollectorFightersInformation(param1)

    def serializeAs_TaxCollectorFightersInformation(self, param1):
        param1.write_int(self.collectorId)
        param1.write_short(len(self.allyCharactersInformations))
        _loc2_ = 0
        while _loc2_ < len(self.allyCharactersInformations):
            param1.write_short(as_parent(self.allyCharactersInformations[_loc2_], CharacterMinimalPlusLookInformations).getTypeId())
            as_parent(self.allyCharactersInformations[_loc2_], CharacterMinimalPlusLookInformations).serialize(param1)
            _loc2_ += 1
        param1.write_short(len(self.enemyCharactersInformations))
        _loc3_ = 0
        while _loc3_ < len(self.enemyCharactersInformations):
            param1.write_short(as_parent(self.enemyCharactersInformations[_loc3_], CharacterMinimalPlusLookInformations).getTypeId())
            as_parent(self.enemyCharactersInformations[_loc3_], CharacterMinimalPlusLookInformations).serialize(param1)
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorFightersInformation(param1)

    def deserializeAs_TaxCollectorFightersInformation(self, param1):
        _loc6_ = 0
        _loc7_ = None
        _loc8_ = 0
        _loc9_ = None
        self._collectorIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_unsigned_short()
            _loc7_ = ProtocolTypeManager.get_instance(CharacterMinimalPlusLookInformations,_loc6_)
            _loc7_.deserialize(param1)
            self.allyCharactersInformations.append(_loc7_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc8_ = param1.read_unsigned_short()
            _loc9_ = ProtocolTypeManager.get_instance(CharacterMinimalPlusLookInformations,_loc8_)
            _loc9_.deserialize(param1)
            self.enemyCharactersInformations.append(_loc9_)
            _loc5_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorFightersInformation(param1)

    def deserializeAsyncAs_TaxCollectorFightersInformation(self, param1):
        param1.add_child(self._collectorIdFunc)
        self._allyCharactersInformationstree = param1.add_child(self._allyCharactersInformationstreeFunc)
        self._enemyCharactersInformationstree = param1.add_child(self._enemyCharactersInformationstreeFunc)

    def _collectorIdFunc(self, param1):
        self.collectorId = param1.read_int()

    def _allyCharactersInformationstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._allyCharactersInformationstree.add_child(self._allyCharactersInformationsFunc)
            _loc3_ += 1

    def _allyCharactersInformationsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(CharacterMinimalPlusLookInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.allyCharactersInformations.append(_loc3_)

    def _enemyCharactersInformationstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._enemyCharactersInformationstree.add_child(self._enemyCharactersInformationsFunc)
            _loc3_ += 1

    def _enemyCharactersInformationsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(CharacterMinimalPlusLookInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.enemyCharactersInformations.append(_loc3_)


class TaxCollectorInformations():
    protocolId = 167

    def __init__(self):
        super().__init__()
        self.uniqueId = 0
        self.firtNameId = 0
        self.lastNameId = 0
        self.additionalInfos = AdditionalTaxCollectorInformations()
        self.worldX = 0
        self.worldY = 0
        self.subAreaId = 0
        self.state = 0
        self.look = EntityLook()
        self.complements = []
        self._additionalInfostree = FuncTree()
        self._looktree = FuncTree()
        self._complementstree = FuncTree()

    def getTypeId(self):
        return 167

    def initTaxCollectorInformations(self, param1=0, param2=0, param3=0, param4=None, param5=0, param6=0, param7=0, param8=0, param9=None, param10=[]):
        self.uniqueId = param1
        self.firtNameId = param2
        self.lastNameId = param3
        self.additionalInfos = param4
        self.worldX = param5
        self.worldY = param6
        self.subAreaId = param7
        self.state = param8
        self.look = param9
        self.complements = param10
        return self

    def reset(self):
        self.uniqueId = 0
        self.firtNameId = 0
        self.lastNameId = 0
        self.additionalInfos = AdditionalTaxCollectorInformations()
        self.worldY = 0
        self.subAreaId = 0
        self.state = 0
        self.look = EntityLook()

    def serialize(self, param1):
        self.serializeAs_TaxCollectorInformations(param1)

    def serializeAs_TaxCollectorInformations(self, param1):
        param1.write_int(self.uniqueId)
        if self.firtNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firtNameId) + ") on element firtNameId.")
        param1.write_var_short(self.firtNameId)
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element lastNameId.")
        param1.write_var_short(self.lastNameId)
        self.additionalInfos.serializeAs_AdditionalTaxCollectorInformations(param1)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        param1.write_byte(self.state)
        self.look.serializeAs_EntityLook(param1)
        param1.write_short(len(self.complements))
        _loc2_ = 0
        while _loc2_ < len(self.complements):
            param1.write_short(as_parent(self.complements[_loc2_], TaxCollectorComplementaryInformations).getTypeId())
            as_parent(self.complements[_loc2_], TaxCollectorComplementaryInformations).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorInformations(param1)

    def deserializeAs_TaxCollectorInformations(self, param1):
        _loc4_ = 0
        _loc5_ = None
        self._uniqueIdFunc(param1)
        self._firtNameIdFunc(param1)
        self._lastNameIdFunc(param1)
        self.additionalInfos = AdditionalTaxCollectorInformations()
        self.additionalInfos.deserialize(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._subAreaIdFunc(param1)
        self._stateFunc(param1)
        self.look = EntityLook()
        self.look.deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(TaxCollectorComplementaryInformations,_loc4_)
            _loc5_.deserialize(param1)
            self.complements.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorInformations(param1)

    def deserializeAsyncAs_TaxCollectorInformations(self, param1):
        param1.add_child(self._uniqueIdFunc)
        param1.add_child(self._firtNameIdFunc)
        param1.add_child(self._lastNameIdFunc)
        self._additionalInfostree = param1.add_child(self._additionalInfostreeFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._subAreaIdFunc)
        param1.add_child(self._stateFunc)
        self._looktree = param1.add_child(self._looktreeFunc)
        self._complementstree = param1.add_child(self._complementstreeFunc)

    def _uniqueIdFunc(self, param1):
        self.uniqueId = param1.read_int()

    def _firtNameIdFunc(self, param1):
        self.firtNameId = param1.read_var_uh_short()
        if self.firtNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firtNameId) + ") on element of TaxCollectorInformations.firtNameId.")

    def _lastNameIdFunc(self, param1):
        self.lastNameId = param1.read_var_uh_short()
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of TaxCollectorInformations.lastNameId.")

    def _additionalInfostreeFunc(self, param1):
        self.additionalInfos = AdditionalTaxCollectorInformations()
        self.additionalInfos.deserializeAsync(self._additionalInfostree)

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of TaxCollectorInformations.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of TaxCollectorInformations.worldY.")

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of TaxCollectorInformations.subAreaId.")

    def _stateFunc(self, param1):
        self.state = param1.read_byte()
        if self.state < 0:
            raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of TaxCollectorInformations.state.")

    def _looktreeFunc(self, param1):
        self.look = EntityLook()
        self.look.deserializeAsync(self._looktree)

    def _complementstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._complementstree.add_child(self._complementsFunc)
            _loc3_ += 1

    def _complementsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(TaxCollectorComplementaryInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.complements.append(_loc3_)


class TaxCollectorMovement():
    protocolId = 493

    def __init__(self):
        super().__init__()
        self.movementType = 0
        self.basicInfos = TaxCollectorBasicInformations()
        self.playerId = 0
        self.playerName = ""
        self._basicInfostree = FuncTree()

    def getTypeId(self):
        return 493

    def initTaxCollectorMovement(self, param1=0, param2=None, param3=0, param4=""):
        self.movementType = param1
        self.basicInfos = param2
        self.playerId = param3
        self.playerName = param4
        return self

    def reset(self):
        self.movementType = 0
        self.basicInfos = TaxCollectorBasicInformations()
        self.playerName = ""

    def serialize(self, param1):
        self.serializeAs_TaxCollectorMovement(param1)

    def serializeAs_TaxCollectorMovement(self, param1):
        param1.write_byte(self.movementType)
        self.basicInfos.serializeAs_TaxCollectorBasicInformations(param1)
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element playerId.")
        param1.write_var_long(self.playerId)
        param1.write_utf(self.playerName)

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorMovement(param1)

    def deserializeAs_TaxCollectorMovement(self, param1):
        self._movementTypeFunc(param1)
        self.basicInfos = TaxCollectorBasicInformations()
        self.basicInfos.deserialize(param1)
        self._playerIdFunc(param1)
        self._playerNameFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorMovement(param1)

    def deserializeAsyncAs_TaxCollectorMovement(self, param1):
        param1.add_child(self._movementTypeFunc)
        self._basicInfostree = param1.add_child(self._basicInfostreeFunc)
        param1.add_child(self._playerIdFunc)
        param1.add_child(self._playerNameFunc)

    def _movementTypeFunc(self, param1):
        self.movementType = param1.read_byte()
        if self.movementType < 0:
            raise RuntimeError("Forbidden value (" + str(self.movementType) + ") on element of TaxCollectorMovement.movementType.")

    def _basicInfostreeFunc(self, param1):
        self.basicInfos = TaxCollectorBasicInformations()
        self.basicInfos.deserializeAsync(self._basicInfostree)

    def _playerIdFunc(self, param1):
        self.playerId = param1.read_var_uh_long()
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of TaxCollectorMovement.playerId.")

    def _playerNameFunc(self, param1):
        self.playerName = param1.read_utf()


class HouseInformations():
    protocolId = 111

    def __init__(self):
        super().__init__()
        self.houseId = 0
        self.modelId = 0

    def getTypeId(self):
        return 111

    def initHouseInformations(self, param1=0, param2=0):
        self.houseId = param1
        self.modelId = param2
        return self

    def reset(self):
        self.houseId = 0
        self.modelId = 0

    def serialize(self, param1):
        self.serializeAs_HouseInformations(param1)

    def serializeAs_HouseInformations(self, param1):
        if self.houseId < 0:
            raise RuntimeError("Forbidden value (" + str(self.houseId) + ") on element houseId.")
        param1.write_var_int(self.houseId)
        if self.modelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element modelId.")
        param1.write_var_short(self.modelId)

    def deserialize(self, param1):
        self.deserializeAs_HouseInformations(param1)

    def deserializeAs_HouseInformations(self, param1):
        self._houseIdFunc(param1)
        self._modelIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HouseInformations(param1)

    def deserializeAsyncAs_HouseInformations(self, param1):
        param1.add_child(self._houseIdFunc)
        param1.add_child(self._modelIdFunc)

    def _houseIdFunc(self, param1):
        self.houseId = param1.read_var_uh_int()
        if self.houseId < 0:
            raise RuntimeError("Forbidden value (" + str(self.houseId) + ") on element of HouseInformations.houseId.")

    def _modelIdFunc(self, param1):
        self.modelId = param1.read_var_uh_short()
        if self.modelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element of HouseInformations.modelId.")


class HouseInformationsForSell():
    protocolId = 221

    def __init__(self):
        super().__init__()
        self.instanceId = 0
        self.secondHand = False
        self.modelId = 0
        self.ownerName = ""
        self.ownerConnected = False
        self.worldX = 0
        self.worldY = 0
        self.subAreaId = 0
        self.nbRoom = 0
        self.nbChest = 0
        self.skillListIds = []
        self.isLocked = False
        self.price = 0
        self._skillListIdstree = FuncTree()

    def getTypeId(self):
        return 221

    def initHouseInformationsForSell(self, param1=0, param2=False, param3=0, param4="", param5=False, param6=0, param7=0, param8=0, param9=0, param10=0, param11=[], param12=False, param13=0):
        self.instanceId = param1
        self.secondHand = param2
        self.modelId = param3
        self.ownerName = param4
        self.ownerConnected = param5
        self.worldX = param6
        self.worldY = param7
        self.subAreaId = param8
        self.nbRoom = param9
        self.nbChest = param10
        self.skillListIds = param11
        self.isLocked = param12
        self.price = param13
        return self

    def reset(self):
        self.instanceId = 0
        self.secondHand = False
        self.modelId = 0
        self.ownerName = ""
        self.ownerConnected = False
        self.worldX = 0
        self.worldY = 0
        self.subAreaId = 0
        self.nbRoom = 0
        self.nbChest = 0
        self.skillListIds = []
        self.isLocked = False
        self.price = 0

    def serialize(self, param1):
        self.serializeAs_HouseInformationsForSell(param1)

    def serializeAs_HouseInformationsForSell(self, param1):
        if self.instanceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element instanceId.")
        param1.write_int(self.instanceId)
        param1.write_boolean(self.secondHand)
        if self.modelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element modelId.")
        param1.write_var_int(self.modelId)
        param1.write_utf(self.ownerName)
        param1.write_boolean(self.ownerConnected)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        param1.write_byte(self.nbRoom)
        param1.write_byte(self.nbChest)
        param1.write_short(len(self.skillListIds))
        _loc2_ = 0
        while _loc2_ < len(self.skillListIds):
            param1.write_int(self.skillListIds[_loc2_])
            _loc2_ += 1
        param1.write_boolean(self.isLocked)
        if self.price < 0 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element price.")
        param1.write_var_long(self.price)

    def deserialize(self, param1):
        self.deserializeAs_HouseInformationsForSell(param1)

    def deserializeAs_HouseInformationsForSell(self, param1):
        _loc4_ = 0
        self._instanceIdFunc(param1)
        self._secondHandFunc(param1)
        self._modelIdFunc(param1)
        self._ownerNameFunc(param1)
        self._ownerConnectedFunc(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._subAreaIdFunc(param1)
        self._nbRoomFunc(param1)
        self._nbChestFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_int()
            self.skillListIds.append(_loc4_)
            _loc3_ += 1
        self._isLockedFunc(param1)
        self._priceFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HouseInformationsForSell(param1)

    def deserializeAsyncAs_HouseInformationsForSell(self, param1):
        param1.add_child(self._instanceIdFunc)
        param1.add_child(self._secondHandFunc)
        param1.add_child(self._modelIdFunc)
        param1.add_child(self._ownerNameFunc)
        param1.add_child(self._ownerConnectedFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._subAreaIdFunc)
        param1.add_child(self._nbRoomFunc)
        param1.add_child(self._nbChestFunc)
        self._skillListIdstree = param1.add_child(self._skillListIdstreeFunc)
        param1.add_child(self._isLockedFunc)
        param1.add_child(self._priceFunc)

    def _instanceIdFunc(self, param1):
        self.instanceId = param1.read_int()
        if self.instanceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of HouseInformationsForSell.instanceId.")

    def _secondHandFunc(self, param1):
        self.secondHand = param1.read_boolean()

    def _modelIdFunc(self, param1):
        self.modelId = param1.read_var_uh_int()
        if self.modelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element of HouseInformationsForSell.modelId.")

    def _ownerNameFunc(self, param1):
        self.ownerName = param1.read_utf()

    def _ownerConnectedFunc(self, param1):
        self.ownerConnected = param1.read_boolean()

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of HouseInformationsForSell.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of HouseInformationsForSell.worldY.")

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of HouseInformationsForSell.subAreaId.")

    def _nbRoomFunc(self, param1):
        self.nbRoom = param1.read_byte()

    def _nbChestFunc(self, param1):
        self.nbChest = param1.read_byte()

    def _skillListIdstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._skillListIdstree.add_child(self._skillListIdsFunc)
            _loc3_ += 1

    def _skillListIdsFunc(self, param1):
        _loc2_ = param1.read_int()
        self.skillListIds.append(_loc2_)

    def _isLockedFunc(self, param1):
        self.isLocked = param1.read_boolean()

    def _priceFunc(self, param1):
        self.price = param1.read_var_uh_long()
        if self.price < 0 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of HouseInformationsForSell.price.")


class HouseInstanceInformations():
    protocolId = 511

    def __init__(self):
        super().__init__()
        self.instanceId = 0
        self.secondHand = False
        self.isLocked = False
        self.ownerName = ""
        self.price = 0
        self.isSaleLocked = False

    def getTypeId(self):
        return 511

    def initHouseInstanceInformations(self, param1=0, param2=False, param3=False, param4="", param5=0, param6=False):
        self.instanceId = param1
        self.secondHand = param2
        self.isLocked = param3
        self.ownerName = param4
        self.price = param5
        self.isSaleLocked = param6
        return self

    def reset(self):
        self.instanceId = 0
        self.secondHand = False
        self.isLocked = False
        self.ownerName = ""
        self.price = 0
        self.isSaleLocked = False

    def serialize(self, param1):
        self.serializeAs_HouseInstanceInformations(param1)

    def serializeAs_HouseInstanceInformations(self, param1):
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.secondHand)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.isLocked)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,2,self.isSaleLocked)
        param1.write_byte(_loc2_)
        if self.instanceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element instanceId.")
        param1.write_int(self.instanceId)
        param1.write_utf(self.ownerName)
        if self.price < -9007199254740990 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element price.")
        param1.write_var_long(self.price)

    def deserialize(self, param1):
        self.deserializeAs_HouseInstanceInformations(param1)

    def deserializeAs_HouseInstanceInformations(self, param1):
        self.deserializeByteBoxes(param1)
        self._instanceIdFunc(param1)
        self._ownerNameFunc(param1)
        self._priceFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HouseInstanceInformations(param1)

    def deserializeAsyncAs_HouseInstanceInformations(self, param1):
        param1.add_child(self.deserializeByteBoxes)
        param1.add_child(self._instanceIdFunc)
        param1.add_child(self._ownerNameFunc)
        param1.add_child(self._priceFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.secondHand = BooleanByteWrapper.get_flag(_loc2_,0)
        self.isLocked = BooleanByteWrapper.get_flag(_loc2_,1)
        self.isSaleLocked = BooleanByteWrapper.get_flag(_loc2_,2)

    def _instanceIdFunc(self, param1):
        self.instanceId = param1.read_int()
        if self.instanceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of HouseInstanceInformations.instanceId.")

    def _ownerNameFunc(self, param1):
        self.ownerName = param1.read_utf()

    def _priceFunc(self, param1):
        self.price = param1.read_var_long()
        if self.price < -9007199254740990 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of HouseInstanceInformations.price.")


class Idol():
    protocolId = 489

    def __init__(self):
        super().__init__()
        self.id = 0
        self.xpBonusPercent = 0
        self.dropBonusPercent = 0

    def getTypeId(self):
        return 489

    def initIdol(self, param1=0, param2=0, param3=0):
        self.id = param1
        self.xpBonusPercent = param2
        self.dropBonusPercent = param3
        return self

    def reset(self):
        self.id = 0
        self.xpBonusPercent = 0
        self.dropBonusPercent = 0

    def serialize(self, param1):
        self.serializeAs_Idol(param1)

    def serializeAs_Idol(self, param1):
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_var_short(self.id)
        if self.xpBonusPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.xpBonusPercent) + ") on element xpBonusPercent.")
        param1.write_var_short(self.xpBonusPercent)
        if self.dropBonusPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.dropBonusPercent) + ") on element dropBonusPercent.")
        param1.write_var_short(self.dropBonusPercent)

    def deserialize(self, param1):
        self.deserializeAs_Idol(param1)

    def deserializeAs_Idol(self, param1):
        self._idFunc(param1)
        self._xpBonusPercentFunc(param1)
        self._dropBonusPercentFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_Idol(param1)

    def deserializeAsyncAs_Idol(self, param1):
        param1.add_child(self._idFunc)
        param1.add_child(self._xpBonusPercentFunc)
        param1.add_child(self._dropBonusPercentFunc)

    def _idFunc(self, param1):
        self.id = param1.read_var_uh_short()
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of Idol.id.")

    def _xpBonusPercentFunc(self, param1):
        self.xpBonusPercent = param1.read_var_uh_short()
        if self.xpBonusPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.xpBonusPercent) + ") on element of Idol.xpBonusPercent.")

    def _dropBonusPercentFunc(self, param1):
        self.dropBonusPercent = param1.read_var_uh_short()
        if self.dropBonusPercent < 0:
            raise RuntimeError("Forbidden value (" + str(self.dropBonusPercent) + ") on element of Idol.dropBonusPercent.")


class InteractiveElement():
    protocolId = 80

    def __init__(self):
        super().__init__()
        self.elementId = 0
        self.elementTypeId = 0
        self.enabledSkills = []
        self.disabledSkills = []
        self.onCurrentMap = False
        self._enabledSkillstree = FuncTree()
        self._disabledSkillstree = FuncTree()

    def getTypeId(self):
        return 80

    def initInteractiveElement(self, param1=0, param2=0, param3=[], param4=[], param5=False):
        self.elementId = param1
        self.elementTypeId = param2
        self.enabledSkills = param3
        self.disabledSkills = param4
        self.onCurrentMap = param5
        return self

    def reset(self):
        self.elementId = 0
        self.elementTypeId = 0
        self.enabledSkills = []
        self.disabledSkills = []
        self.onCurrentMap = False

    def serialize(self, param1):
        self.serializeAs_InteractiveElement(param1)

    def serializeAs_InteractiveElement(self, param1):
        if self.elementId < 0:
            raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element elementId.")
        param1.write_int(self.elementId)
        param1.write_int(self.elementTypeId)
        param1.write_short(len(self.enabledSkills))
        _loc2_ = 0
        while _loc2_ < len(self.enabledSkills):
            param1.write_short(as_parent(self.enabledSkills[_loc2_], InteractiveElementSkill).getTypeId())
            as_parent(self.enabledSkills[_loc2_], InteractiveElementSkill).serialize(param1)
            _loc2_ += 1
        param1.write_short(len(self.disabledSkills))
        _loc3_ = 0
        while _loc3_ < len(self.disabledSkills):
            param1.write_short(as_parent(self.disabledSkills[_loc3_], InteractiveElementSkill).getTypeId())
            as_parent(self.disabledSkills[_loc3_], InteractiveElementSkill).serialize(param1)
            _loc3_ += 1
        param1.write_boolean(self.onCurrentMap)

    def deserialize(self, param1):
        self.deserializeAs_InteractiveElement(param1)

    def deserializeAs_InteractiveElement(self, param1):
        _loc6_ = 0
        _loc7_ = None
        _loc8_ = 0
        _loc9_ = None
        self._elementIdFunc(param1)
        self._elementTypeIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_unsigned_short()
            _loc7_ = ProtocolTypeManager.get_instance(InteractiveElementSkill,_loc6_)
            _loc7_.deserialize(param1)
            self.enabledSkills.append(_loc7_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc8_ = param1.read_unsigned_short()
            _loc9_ = ProtocolTypeManager.get_instance(InteractiveElementSkill,_loc8_)
            _loc9_.deserialize(param1)
            self.disabledSkills.append(_loc9_)
            _loc5_ += 1
        self._onCurrentMapFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_InteractiveElement(param1)

    def deserializeAsyncAs_InteractiveElement(self, param1):
        param1.add_child(self._elementIdFunc)
        param1.add_child(self._elementTypeIdFunc)
        self._enabledSkillstree = param1.add_child(self._enabledSkillstreeFunc)
        self._disabledSkillstree = param1.add_child(self._disabledSkillstreeFunc)
        param1.add_child(self._onCurrentMapFunc)

    def _elementIdFunc(self, param1):
        self.elementId = param1.read_int()
        if self.elementId < 0:
            raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element of InteractiveElement.elementId.")

    def _elementTypeIdFunc(self, param1):
        self.elementTypeId = param1.read_int()

    def _enabledSkillstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._enabledSkillstree.add_child(self._enabledSkillsFunc)
            _loc3_ += 1

    def _enabledSkillsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(InteractiveElementSkill,_loc2_)
        _loc3_.deserialize(param1)
        self.enabledSkills.append(_loc3_)

    def _disabledSkillstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._disabledSkillstree.add_child(self._disabledSkillsFunc)
            _loc3_ += 1

    def _disabledSkillsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(InteractiveElementSkill,_loc2_)
        _loc3_.deserialize(param1)
        self.disabledSkills.append(_loc3_)

    def _onCurrentMapFunc(self, param1):
        self.onCurrentMap = param1.read_boolean()


class InteractiveElementSkill():
    protocolId = 219

    def __init__(self):
        super().__init__()
        self.skillId = 0
        self.skillInstanceUid = 0

    def getTypeId(self):
        return 219

    def initInteractiveElementSkill(self, param1=0, param2=0):
        self.skillId = param1
        self.skillInstanceUid = param2
        return self

    def reset(self):
        self.skillId = 0
        self.skillInstanceUid = 0

    def serialize(self, param1):
        self.serializeAs_InteractiveElementSkill(param1)

    def serializeAs_InteractiveElementSkill(self, param1):
        if self.skillId < 0:
            raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element skillId.")
        param1.write_var_int(self.skillId)
        if self.skillInstanceUid < 0:
            raise RuntimeError("Forbidden value (" + str(self.skillInstanceUid) + ") on element skillInstanceUid.")
        param1.write_int(self.skillInstanceUid)

    def deserialize(self, param1):
        self.deserializeAs_InteractiveElementSkill(param1)

    def deserializeAs_InteractiveElementSkill(self, param1):
        self._skillIdFunc(param1)
        self._skillInstanceUidFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_InteractiveElementSkill(param1)

    def deserializeAsyncAs_InteractiveElementSkill(self, param1):
        param1.add_child(self._skillIdFunc)
        param1.add_child(self._skillInstanceUidFunc)

    def _skillIdFunc(self, param1):
        self.skillId = param1.read_var_uh_int()
        if self.skillId < 0:
            raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of InteractiveElementSkill.skillId.")

    def _skillInstanceUidFunc(self, param1):
        self.skillInstanceUid = param1.read_int()
        if self.skillInstanceUid < 0:
            raise RuntimeError("Forbidden value (" + str(self.skillInstanceUid) + ") on element of InteractiveElementSkill.skillInstanceUid.")


class MapObstacle():
    protocolId = 200

    def __init__(self):
        super().__init__()
        self.obstacleCellId = 0
        self.state = 0

    def getTypeId(self):
        return 200

    def initMapObstacle(self, param1=0, param2=0):
        self.obstacleCellId = param1
        self.state = param2
        return self

    def reset(self):
        self.obstacleCellId = 0
        self.state = 0

    def serialize(self, param1):
        self.serializeAs_MapObstacle(param1)

    def serializeAs_MapObstacle(self, param1):
        if self.obstacleCellId < 0 or self.obstacleCellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.obstacleCellId) + ") on element obstacleCellId.")
        param1.write_var_short(self.obstacleCellId)
        param1.write_byte(self.state)

    def deserialize(self, param1):
        self.deserializeAs_MapObstacle(param1)

    def deserializeAs_MapObstacle(self, param1):
        self._obstacleCellIdFunc(param1)
        self._stateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MapObstacle(param1)

    def deserializeAsyncAs_MapObstacle(self, param1):
        param1.add_child(self._obstacleCellIdFunc)
        param1.add_child(self._stateFunc)

    def _obstacleCellIdFunc(self, param1):
        self.obstacleCellId = param1.read_var_uh_short()
        if self.obstacleCellId < 0 or self.obstacleCellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.obstacleCellId) + ") on element of MapObstacle.obstacleCellId.")

    def _stateFunc(self, param1):
        self.state = param1.read_byte()
        if self.state < 0:
            raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of MapObstacle.state.")


class StatedElement():
    protocolId = 108

    def __init__(self):
        super().__init__()
        self.elementId = 0
        self.elementCellId = 0
        self.elementState = 0
        self.onCurrentMap = False

    def getTypeId(self):
        return 108

    def initStatedElement(self, param1=0, param2=0, param3=0, param4=False):
        self.elementId = param1
        self.elementCellId = param2
        self.elementState = param3
        self.onCurrentMap = param4
        return self

    def reset(self):
        self.elementId = 0
        self.elementCellId = 0
        self.elementState = 0
        self.onCurrentMap = False

    def serialize(self, param1):
        self.serializeAs_StatedElement(param1)

    def serializeAs_StatedElement(self, param1):
        if self.elementId < 0:
            raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element elementId.")
        param1.write_int(self.elementId)
        if self.elementCellId < 0 or self.elementCellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.elementCellId) + ") on element elementCellId.")
        param1.write_var_short(self.elementCellId)
        if self.elementState < 0:
            raise RuntimeError("Forbidden value (" + str(self.elementState) + ") on element elementState.")
        param1.write_var_int(self.elementState)
        param1.write_boolean(self.onCurrentMap)

    def deserialize(self, param1):
        self.deserializeAs_StatedElement(param1)

    def deserializeAs_StatedElement(self, param1):
        self._elementIdFunc(param1)
        self._elementCellIdFunc(param1)
        self._elementStateFunc(param1)
        self._onCurrentMapFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_StatedElement(param1)

    def deserializeAsyncAs_StatedElement(self, param1):
        param1.add_child(self._elementIdFunc)
        param1.add_child(self._elementCellIdFunc)
        param1.add_child(self._elementStateFunc)
        param1.add_child(self._onCurrentMapFunc)

    def _elementIdFunc(self, param1):
        self.elementId = param1.read_int()
        if self.elementId < 0:
            raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element of StatedElement.elementId.")

    def _elementCellIdFunc(self, param1):
        self.elementCellId = param1.read_var_uh_short()
        if self.elementCellId < 0 or self.elementCellId > 559:
            raise RuntimeError("Forbidden value (" + str(self.elementCellId) + ") on element of StatedElement.elementCellId.")

    def _elementStateFunc(self, param1):
        self.elementState = param1.read_var_uh_int()
        if self.elementState < 0:
            raise RuntimeError("Forbidden value (" + str(self.elementState) + ") on element of StatedElement.elementState.")

    def _onCurrentMapFunc(self, param1):
        self.onCurrentMap = param1.read_boolean()


class SkillActionDescription():
    protocolId = 102

    def __init__(self):
        super().__init__()
        self.skillId = 0

    def getTypeId(self):
        return 102

    def initSkillActionDescription(self, param1=0):
        self.skillId = param1
        return self

    def reset(self):
        self.skillId = 0

    def serialize(self, param1):
        self.serializeAs_SkillActionDescription(param1)

    def serializeAs_SkillActionDescription(self, param1):
        if self.skillId < 0:
            raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element skillId.")
        param1.write_var_short(self.skillId)

    def deserialize(self, param1):
        self.deserializeAs_SkillActionDescription(param1)

    def deserializeAs_SkillActionDescription(self, param1):
        self._skillIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_SkillActionDescription(param1)

    def deserializeAsyncAs_SkillActionDescription(self, param1):
        param1.add_child(self._skillIdFunc)

    def _skillIdFunc(self, param1):
        self.skillId = param1.read_var_uh_short()
        if self.skillId < 0:
            raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of SkillActionDescription.skillId.")


class IdolsPreset():
    protocolId = 491

    def __init__(self):
        super().__init__()
        self.presetId = 0
        self.symbolId = 0
        self.idolId = []
        self._idolIdtree = FuncTree()

    def getTypeId(self):
        return 491

    def initIdolsPreset(self, param1=0, param2=0, param3=[]):
        self.presetId = param1
        self.symbolId = param2
        self.idolId = param3
        return self

    def reset(self):
        self.presetId = 0
        self.symbolId = 0
        self.idolId = []

    def serialize(self, param1):
        self.serializeAs_IdolsPreset(param1)

    def serializeAs_IdolsPreset(self, param1):
        if self.presetId < 0:
            raise RuntimeError("Forbidden value (" + str(self.presetId) + ") on element presetId.")
        param1.write_byte(self.presetId)
        if self.symbolId < 0:
            raise RuntimeError("Forbidden value (" + str(self.symbolId) + ") on element symbolId.")
        param1.write_byte(self.symbolId)
        param1.write_short(len(self.idolId))
        _loc2_ = 0
        while _loc2_ < len(self.idolId):
            if self.idolId[_loc2_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.idolId[_loc2_]) + ") on element 3 (starting at 1) of idolId.")
            param1.write_var_short(self.idolId[_loc2_])
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_IdolsPreset(param1)

    def deserializeAs_IdolsPreset(self, param1):
        _loc4_ = 0
        self._presetIdFunc(param1)
        self._symbolIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_var_uh_short()
            if _loc4_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc4_) + ") on elements of idolId.")
            self.idolId.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_IdolsPreset(param1)

    def deserializeAsyncAs_IdolsPreset(self, param1):
        param1.add_child(self._presetIdFunc)
        param1.add_child(self._symbolIdFunc)
        self._idolIdtree = param1.add_child(self._idolIdtreeFunc)

    def _presetIdFunc(self, param1):
        self.presetId = param1.read_byte()
        if self.presetId < 0:
            raise RuntimeError("Forbidden value (" + str(self.presetId) + ") on element of IdolsPreset.presetId.")

    def _symbolIdFunc(self, param1):
        self.symbolId = param1.read_byte()
        if self.symbolId < 0:
            raise RuntimeError("Forbidden value (" + str(self.symbolId) + ") on element of IdolsPreset.symbolId.")

    def _idolIdtreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._idolIdtree.add_child(self._idolIdFunc)
            _loc3_ += 1

    def _idolIdFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of idolId.")
        self.idolId.append(_loc2_)


class Preset():
    protocolId = 355

    def __init__(self):
        super().__init__()
        self.presetId = 0
        self.symbolId = 0
        self.mount = False
        self.objects = []
        self._objectstree = FuncTree()

    def getTypeId(self):
        return 355

    def initPreset(self, param1=0, param2=0, param3=False, param4=[]):
        self.presetId = param1
        self.symbolId = param2
        self.mount = param3
        self.objects = param4
        return self

    def reset(self):
        self.presetId = 0
        self.symbolId = 0
        self.mount = False
        self.objects = []

    def serialize(self, param1):
        self.serializeAs_Preset(param1)

    def serializeAs_Preset(self, param1):
        if self.presetId < 0:
            raise RuntimeError("Forbidden value (" + str(self.presetId) + ") on element presetId.")
        param1.write_byte(self.presetId)
        if self.symbolId < 0:
            raise RuntimeError("Forbidden value (" + str(self.symbolId) + ") on element symbolId.")
        param1.write_byte(self.symbolId)
        param1.write_boolean(self.mount)
        param1.write_short(len(self.objects))
        _loc2_ = 0
        while _loc2_ < len(self.objects):
            as_parent(self.objects[_loc2_], PresetItem).serializeAs_PresetItem(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_Preset(param1)

    def deserializeAs_Preset(self, param1):
        _loc4_ = None
        self._presetIdFunc(param1)
        self._symbolIdFunc(param1)
        self._mountFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = PresetItem()
            _loc4_.deserialize(param1)
            self.objects.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_Preset(param1)

    def deserializeAsyncAs_Preset(self, param1):
        param1.add_child(self._presetIdFunc)
        param1.add_child(self._symbolIdFunc)
        param1.add_child(self._mountFunc)
        self._objectstree = param1.add_child(self._objectstreeFunc)

    def _presetIdFunc(self, param1):
        self.presetId = param1.read_byte()
        if self.presetId < 0:
            raise RuntimeError("Forbidden value (" + str(self.presetId) + ") on element of Preset.presetId.")

    def _symbolIdFunc(self, param1):
        self.symbolId = param1.read_byte()
        if self.symbolId < 0:
            raise RuntimeError("Forbidden value (" + str(self.symbolId) + ") on element of Preset.symbolId.")

    def _mountFunc(self, param1):
        self.mount = param1.read_boolean()

    def _objectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._objectstree.add_child(self._objectsFunc)
            _loc3_ += 1

    def _objectsFunc(self, param1):
        _loc2_ = PresetItem()
        _loc2_.deserialize(param1)
        self.objects.append(_loc2_)


class PresetItem():
    protocolId = 354

    def __init__(self):
        super().__init__()
        self.position = 63
        self.objGid = 0
        self.objUid = 0

    def getTypeId(self):
        return 354

    def initPresetItem(self, param1=63, param2=0, param3=0):
        self.position = param1
        self.objGid = param2
        self.objUid = param3
        return self

    def reset(self):
        self.position = 63
        self.objGid = 0
        self.objUid = 0

    def serialize(self, param1):
        self.serializeAs_PresetItem(param1)

    def serializeAs_PresetItem(self, param1):
        param1.write_byte(self.position)
        if self.objGid < 0:
            raise RuntimeError("Forbidden value (" + str(self.objGid) + ") on element objGid.")
        param1.write_var_short(self.objGid)
        if self.objUid < 0:
            raise RuntimeError("Forbidden value (" + str(self.objUid) + ") on element objUid.")
        param1.write_var_int(self.objUid)

    def deserialize(self, param1):
        self.deserializeAs_PresetItem(param1)

    def deserializeAs_PresetItem(self, param1):
        self._positionFunc(param1)
        self._objGidFunc(param1)
        self._objUidFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PresetItem(param1)

    def deserializeAsyncAs_PresetItem(self, param1):
        param1.add_child(self._positionFunc)
        param1.add_child(self._objGidFunc)
        param1.add_child(self._objUidFunc)

    def _positionFunc(self, param1):
        self.position = param1.read_unsigned_byte()
        if self.position < 0 or self.position > 255:
            raise RuntimeError("Forbidden value (" + str(self.position) + ") on element of PresetItem.position.")

    def _objGidFunc(self, param1):
        self.objGid = param1.read_var_uh_short()
        if self.objGid < 0:
            raise RuntimeError("Forbidden value (" + str(self.objGid) + ") on element of PresetItem.objGid.")

    def _objUidFunc(self, param1):
        self.objUid = param1.read_var_uh_int()
        if self.objUid < 0:
            raise RuntimeError("Forbidden value (" + str(self.objUid) + ") on element of PresetItem.objUid.")


class EntityLook():
    protocolId = 55

    def __init__(self):
        super().__init__()
        self.bonesId = 0
        self.skins = []
        self.indexedColors = []
        self.scales = []
        self.subentities = []
        self._skinstree = FuncTree()
        self._indexedColorstree = FuncTree()
        self._scalestree = FuncTree()
        self._subentitiestree = FuncTree()

    def getTypeId(self):
        return 55

    def initEntityLook(self, param1=0, param2=[], param3=[], param4=[], param5=[]):
        self.bonesId = param1
        self.skins = param2
        self.indexedColors = param3
        self.scales = param4
        self.subentities = param5
        return self

    def reset(self):
        self.bonesId = 0
        self.skins = []
        self.indexedColors = []
        self.scales = []
        self.subentities = []

    def serialize(self, param1):
        self.serializeAs_EntityLook(param1)

    def serializeAs_EntityLook(self, param1):
        if self.bonesId < 0:
            raise RuntimeError("Forbidden value (" + str(self.bonesId) + ") on element bonesId.")
        param1.write_var_short(self.bonesId)
        param1.write_short(len(self.skins))
        _loc2_ = 0
        while _loc2_ < len(self.skins):
            if self.skins[_loc2_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.skins[_loc2_]) + ") on element 2 (starting at 1) of skins.")
            param1.write_var_short(self.skins[_loc2_])
            _loc2_ += 1
        param1.write_short(len(self.indexedColors))
        _loc3_ = 0
        while _loc3_ < len(self.indexedColors):
            param1.write_int(self.indexedColors[_loc3_])
            _loc3_ += 1
        param1.write_short(len(self.scales))
        _loc4_ = 0
        while _loc4_ < len(self.scales):
            param1.write_var_short(self.scales[_loc4_])
            _loc4_ += 1
        param1.write_short(len(self.subentities))
        _loc5_ = 0
        while _loc5_ < len(self.subentities):
            as_parent(self.subentities[_loc5_], SubEntity).serializeAs_SubEntity(param1)
            _loc5_ += 1

    def deserialize(self, param1):
        self.deserializeAs_EntityLook(param1)

    def deserializeAs_EntityLook(self, param1):
        _loc10_ = 0
        _loc11_ = 0
        _loc12_ = 0
        _loc13_ = None
        self._bonesIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc10_ = param1.read_var_uh_short()
            if _loc10_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc10_) + ") on elements of skins.")
            self.skins.append(_loc10_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc11_ = param1.read_int()
            self.indexedColors.append(_loc11_)
            _loc5_ += 1
        _loc6_ = param1.read_unsigned_short()
        _loc7_ = 0
        while _loc7_ < _loc6_:
            _loc12_ = param1.read_var_short()
            self.scales.append(_loc12_)
            _loc7_ += 1
        _loc8_ = param1.read_unsigned_short()
        _loc9_ = 0
        while _loc9_ < _loc8_:
            _loc13_ = SubEntity()
            _loc13_.deserialize(param1)
            self.subentities.append(_loc13_)
            _loc9_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_EntityLook(param1)

    def deserializeAsyncAs_EntityLook(self, param1):
        param1.add_child(self._bonesIdFunc)
        self._skinstree = param1.add_child(self._skinstreeFunc)
        self._indexedColorstree = param1.add_child(self._indexedColorstreeFunc)
        self._scalestree = param1.add_child(self._scalestreeFunc)
        self._subentitiestree = param1.add_child(self._subentitiestreeFunc)

    def _bonesIdFunc(self, param1):
        self.bonesId = param1.read_var_uh_short()
        if self.bonesId < 0:
            raise RuntimeError("Forbidden value (" + str(self.bonesId) + ") on element of EntityLook.bonesId.")

    def _skinstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._skinstree.add_child(self._skinsFunc)
            _loc3_ += 1

    def _skinsFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of skins.")
        self.skins.append(_loc2_)

    def _indexedColorstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._indexedColorstree.add_child(self._indexedColorsFunc)
            _loc3_ += 1

    def _indexedColorsFunc(self, param1):
        _loc2_ = param1.read_int()
        self.indexedColors.append(_loc2_)

    def _scalestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._scalestree.add_child(self._scalesFunc)
            _loc3_ += 1

    def _scalesFunc(self, param1):
        _loc2_ = param1.read_var_short()
        self.scales.append(_loc2_)

    def _subentitiestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._subentitiestree.add_child(self._subentitiesFunc)
            _loc3_ += 1

    def _subentitiesFunc(self, param1):
        _loc2_ = SubEntity()
        _loc2_.deserialize(param1)
        self.subentities.append(_loc2_)


class IndexedEntityLook():
    protocolId = 405

    def __init__(self):
        super().__init__()
        self.look = EntityLook()
        self.index = 0
        self._looktree = FuncTree()

    def getTypeId(self):
        return 405

    def initIndexedEntityLook(self, param1=None, param2=0):
        self.look = param1
        self.index = param2
        return self

    def reset(self):
        self.look = EntityLook()

    def serialize(self, param1):
        self.serializeAs_IndexedEntityLook(param1)

    def serializeAs_IndexedEntityLook(self, param1):
        self.look.serializeAs_EntityLook(param1)
        if self.index < 0:
            raise RuntimeError("Forbidden value (" + str(self.index) + ") on element index.")
        param1.write_byte(self.index)

    def deserialize(self, param1):
        self.deserializeAs_IndexedEntityLook(param1)

    def deserializeAs_IndexedEntityLook(self, param1):
        self.look = EntityLook()
        self.look.deserialize(param1)
        self._indexFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_IndexedEntityLook(param1)

    def deserializeAsyncAs_IndexedEntityLook(self, param1):
        self._looktree = param1.add_child(self._looktreeFunc)
        param1.add_child(self._indexFunc)

    def _looktreeFunc(self, param1):
        self.look = EntityLook()
        self.look.deserializeAsync(self._looktree)

    def _indexFunc(self, param1):
        self.index = param1.read_byte()
        if self.index < 0:
            raise RuntimeError("Forbidden value (" + str(self.index) + ") on element of IndexedEntityLook.index.")


class SubEntity():
    protocolId = 54

    def __init__(self):
        super().__init__()
        self.bindingPointCategory = 0
        self.bindingPointIndex = 0
        self.subEntityLook = EntityLook()
        self._subEntityLooktree = FuncTree()

    def getTypeId(self):
        return 54

    def initSubEntity(self, param1=0, param2=0, param3=None):
        self.bindingPointCategory = param1
        self.bindingPointIndex = param2
        self.subEntityLook = param3
        return self

    def reset(self):
        self.bindingPointCategory = 0
        self.bindingPointIndex = 0
        self.subEntityLook = EntityLook()

    def serialize(self, param1):
        self.serializeAs_SubEntity(param1)

    def serializeAs_SubEntity(self, param1):
        param1.write_byte(self.bindingPointCategory)
        if self.bindingPointIndex < 0:
            raise RuntimeError("Forbidden value (" + str(self.bindingPointIndex) + ") on element bindingPointIndex.")
        param1.write_byte(self.bindingPointIndex)
        self.subEntityLook.serializeAs_EntityLook(param1)

    def deserialize(self, param1):
        self.deserializeAs_SubEntity(param1)

    def deserializeAs_SubEntity(self, param1):
        self._bindingPointCategoryFunc(param1)
        self._bindingPointIndexFunc(param1)
        self.subEntityLook = EntityLook()
        self.subEntityLook.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_SubEntity(param1)

    def deserializeAsyncAs_SubEntity(self, param1):
        param1.add_child(self._bindingPointCategoryFunc)
        param1.add_child(self._bindingPointIndexFunc)
        self._subEntityLooktree = param1.add_child(self._subEntityLooktreeFunc)

    def _bindingPointCategoryFunc(self, param1):
        self.bindingPointCategory = param1.read_byte()
        if self.bindingPointCategory < 0:
            raise RuntimeError("Forbidden value (" + str(self.bindingPointCategory) + ") on element of SubEntity.bindingPointCategory.")

    def _bindingPointIndexFunc(self, param1):
        self.bindingPointIndex = param1.read_byte()
        if self.bindingPointIndex < 0:
            raise RuntimeError("Forbidden value (" + str(self.bindingPointIndex) + ") on element of SubEntity.bindingPointIndex.")

    def _subEntityLooktreeFunc(self, param1):
        self.subEntityLook = EntityLook()
        self.subEntityLook.deserializeAsync(self._subEntityLooktree)


class ItemDurability():
    protocolId = 168

    def __init__(self):
        super().__init__()
        self.durability = 0
        self.durabilityMax = 0

    def getTypeId(self):
        return 168

    def initItemDurability(self, param1=0, param2=0):
        self.durability = param1
        self.durabilityMax = param2
        return self

    def reset(self):
        self.durability = 0
        self.durabilityMax = 0

    def serialize(self, param1):
        self.serializeAs_ItemDurability(param1)

    def serializeAs_ItemDurability(self, param1):
        param1.write_short(self.durability)
        param1.write_short(self.durabilityMax)

    def deserialize(self, param1):
        self.deserializeAs_ItemDurability(param1)

    def deserializeAs_ItemDurability(self, param1):
        self._durabilityFunc(param1)
        self._durabilityMaxFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ItemDurability(param1)

    def deserializeAsyncAs_ItemDurability(self, param1):
        param1.add_child(self._durabilityFunc)
        param1.add_child(self._durabilityMaxFunc)

    def _durabilityFunc(self, param1):
        self.durability = param1.read_short()

    def _durabilityMaxFunc(self, param1):
        self.durabilityMax = param1.read_short()


class MountClientData():
    protocolId = 178

    def __init__(self):
        super().__init__()
        self.id = 0
        self.model = 0
        self.ancestor = []
        self.behaviors = []
        self.name = ""
        self.sex = False
        self.ownerId = 0
        self.experience = 0
        self.experienceForLevel = 0
        self.experienceForNextLevel = 0
        self.level = 0
        self.isRideable = False
        self.maxPods = 0
        self.isWild = False
        self.stamina = 0
        self.staminaMax = 0
        self.maturity = 0
        self.maturityForAdult = 0
        self.energy = 0
        self.energyMax = 0
        self.serenity = 0
        self.aggressivityMax = 0
        self.serenityMax = 0
        self.love = 0
        self.loveMax = 0
        self.fecondationTime = 0
        self.isFecondationReady = False
        self.boostLimiter = 0
        self.boostMax = 0
        self.reproductionCount = 0
        self.reproductionCountMax = 0
        self.harnessGID = 0
        self.useHarnessColors = False
        self.effectList = []
        self._ancestortree = FuncTree()
        self._behaviorstree = FuncTree()
        self._effectListtree = FuncTree()

    def getTypeId(self):
        return 178

    def initMountClientData(self, param1=0, param2=0, param3=[], param4=[], param5="", param6=False, param7=0, param8=0, param9=0, param10=0, param11=0, param12=False, param13=0, param14=False, param15=0, param16=0, param17=0, param18=0, param19=0, param20=0, param21=0, param22=0, param23=0, param24=0, param25=0, param26=0, param27=False, param28=0, param29=0, param30=0, param31=0, param32=0, param33=False, param34=[]):
        self.id = param1
        self.model = param2
        self.ancestor = param3
        self.behaviors = param4
        self.name = param5
        self.sex = param6
        self.ownerId = param7
        self.experience = param8
        self.experienceForLevel = param9
        self.experienceForNextLevel = param10
        self.level = param11
        self.isRideable = param12
        self.maxPods = param13
        self.isWild = param14
        self.stamina = param15
        self.staminaMax = param16
        self.maturity = param17
        self.maturityForAdult = param18
        self.energy = param19
        self.energyMax = param20
        self.serenity = param21
        self.aggressivityMax = param22
        self.serenityMax = param23
        self.love = param24
        self.loveMax = param25
        self.fecondationTime = param26
        self.isFecondationReady = param27
        self.boostLimiter = param28
        self.boostMax = param29
        self.reproductionCount = param30
        self.reproductionCountMax = param31
        self.harnessGID = param32
        self.useHarnessColors = param33
        self.effectList = param34
        return self

    def reset(self):
        self.id = 0
        self.model = 0
        self.ancestor = []
        self.behaviors = []
        self.name = ""
        self.sex = False
        self.ownerId = 0
        self.experience = 0
        self.experienceForLevel = 0
        self.experienceForNextLevel = 0
        self.level = 0
        self.isRideable = False
        self.maxPods = 0
        self.isWild = False
        self.stamina = 0
        self.staminaMax = 0
        self.maturity = 0
        self.maturityForAdult = 0
        self.energy = 0
        self.energyMax = 0
        self.serenity = 0
        self.aggressivityMax = 0
        self.serenityMax = 0
        self.love = 0
        self.loveMax = 0
        self.fecondationTime = 0
        self.isFecondationReady = False
        self.boostLimiter = 0
        self.boostMax = 0
        self.reproductionCount = 0
        self.reproductionCountMax = 0
        self.harnessGID = 0
        self.useHarnessColors = False
        self.effectList = []

    def serialize(self, param1):
        self.serializeAs_MountClientData(param1)

    def serializeAs_MountClientData(self, param1):
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.sex)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.isRideable)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,2,self.isWild)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,3,self.isFecondationReady)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,4,self.useHarnessColors)
        param1.write_byte(_loc2_)
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_double(self.id)
        if self.model < 0:
            raise RuntimeError("Forbidden value (" + str(self.model) + ") on element model.")
        param1.write_var_int(self.model)
        param1.write_short(len(self.ancestor))
        _loc3_ = 0
        while _loc3_ < len(self.ancestor):
            if self.ancestor[_loc3_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.ancestor[_loc3_]) + ") on element 3 (starting at 1) of ancestor.")
            param1.write_int(self.ancestor[_loc3_])
            _loc3_ += 1
        param1.write_short(len(self.behaviors))
        _loc4_ = 0
        while _loc4_ < len(self.behaviors):
            if self.behaviors[_loc4_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.behaviors[_loc4_]) + ") on element 4 (starting at 1) of behaviors.")
            param1.write_int(self.behaviors[_loc4_])
            _loc4_ += 1
        param1.write_utf(self.name)
        if self.ownerId < 0:
            raise RuntimeError("Forbidden value (" + str(self.ownerId) + ") on element ownerId.")
        param1.write_int(self.ownerId)
        if self.experience < 0 or self.experience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element experience.")
        param1.write_var_long(self.experience)
        if self.experienceForLevel < 0 or self.experienceForLevel > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceForLevel) + ") on element experienceForLevel.")
        param1.write_var_long(self.experienceForLevel)
        if self.experienceForNextLevel < -9007199254740990 or self.experienceForNextLevel > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceForNextLevel) + ") on element experienceForNextLevel.")
        param1.write_double(self.experienceForNextLevel)
        if self.level < 0:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)
        if self.maxPods < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxPods) + ") on element maxPods.")
        param1.write_var_int(self.maxPods)
        if self.stamina < 0:
            raise RuntimeError("Forbidden value (" + str(self.stamina) + ") on element stamina.")
        param1.write_var_int(self.stamina)
        if self.staminaMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.staminaMax) + ") on element staminaMax.")
        param1.write_var_int(self.staminaMax)
        if self.maturity < 0:
            raise RuntimeError("Forbidden value (" + str(self.maturity) + ") on element maturity.")
        param1.write_var_int(self.maturity)
        if self.maturityForAdult < 0:
            raise RuntimeError("Forbidden value (" + str(self.maturityForAdult) + ") on element maturityForAdult.")
        param1.write_var_int(self.maturityForAdult)
        if self.energy < 0:
            raise RuntimeError("Forbidden value (" + str(self.energy) + ") on element energy.")
        param1.write_var_int(self.energy)
        if self.energyMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.energyMax) + ") on element energyMax.")
        param1.write_var_int(self.energyMax)
        param1.write_int(self.serenity)
        param1.write_int(self.aggressivityMax)
        if self.serenityMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.serenityMax) + ") on element serenityMax.")
        param1.write_var_int(self.serenityMax)
        if self.love < 0:
            raise RuntimeError("Forbidden value (" + str(self.love) + ") on element love.")
        param1.write_var_int(self.love)
        if self.loveMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.loveMax) + ") on element loveMax.")
        param1.write_var_int(self.loveMax)
        param1.write_int(self.fecondationTime)
        if self.boostLimiter < 0:
            raise RuntimeError("Forbidden value (" + str(self.boostLimiter) + ") on element boostLimiter.")
        param1.write_int(self.boostLimiter)
        if self.boostMax < -9007199254740990 or self.boostMax > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.boostMax) + ") on element boostMax.")
        param1.write_double(self.boostMax)
        param1.write_int(self.reproductionCount)
        if self.reproductionCountMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.reproductionCountMax) + ") on element reproductionCountMax.")
        param1.write_var_int(self.reproductionCountMax)
        if self.harnessGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.harnessGID) + ") on element harnessGID.")
        param1.write_var_short(self.harnessGID)
        param1.write_short(len(self.effectList))
        _loc5_ = 0
        while _loc5_ < len(self.effectList):
            as_parent(self.effectList[_loc5_], ObjectEffectInteger).serializeAs_ObjectEffectInteger(param1)
            _loc5_ += 1

    def deserialize(self, param1):
        self.deserializeAs_MountClientData(param1)

    def deserializeAs_MountClientData(self, param1):
        _loc8_ = 0
        _loc9_ = 0
        _loc10_ = None
        self.deserializeByteBoxes(param1)
        self._idFunc(param1)
        self._modelFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc8_ = param1.read_int()
            if _loc8_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc8_) + ") on elements of ancestor.")
            self.ancestor.append(_loc8_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc9_ = param1.read_int()
            if _loc9_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc9_) + ") on elements of behaviors.")
            self.behaviors.append(_loc9_)
            _loc5_ += 1
        self._nameFunc(param1)
        self._ownerIdFunc(param1)
        self._experienceFunc(param1)
        self._experienceForLevelFunc(param1)
        self._experienceForNextLevelFunc(param1)
        self._levelFunc(param1)
        self._maxPodsFunc(param1)
        self._staminaFunc(param1)
        self._staminaMaxFunc(param1)
        self._maturityFunc(param1)
        self._maturityForAdultFunc(param1)
        self._energyFunc(param1)
        self._energyMaxFunc(param1)
        self._serenityFunc(param1)
        self._aggressivityMaxFunc(param1)
        self._serenityMaxFunc(param1)
        self._loveFunc(param1)
        self._loveMaxFunc(param1)
        self._fecondationTimeFunc(param1)
        self._boostLimiterFunc(param1)
        self._boostMaxFunc(param1)
        self._reproductionCountFunc(param1)
        self._reproductionCountMaxFunc(param1)
        self._harnessGIDFunc(param1)
        _loc6_ = param1.read_unsigned_short()
        _loc7_ = 0
        while _loc7_ < _loc6_:
            _loc10_ = ObjectEffectInteger()
            _loc10_.deserialize(param1)
            self.effectList.append(_loc10_)
            _loc7_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MountClientData(param1)

    def deserializeAsyncAs_MountClientData(self, param1):
        param1.add_child(self.deserializeByteBoxes)
        param1.add_child(self._idFunc)
        param1.add_child(self._modelFunc)
        self._ancestortree = param1.add_child(self._ancestortreeFunc)
        self._behaviorstree = param1.add_child(self._behaviorstreeFunc)
        param1.add_child(self._nameFunc)
        param1.add_child(self._ownerIdFunc)
        param1.add_child(self._experienceFunc)
        param1.add_child(self._experienceForLevelFunc)
        param1.add_child(self._experienceForNextLevelFunc)
        param1.add_child(self._levelFunc)
        param1.add_child(self._maxPodsFunc)
        param1.add_child(self._staminaFunc)
        param1.add_child(self._staminaMaxFunc)
        param1.add_child(self._maturityFunc)
        param1.add_child(self._maturityForAdultFunc)
        param1.add_child(self._energyFunc)
        param1.add_child(self._energyMaxFunc)
        param1.add_child(self._serenityFunc)
        param1.add_child(self._aggressivityMaxFunc)
        param1.add_child(self._serenityMaxFunc)
        param1.add_child(self._loveFunc)
        param1.add_child(self._loveMaxFunc)
        param1.add_child(self._fecondationTimeFunc)
        param1.add_child(self._boostLimiterFunc)
        param1.add_child(self._boostMaxFunc)
        param1.add_child(self._reproductionCountFunc)
        param1.add_child(self._reproductionCountMaxFunc)
        param1.add_child(self._harnessGIDFunc)
        self._effectListtree = param1.add_child(self._effectListtreeFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.sex = BooleanByteWrapper.get_flag(_loc2_,0)
        self.isRideable = BooleanByteWrapper.get_flag(_loc2_,1)
        self.isWild = BooleanByteWrapper.get_flag(_loc2_,2)
        self.isFecondationReady = BooleanByteWrapper.get_flag(_loc2_,3)
        self.useHarnessColors = BooleanByteWrapper.get_flag(_loc2_,4)

    def _idFunc(self, param1):
        self.id = param1.read_double()
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of MountClientData.id.")

    def _modelFunc(self, param1):
        self.model = param1.read_var_uh_int()
        if self.model < 0:
            raise RuntimeError("Forbidden value (" + str(self.model) + ") on element of MountClientData.model.")

    def _ancestortreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._ancestortree.add_child(self._ancestorFunc)
            _loc3_ += 1

    def _ancestorFunc(self, param1):
        _loc2_ = param1.read_int()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of ancestor.")
        self.ancestor.append(_loc2_)

    def _behaviorstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._behaviorstree.add_child(self._behaviorsFunc)
            _loc3_ += 1

    def _behaviorsFunc(self, param1):
        _loc2_ = param1.read_int()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of behaviors.")
        self.behaviors.append(_loc2_)

    def _nameFunc(self, param1):
        self.name = param1.read_utf()

    def _ownerIdFunc(self, param1):
        self.ownerId = param1.read_int()
        if self.ownerId < 0:
            raise RuntimeError("Forbidden value (" + str(self.ownerId) + ") on element of MountClientData.ownerId.")

    def _experienceFunc(self, param1):
        self.experience = param1.read_var_uh_long()
        if self.experience < 0 or self.experience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element of MountClientData.experience.")

    def _experienceForLevelFunc(self, param1):
        self.experienceForLevel = param1.read_var_uh_long()
        if self.experienceForLevel < 0 or self.experienceForLevel > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceForLevel) + ") on element of MountClientData.experienceForLevel.")

    def _experienceForNextLevelFunc(self, param1):
        self.experienceForNextLevel = param1.read_double()
        if self.experienceForNextLevel < -9007199254740990 or self.experienceForNextLevel > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceForNextLevel) + ") on element of MountClientData.experienceForNextLevel.")

    def _levelFunc(self, param1):
        self.level = param1.read_byte()
        if self.level < 0:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of MountClientData.level.")

    def _maxPodsFunc(self, param1):
        self.maxPods = param1.read_var_uh_int()
        if self.maxPods < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxPods) + ") on element of MountClientData.maxPods.")

    def _staminaFunc(self, param1):
        self.stamina = param1.read_var_uh_int()
        if self.stamina < 0:
            raise RuntimeError("Forbidden value (" + str(self.stamina) + ") on element of MountClientData.stamina.")

    def _staminaMaxFunc(self, param1):
        self.staminaMax = param1.read_var_uh_int()
        if self.staminaMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.staminaMax) + ") on element of MountClientData.staminaMax.")

    def _maturityFunc(self, param1):
        self.maturity = param1.read_var_uh_int()
        if self.maturity < 0:
            raise RuntimeError("Forbidden value (" + str(self.maturity) + ") on element of MountClientData.maturity.")

    def _maturityForAdultFunc(self, param1):
        self.maturityForAdult = param1.read_var_uh_int()
        if self.maturityForAdult < 0:
            raise RuntimeError("Forbidden value (" + str(self.maturityForAdult) + ") on element of MountClientData.maturityForAdult.")

    def _energyFunc(self, param1):
        self.energy = param1.read_var_uh_int()
        if self.energy < 0:
            raise RuntimeError("Forbidden value (" + str(self.energy) + ") on element of MountClientData.energy.")

    def _energyMaxFunc(self, param1):
        self.energyMax = param1.read_var_uh_int()
        if self.energyMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.energyMax) + ") on element of MountClientData.energyMax.")

    def _serenityFunc(self, param1):
        self.serenity = param1.read_int()

    def _aggressivityMaxFunc(self, param1):
        self.aggressivityMax = param1.read_int()

    def _serenityMaxFunc(self, param1):
        self.serenityMax = param1.read_var_uh_int()
        if self.serenityMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.serenityMax) + ") on element of MountClientData.serenityMax.")

    def _loveFunc(self, param1):
        self.love = param1.read_var_uh_int()
        if self.love < 0:
            raise RuntimeError("Forbidden value (" + str(self.love) + ") on element of MountClientData.love.")

    def _loveMaxFunc(self, param1):
        self.loveMax = param1.read_var_uh_int()
        if self.loveMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.loveMax) + ") on element of MountClientData.loveMax.")

    def _fecondationTimeFunc(self, param1):
        self.fecondationTime = param1.read_int()

    def _boostLimiterFunc(self, param1):
        self.boostLimiter = param1.read_int()
        if self.boostLimiter < 0:
            raise RuntimeError("Forbidden value (" + str(self.boostLimiter) + ") on element of MountClientData.boostLimiter.")

    def _boostMaxFunc(self, param1):
        self.boostMax = param1.read_double()
        if self.boostMax < -9007199254740990 or self.boostMax > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.boostMax) + ") on element of MountClientData.boostMax.")

    def _reproductionCountFunc(self, param1):
        self.reproductionCount = param1.read_int()

    def _reproductionCountMaxFunc(self, param1):
        self.reproductionCountMax = param1.read_var_uh_int()
        if self.reproductionCountMax < 0:
            raise RuntimeError("Forbidden value (" + str(self.reproductionCountMax) + ") on element of MountClientData.reproductionCountMax.")

    def _harnessGIDFunc(self, param1):
        self.harnessGID = param1.read_var_uh_short()
        if self.harnessGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.harnessGID) + ") on element of MountClientData.harnessGID.")

    def _effectListtreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._effectListtree.add_child(self._effectListFunc)
            _loc3_ += 1

    def _effectListFunc(self, param1):
        _loc2_ = ObjectEffectInteger()
        _loc2_.deserialize(param1)
        self.effectList.append(_loc2_)


class UpdateMountBoost():
    protocolId = 356

    def __init__(self):
        super().__init__()
        self.type = 0

    def getTypeId(self):
        return 356

    def initUpdateMountBoost(self, param1=0):
        self.type = param1
        return self

    def reset(self):
        self.type = 0

    def serialize(self, param1):
        self.serializeAs_UpdateMountBoost(param1)

    def serializeAs_UpdateMountBoost(self, param1):
        param1.write_byte(self.type)

    def deserialize(self, param1):
        self.deserializeAs_UpdateMountBoost(param1)

    def deserializeAs_UpdateMountBoost(self, param1):
        self._typeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_UpdateMountBoost(param1)

    def deserializeAsyncAs_UpdateMountBoost(self, param1):
        param1.add_child(self._typeFunc)

    def _typeFunc(self, param1):
        self.type = param1.read_byte()
        if self.type < 0:
            raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of UpdateMountBoost.type.")


class MountInformationsForPaddock():
    protocolId = 184

    def __init__(self):
        super().__init__()
        self.modelId = 0
        self.name = ""
        self.ownerName = ""

    def getTypeId(self):
        return 184

    def initMountInformationsForPaddock(self, param1=0, param2="", param3=""):
        self.modelId = param1
        self.name = param2
        self.ownerName = param3
        return self

    def reset(self):
        self.modelId = 0
        self.name = ""
        self.ownerName = ""

    def serialize(self, param1):
        self.serializeAs_MountInformationsForPaddock(param1)

    def serializeAs_MountInformationsForPaddock(self, param1):
        if self.modelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element modelId.")
        param1.write_var_short(self.modelId)
        param1.write_utf(self.name)
        param1.write_utf(self.ownerName)

    def deserialize(self, param1):
        self.deserializeAs_MountInformationsForPaddock(param1)

    def deserializeAs_MountInformationsForPaddock(self, param1):
        self._modelIdFunc(param1)
        self._nameFunc(param1)
        self._ownerNameFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MountInformationsForPaddock(param1)

    def deserializeAsyncAs_MountInformationsForPaddock(self, param1):
        param1.add_child(self._modelIdFunc)
        param1.add_child(self._nameFunc)
        param1.add_child(self._ownerNameFunc)

    def _modelIdFunc(self, param1):
        self.modelId = param1.read_var_uh_short()
        if self.modelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element of MountInformationsForPaddock.modelId.")

    def _nameFunc(self, param1):
        self.name = param1.read_utf()

    def _ownerNameFunc(self, param1):
        self.ownerName = param1.read_utf()


class PaddockBuyableInformations():
    protocolId = 130

    def __init__(self):
        super().__init__()
        self.price = 0
        self.locked = False

    def getTypeId(self):
        return 130

    def initPaddockBuyableInformations(self, param1=0, param2=False):
        self.price = param1
        self.locked = param2
        return self

    def reset(self):
        self.price = 0
        self.locked = False

    def serialize(self, param1):
        self.serializeAs_PaddockBuyableInformations(param1)

    def serializeAs_PaddockBuyableInformations(self, param1):
        if self.price < 0 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element price.")
        param1.write_var_long(self.price)
        param1.write_boolean(self.locked)

    def deserialize(self, param1):
        self.deserializeAs_PaddockBuyableInformations(param1)

    def deserializeAs_PaddockBuyableInformations(self, param1):
        self._priceFunc(param1)
        self._lockedFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PaddockBuyableInformations(param1)

    def deserializeAsyncAs_PaddockBuyableInformations(self, param1):
        param1.add_child(self._priceFunc)
        param1.add_child(self._lockedFunc)

    def _priceFunc(self, param1):
        self.price = param1.read_var_uh_long()
        if self.price < 0 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of PaddockBuyableInformations.price.")

    def _lockedFunc(self, param1):
        self.locked = param1.read_boolean()


class PaddockInformations():
    protocolId = 132

    def __init__(self):
        super().__init__()
        self.maxOutdoorMount = 0
        self.maxItems = 0

    def getTypeId(self):
        return 132

    def initPaddockInformations(self, param1=0, param2=0):
        self.maxOutdoorMount = param1
        self.maxItems = param2
        return self

    def reset(self):
        self.maxOutdoorMount = 0
        self.maxItems = 0

    def serialize(self, param1):
        self.serializeAs_PaddockInformations(param1)

    def serializeAs_PaddockInformations(self, param1):
        if self.maxOutdoorMount < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxOutdoorMount) + ") on element maxOutdoorMount.")
        param1.write_var_short(self.maxOutdoorMount)
        if self.maxItems < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxItems) + ") on element maxItems.")
        param1.write_var_short(self.maxItems)

    def deserialize(self, param1):
        self.deserializeAs_PaddockInformations(param1)

    def deserializeAs_PaddockInformations(self, param1):
        self._maxOutdoorMountFunc(param1)
        self._maxItemsFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PaddockInformations(param1)

    def deserializeAsyncAs_PaddockInformations(self, param1):
        param1.add_child(self._maxOutdoorMountFunc)
        param1.add_child(self._maxItemsFunc)

    def _maxOutdoorMountFunc(self, param1):
        self.maxOutdoorMount = param1.read_var_uh_short()
        if self.maxOutdoorMount < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxOutdoorMount) + ") on element of PaddockInformations.maxOutdoorMount.")

    def _maxItemsFunc(self, param1):
        self.maxItems = param1.read_var_uh_short()
        if self.maxItems < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxItems) + ") on element of PaddockInformations.maxItems.")


class PaddockInformationsForSell():
    protocolId = 222

    def __init__(self):
        super().__init__()
        self.guildOwner = ""
        self.worldX = 0
        self.worldY = 0
        self.subAreaId = 0
        self.nbMount = 0
        self.nbObject = 0
        self.price = 0

    def getTypeId(self):
        return 222

    def initPaddockInformationsForSell(self, param1="", param2=0, param3=0, param4=0, param5=0, param6=0, param7=0):
        self.guildOwner = param1
        self.worldX = param2
        self.worldY = param3
        self.subAreaId = param4
        self.nbMount = param5
        self.nbObject = param6
        self.price = param7
        return self

    def reset(self):
        self.guildOwner = ""
        self.worldX = 0
        self.worldY = 0
        self.subAreaId = 0
        self.nbMount = 0
        self.nbObject = 0
        self.price = 0

    def serialize(self, param1):
        self.serializeAs_PaddockInformationsForSell(param1)

    def serializeAs_PaddockInformationsForSell(self, param1):
        param1.write_utf(self.guildOwner)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        param1.write_byte(self.nbMount)
        param1.write_byte(self.nbObject)
        if self.price < 0 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element price.")
        param1.write_var_long(self.price)

    def deserialize(self, param1):
        self.deserializeAs_PaddockInformationsForSell(param1)

    def deserializeAs_PaddockInformationsForSell(self, param1):
        self._guildOwnerFunc(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._subAreaIdFunc(param1)
        self._nbMountFunc(param1)
        self._nbObjectFunc(param1)
        self._priceFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PaddockInformationsForSell(param1)

    def deserializeAsyncAs_PaddockInformationsForSell(self, param1):
        param1.add_child(self._guildOwnerFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._subAreaIdFunc)
        param1.add_child(self._nbMountFunc)
        param1.add_child(self._nbObjectFunc)
        param1.add_child(self._priceFunc)

    def _guildOwnerFunc(self, param1):
        self.guildOwner = param1.read_utf()

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PaddockInformationsForSell.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PaddockInformationsForSell.worldY.")

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PaddockInformationsForSell.subAreaId.")

    def _nbMountFunc(self, param1):
        self.nbMount = param1.read_byte()

    def _nbObjectFunc(self, param1):
        self.nbObject = param1.read_byte()

    def _priceFunc(self, param1):
        self.price = param1.read_var_uh_long()
        if self.price < 0 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of PaddockInformationsForSell.price.")


class PrismFightersInformation():
    protocolId = 443

    def __init__(self):
        super().__init__()
        self.subAreaId = 0
        self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo()
        self.allyCharactersInformations = []
        self.enemyCharactersInformations = []
        self._waitingForHelpInfotree = FuncTree()
        self._allyCharactersInformationstree = FuncTree()
        self._enemyCharactersInformationstree = FuncTree()

    def getTypeId(self):
        return 443

    def initPrismFightersInformation(self, param1=0, param2=None, param3=[], param4=[]):
        self.subAreaId = param1
        self.waitingForHelpInfo = param2
        self.allyCharactersInformations = param3
        self.enemyCharactersInformations = param4
        return self

    def reset(self):
        self.subAreaId = 0
        self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo()
        self.enemyCharactersInformations = []

    def serialize(self, param1):
        self.serializeAs_PrismFightersInformation(param1)

    def serializeAs_PrismFightersInformation(self, param1):
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        self.waitingForHelpInfo.serializeAs_ProtectedEntityWaitingForHelpInfo(param1)
        param1.write_short(len(self.allyCharactersInformations))
        _loc2_ = 0
        while _loc2_ < len(self.allyCharactersInformations):
            param1.write_short(as_parent(self.allyCharactersInformations[_loc2_], CharacterMinimalPlusLookInformations).getTypeId())
            as_parent(self.allyCharactersInformations[_loc2_], CharacterMinimalPlusLookInformations).serialize(param1)
            _loc2_ += 1
        param1.write_short(len(self.enemyCharactersInformations))
        _loc3_ = 0
        while _loc3_ < len(self.enemyCharactersInformations):
            param1.write_short(as_parent(self.enemyCharactersInformations[_loc3_], CharacterMinimalPlusLookInformations).getTypeId())
            as_parent(self.enemyCharactersInformations[_loc3_], CharacterMinimalPlusLookInformations).serialize(param1)
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_PrismFightersInformation(param1)

    def deserializeAs_PrismFightersInformation(self, param1):
        _loc6_ = 0
        _loc7_ = None
        _loc8_ = 0
        _loc9_ = None
        self._subAreaIdFunc(param1)
        self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo()
        self.waitingForHelpInfo.deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_unsigned_short()
            _loc7_ = ProtocolTypeManager.get_instance(CharacterMinimalPlusLookInformations,_loc6_)
            _loc7_.deserialize(param1)
            self.allyCharactersInformations.append(_loc7_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc8_ = param1.read_unsigned_short()
            _loc9_ = ProtocolTypeManager.get_instance(CharacterMinimalPlusLookInformations,_loc8_)
            _loc9_.deserialize(param1)
            self.enemyCharactersInformations.append(_loc9_)
            _loc5_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PrismFightersInformation(param1)

    def deserializeAsyncAs_PrismFightersInformation(self, param1):
        param1.add_child(self._subAreaIdFunc)
        self._waitingForHelpInfotree = param1.add_child(self._waitingForHelpInfotreeFunc)
        self._allyCharactersInformationstree = param1.add_child(self._allyCharactersInformationstreeFunc)
        self._enemyCharactersInformationstree = param1.add_child(self._enemyCharactersInformationstreeFunc)

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PrismFightersInformation.subAreaId.")

    def _waitingForHelpInfotreeFunc(self, param1):
        self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo()
        self.waitingForHelpInfo.deserializeAsync(self._waitingForHelpInfotree)

    def _allyCharactersInformationstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._allyCharactersInformationstree.add_child(self._allyCharactersInformationsFunc)
            _loc3_ += 1

    def _allyCharactersInformationsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(CharacterMinimalPlusLookInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.allyCharactersInformations.append(_loc3_)

    def _enemyCharactersInformationstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._enemyCharactersInformationstree.add_child(self._enemyCharactersInformationsFunc)
            _loc3_ += 1

    def _enemyCharactersInformationsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(CharacterMinimalPlusLookInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.enemyCharactersInformations.append(_loc3_)


class PrismInformation():
    protocolId = 428

    def __init__(self):
        super().__init__()
        self.typeId = 0
        self.state = 1
        self.nextVulnerabilityDate = 0
        self.placementDate = 0
        self.rewardTokenCount = 0

    def getTypeId(self):
        return 428

    def initPrismInformation(self, param1=0, param2=1, param3=0, param4=0, param5=0):
        self.typeId = param1
        self.state = param2
        self.nextVulnerabilityDate = param3
        self.placementDate = param4
        self.rewardTokenCount = param5
        return self

    def reset(self):
        self.typeId = 0
        self.state = 1
        self.nextVulnerabilityDate = 0
        self.placementDate = 0
        self.rewardTokenCount = 0

    def serialize(self, param1):
        self.serializeAs_PrismInformation(param1)

    def serializeAs_PrismInformation(self, param1):
        if self.typeId < 0:
            raise RuntimeError("Forbidden value (" + str(self.typeId) + ") on element typeId.")
        param1.write_byte(self.typeId)
        param1.write_byte(self.state)
        if self.nextVulnerabilityDate < 0:
            raise RuntimeError("Forbidden value (" + str(self.nextVulnerabilityDate) + ") on element nextVulnerabilityDate.")
        param1.write_int(self.nextVulnerabilityDate)
        if self.placementDate < 0:
            raise RuntimeError("Forbidden value (" + str(self.placementDate) + ") on element placementDate.")
        param1.write_int(self.placementDate)
        if self.rewardTokenCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.rewardTokenCount) + ") on element rewardTokenCount.")
        param1.write_var_int(self.rewardTokenCount)

    def deserialize(self, param1):
        self.deserializeAs_PrismInformation(param1)

    def deserializeAs_PrismInformation(self, param1):
        self._typeIdFunc(param1)
        self._stateFunc(param1)
        self._nextVulnerabilityDateFunc(param1)
        self._placementDateFunc(param1)
        self._rewardTokenCountFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PrismInformation(param1)

    def deserializeAsyncAs_PrismInformation(self, param1):
        param1.add_child(self._typeIdFunc)
        param1.add_child(self._stateFunc)
        param1.add_child(self._nextVulnerabilityDateFunc)
        param1.add_child(self._placementDateFunc)
        param1.add_child(self._rewardTokenCountFunc)

    def _typeIdFunc(self, param1):
        self.typeId = param1.read_byte()
        if self.typeId < 0:
            raise RuntimeError("Forbidden value (" + str(self.typeId) + ") on element of PrismInformation.typeId.")

    def _stateFunc(self, param1):
        self.state = param1.read_byte()
        if self.state < 0:
            raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of PrismInformation.state.")

    def _nextVulnerabilityDateFunc(self, param1):
        self.nextVulnerabilityDate = param1.read_int()
        if self.nextVulnerabilityDate < 0:
            raise RuntimeError("Forbidden value (" + str(self.nextVulnerabilityDate) + ") on element of PrismInformation.nextVulnerabilityDate.")

    def _placementDateFunc(self, param1):
        self.placementDate = param1.read_int()
        if self.placementDate < 0:
            raise RuntimeError("Forbidden value (" + str(self.placementDate) + ") on element of PrismInformation.placementDate.")

    def _rewardTokenCountFunc(self, param1):
        self.rewardTokenCount = param1.read_var_uh_int()
        if self.rewardTokenCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.rewardTokenCount) + ") on element of PrismInformation.rewardTokenCount.")


class PrismSubareaEmptyInfo():
    protocolId = 438

    def __init__(self):
        super().__init__()
        self.subAreaId = 0
        self.allianceId = 0

    def getTypeId(self):
        return 438

    def initPrismSubareaEmptyInfo(self, param1=0, param2=0):
        self.subAreaId = param1
        self.allianceId = param2
        return self

    def reset(self):
        self.subAreaId = 0
        self.allianceId = 0

    def serialize(self, param1):
        self.serializeAs_PrismSubareaEmptyInfo(param1)

    def serializeAs_PrismSubareaEmptyInfo(self, param1):
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element allianceId.")
        param1.write_var_int(self.allianceId)

    def deserialize(self, param1):
        self.deserializeAs_PrismSubareaEmptyInfo(param1)

    def deserializeAs_PrismSubareaEmptyInfo(self, param1):
        self._subAreaIdFunc(param1)
        self._allianceIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PrismSubareaEmptyInfo(param1)

    def deserializeAsyncAs_PrismSubareaEmptyInfo(self, param1):
        param1.add_child(self._subAreaIdFunc)
        param1.add_child(self._allianceIdFunc)

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PrismSubareaEmptyInfo.subAreaId.")

    def _allianceIdFunc(self, param1):
        self.allianceId = param1.read_var_uh_int()
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element of PrismSubareaEmptyInfo.allianceId.")


class Shortcut():
    protocolId = 369

    def __init__(self):
        super().__init__()
        self.slot = 0

    def getTypeId(self):
        return 369

    def initShortcut(self, param1=0):
        self.slot = param1
        return self

    def reset(self):
        self.slot = 0

    def serialize(self, param1):
        self.serializeAs_Shortcut(param1)

    def serializeAs_Shortcut(self, param1):
        if self.slot < 0 or self.slot > 99:
            raise RuntimeError("Forbidden value (" + str(self.slot) + ") on element slot.")
        param1.write_byte(self.slot)

    def deserialize(self, param1):
        self.deserializeAs_Shortcut(param1)

    def deserializeAs_Shortcut(self, param1):
        self._slotFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_Shortcut(param1)

    def deserializeAsyncAs_Shortcut(self, param1):
        param1.add_child(self._slotFunc)

    def _slotFunc(self, param1):
        self.slot = param1.read_byte()
        if self.slot < 0 or self.slot > 99:
            raise RuntimeError("Forbidden value (" + str(self.slot) + ") on element of Shortcut.slot.")


class AbstractSocialGroupInfos():
    protocolId = 416

    def getTypeId(self):
        return 416

    def initAbstractSocialGroupInfos(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_AbstractSocialGroupInfos(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_AbstractSocialGroupInfos(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_AbstractSocialGroupInfos(self, param1):
        pass


class AllianceVersatileInformations():
    protocolId = 432

    def __init__(self):
        super().__init__()
        self.allianceId = 0
        self.nbGuilds = 0
        self.nbMembers = 0
        self.nbSubarea = 0

    def getTypeId(self):
        return 432

    def initAllianceVersatileInformations(self, param1=0, param2=0, param3=0, param4=0):
        self.allianceId = param1
        self.nbGuilds = param2
        self.nbMembers = param3
        self.nbSubarea = param4
        return self

    def reset(self):
        self.allianceId = 0
        self.nbGuilds = 0
        self.nbMembers = 0
        self.nbSubarea = 0

    def serialize(self, param1):
        self.serializeAs_AllianceVersatileInformations(param1)

    def serializeAs_AllianceVersatileInformations(self, param1):
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element allianceId.")
        param1.write_var_int(self.allianceId)
        if self.nbGuilds < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbGuilds) + ") on element nbGuilds.")
        param1.write_var_short(self.nbGuilds)
        if self.nbMembers < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element nbMembers.")
        param1.write_var_short(self.nbMembers)
        if self.nbSubarea < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbSubarea) + ") on element nbSubarea.")
        param1.write_var_short(self.nbSubarea)

    def deserialize(self, param1):
        self.deserializeAs_AllianceVersatileInformations(param1)

    def deserializeAs_AllianceVersatileInformations(self, param1):
        self._allianceIdFunc(param1)
        self._nbGuildsFunc(param1)
        self._nbMembersFunc(param1)
        self._nbSubareaFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AllianceVersatileInformations(param1)

    def deserializeAsyncAs_AllianceVersatileInformations(self, param1):
        param1.add_child(self._allianceIdFunc)
        param1.add_child(self._nbGuildsFunc)
        param1.add_child(self._nbMembersFunc)
        param1.add_child(self._nbSubareaFunc)

    def _allianceIdFunc(self, param1):
        self.allianceId = param1.read_var_uh_int()
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element of AllianceVersatileInformations.allianceId.")

    def _nbGuildsFunc(self, param1):
        self.nbGuilds = param1.read_var_uh_short()
        if self.nbGuilds < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbGuilds) + ") on element of AllianceVersatileInformations.nbGuilds.")

    def _nbMembersFunc(self, param1):
        self.nbMembers = param1.read_var_uh_short()
        if self.nbMembers < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element of AllianceVersatileInformations.nbMembers.")

    def _nbSubareaFunc(self, param1):
        self.nbSubarea = param1.read_var_uh_short()
        if self.nbSubarea < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbSubarea) + ") on element of AllianceVersatileInformations.nbSubarea.")


class GuildVersatileInformations():
    protocolId = 435

    def __init__(self):
        super().__init__()
        self.guildId = 0
        self.leaderId = 0
        self.guildLevel = 0
        self.nbMembers = 0

    def getTypeId(self):
        return 435

    def initGuildVersatileInformations(self, param1=0, param2=0, param3=0, param4=0):
        self.guildId = param1
        self.leaderId = param2
        self.guildLevel = param3
        self.nbMembers = param4
        return self

    def reset(self):
        self.guildId = 0
        self.leaderId = 0
        self.guildLevel = 0
        self.nbMembers = 0

    def serialize(self, param1):
        self.serializeAs_GuildVersatileInformations(param1)

    def serializeAs_GuildVersatileInformations(self, param1):
        if self.guildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element guildId.")
        param1.write_var_int(self.guildId)
        if self.leaderId < 0 or self.leaderId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.leaderId) + ") on element leaderId.")
        param1.write_var_long(self.leaderId)
        if self.guildLevel < 1 or self.guildLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.guildLevel) + ") on element guildLevel.")
        param1.write_byte(self.guildLevel)
        if self.nbMembers < 1 or self.nbMembers > 240:
            raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element nbMembers.")
        param1.write_byte(self.nbMembers)

    def deserialize(self, param1):
        self.deserializeAs_GuildVersatileInformations(param1)

    def deserializeAs_GuildVersatileInformations(self, param1):
        self._guildIdFunc(param1)
        self._leaderIdFunc(param1)
        self._guildLevelFunc(param1)
        self._nbMembersFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GuildVersatileInformations(param1)

    def deserializeAsyncAs_GuildVersatileInformations(self, param1):
        param1.add_child(self._guildIdFunc)
        param1.add_child(self._leaderIdFunc)
        param1.add_child(self._guildLevelFunc)
        param1.add_child(self._nbMembersFunc)

    def _guildIdFunc(self, param1):
        self.guildId = param1.read_var_uh_int()
        if self.guildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of GuildVersatileInformations.guildId.")

    def _leaderIdFunc(self, param1):
        self.leaderId = param1.read_var_uh_long()
        if self.leaderId < 0 or self.leaderId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.leaderId) + ") on element of GuildVersatileInformations.leaderId.")

    def _guildLevelFunc(self, param1):
        self.guildLevel = param1.read_unsigned_byte()
        if self.guildLevel < 1 or self.guildLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.guildLevel) + ") on element of GuildVersatileInformations.guildLevel.")

    def _nbMembersFunc(self, param1):
        self.nbMembers = param1.read_unsigned_byte()
        if self.nbMembers < 1 or self.nbMembers > 240:
            raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element of GuildVersatileInformations.nbMembers.")


class StartupActionAddObject():
    protocolId = 52

    def __init__(self):
        super().__init__()
        self.uid = 0
        self.title = ""
        self.text = ""
        self.descUrl = ""
        self.pictureUrl = ""
        self.items = []
        self._itemstree = FuncTree()

    def getTypeId(self):
        return 52

    def initStartupActionAddObject(self, param1=0, param2="", param3="", param4="", param5="", param6=[]):
        self.uid = param1
        self.title = param2
        self.text = param3
        self.descUrl = param4
        self.pictureUrl = param5
        self.items = param6
        return self

    def reset(self):
        self.uid = 0
        self.title = ""
        self.text = ""
        self.descUrl = ""
        self.pictureUrl = ""
        self.items = []

    def serialize(self, param1):
        self.serializeAs_StartupActionAddObject(param1)

    def serializeAs_StartupActionAddObject(self, param1):
        if self.uid < 0:
            raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element uid.")
        param1.write_int(self.uid)
        param1.write_utf(self.title)
        param1.write_utf(self.text)
        param1.write_utf(self.descUrl)
        param1.write_utf(self.pictureUrl)
        param1.write_short(len(self.items))
        _loc2_ = 0
        while _loc2_ < len(self.items):
            as_parent(self.items[_loc2_], ObjectItemInformationWithQuantity).serializeAs_ObjectItemInformationWithQuantity(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_StartupActionAddObject(param1)

    def deserializeAs_StartupActionAddObject(self, param1):
        _loc4_ = None
        self._uidFunc(param1)
        self._titleFunc(param1)
        self._textFunc(param1)
        self._descUrlFunc(param1)
        self._pictureUrlFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = ObjectItemInformationWithQuantity()
            _loc4_.deserialize(param1)
            self.items.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_StartupActionAddObject(param1)

    def deserializeAsyncAs_StartupActionAddObject(self, param1):
        param1.add_child(self._uidFunc)
        param1.add_child(self._titleFunc)
        param1.add_child(self._textFunc)
        param1.add_child(self._descUrlFunc)
        param1.add_child(self._pictureUrlFunc)
        self._itemstree = param1.add_child(self._itemstreeFunc)

    def _uidFunc(self, param1):
        self.uid = param1.read_int()
        if self.uid < 0:
            raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element of StartupActionAddObject.uid.")

    def _titleFunc(self, param1):
        self.title = param1.read_utf()

    def _textFunc(self, param1):
        self.text = param1.read_utf()

    def _descUrlFunc(self, param1):
        self.descUrl = param1.read_utf()

    def _pictureUrlFunc(self, param1):
        self.pictureUrl = param1.read_utf()

    def _itemstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._itemstree.add_child(self._itemsFunc)
            _loc3_ += 1

    def _itemsFunc(self, param1):
        _loc2_ = ObjectItemInformationWithQuantity()
        _loc2_.deserialize(param1)
        self.items.append(_loc2_)


class TrustCertificate():
    protocolId = 377

    def __init__(self):
        super().__init__()
        self.id = 0
        self.hash = ""

    def getTypeId(self):
        return 377

    def initTrustCertificate(self, param1=0, param2=""):
        self.id = param1
        self.hash = param2
        return self

    def reset(self):
        self.id = 0
        self.hash = ""

    def serialize(self, param1):
        self.serializeAs_TrustCertificate(param1)

    def serializeAs_TrustCertificate(self, param1):
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_int(self.id)
        param1.write_utf(self.hash)

    def deserialize(self, param1):
        self.deserializeAs_TrustCertificate(param1)

    def deserializeAs_TrustCertificate(self, param1):
        self._idFunc(param1)
        self._hashFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TrustCertificate(param1)

    def deserializeAsyncAs_TrustCertificate(self, param1):
        param1.add_child(self._idFunc)
        param1.add_child(self._hashFunc)

    def _idFunc(self, param1):
        self.id = param1.read_int()
        if self.id < 0:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of TrustCertificate.id.")

    def _hashFunc(self, param1):
        self.hash = param1.read_utf()


class ContentPart():
    protocolId = 350

    def __init__(self):
        super().__init__()
        self.id = ""
        self.state = 0

    def getTypeId(self):
        return 350

    def initContentPart(self, param1="", param2=0):
        self.id = param1
        self.state = param2
        return self

    def reset(self):
        self.id = ""
        self.state = 0

    def serialize(self, param1):
        self.serializeAs_ContentPart(param1)

    def serializeAs_ContentPart(self, param1):
        param1.write_utf(self.id)
        param1.write_byte(self.state)

    def deserialize(self, param1):
        self.deserializeAs_ContentPart(param1)

    def deserializeAs_ContentPart(self, param1):
        self._idFunc(param1)
        self._stateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ContentPart(param1)

    def deserializeAsyncAs_ContentPart(self, param1):
        param1.add_child(self._idFunc)
        param1.add_child(self._stateFunc)

    def _idFunc(self, param1):
        self.id = param1.read_utf()

    def _stateFunc(self, param1):
        self.state = param1.read_byte()
        if self.state < 0:
            raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of ContentPart.state.")


class Version():
    protocolId = 11

    def __init__(self):
        super().__init__()
        self.major = 0
        self.minor = 0
        self.release = 0
        self.revision = 0
        self.patch = 0
        self.buildType = 0

    def getTypeId(self):
        return 11

    def initVersion(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0):
        self.major = param1
        self.minor = param2
        self.release = param3
        self.revision = param4
        self.patch = param5
        self.buildType = param6
        return self

    def reset(self):
        self.major = 0
        self.minor = 0
        self.release = 0
        self.revision = 0
        self.patch = 0
        self.buildType = 0

    def serialize(self, param1):
        self.serializeAs_Version(param1)

    def serializeAs_Version(self, param1):
        if self.major < 0:
            raise RuntimeError("Forbidden value (" + str(self.major) + ") on element major.")
        param1.write_byte(self.major)
        if self.minor < 0:
            raise RuntimeError("Forbidden value (" + str(self.minor) + ") on element minor.")
        param1.write_byte(self.minor)
        if self.release < 0:
            raise RuntimeError("Forbidden value (" + str(self.release) + ") on element release.")
        param1.write_byte(self.release)
        if self.revision < 0:
            raise RuntimeError("Forbidden value (" + str(self.revision) + ") on element revision.")
        param1.write_int(self.revision)
        if self.patch < 0:
            raise RuntimeError("Forbidden value (" + str(self.patch) + ") on element patch.")
        param1.write_byte(self.patch)
        param1.write_byte(self.buildType)

    def deserialize(self, param1):
        self.deserializeAs_Version(param1)

    def deserializeAs_Version(self, param1):
        self._majorFunc(param1)
        self._minorFunc(param1)
        self._releaseFunc(param1)
        self._revisionFunc(param1)
        self._patchFunc(param1)
        self._buildTypeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_Version(param1)

    def deserializeAsyncAs_Version(self, param1):
        param1.add_child(self._majorFunc)
        param1.add_child(self._minorFunc)
        param1.add_child(self._releaseFunc)
        param1.add_child(self._revisionFunc)
        param1.add_child(self._patchFunc)
        param1.add_child(self._buildTypeFunc)

    def _majorFunc(self, param1):
        self.major = param1.read_byte()
        if self.major < 0:
            raise RuntimeError("Forbidden value (" + str(self.major) + ") on element of Version.major.")

    def _minorFunc(self, param1):
        self.minor = param1.read_byte()
        if self.minor < 0:
            raise RuntimeError("Forbidden value (" + str(self.minor) + ") on element of Version.minor.")

    def _releaseFunc(self, param1):
        self.release = param1.read_byte()
        if self.release < 0:
            raise RuntimeError("Forbidden value (" + str(self.release) + ") on element of Version.release.")

    def _revisionFunc(self, param1):
        self.revision = param1.read_int()
        if self.revision < 0:
            raise RuntimeError("Forbidden value (" + str(self.revision) + ") on element of Version.revision.")

    def _patchFunc(self, param1):
        self.patch = param1.read_byte()
        if self.patch < 0:
            raise RuntimeError("Forbidden value (" + str(self.patch) + ") on element of Version.patch.")

    def _buildTypeFunc(self, param1):
        self.buildType = param1.read_byte()
        if self.buildType < 0:
            raise RuntimeError("Forbidden value (" + str(self.buildType) + ") on element of Version.buildType.")


class KrosmasterFigure():
    protocolId = 397

    def __init__(self):
        super().__init__()
        self.uid = ""
        self.figure = 0
        self.pedestal = 0
        self.bound = False

    def getTypeId(self):
        return 397

    def initKrosmasterFigure(self, param1="", param2=0, param3=0, param4=False):
        self.uid = param1
        self.figure = param2
        self.pedestal = param3
        self.bound = param4
        return self

    def reset(self):
        self.uid = ""
        self.figure = 0
        self.pedestal = 0
        self.bound = False

    def serialize(self, param1):
        self.serializeAs_KrosmasterFigure(param1)

    def serializeAs_KrosmasterFigure(self, param1):
        param1.write_utf(self.uid)
        if self.figure < 0:
            raise RuntimeError("Forbidden value (" + str(self.figure) + ") on element figure.")
        param1.write_var_short(self.figure)
        if self.pedestal < 0:
            raise RuntimeError("Forbidden value (" + str(self.pedestal) + ") on element pedestal.")
        param1.write_var_short(self.pedestal)
        param1.write_boolean(self.bound)

    def deserialize(self, param1):
        self.deserializeAs_KrosmasterFigure(param1)

    def deserializeAs_KrosmasterFigure(self, param1):
        self._uidFunc(param1)
        self._figureFunc(param1)
        self._pedestalFunc(param1)
        self._boundFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_KrosmasterFigure(param1)

    def deserializeAsyncAs_KrosmasterFigure(self, param1):
        param1.add_child(self._uidFunc)
        param1.add_child(self._figureFunc)
        param1.add_child(self._pedestalFunc)
        param1.add_child(self._boundFunc)

    def _uidFunc(self, param1):
        self.uid = param1.read_utf()

    def _figureFunc(self, param1):
        self.figure = param1.read_var_uh_short()
        if self.figure < 0:
            raise RuntimeError("Forbidden value (" + str(self.figure) + ") on element of KrosmasterFigure.figure.")

    def _pedestalFunc(self, param1):
        self.pedestal = param1.read_var_uh_short()
        if self.pedestal < 0:
            raise RuntimeError("Forbidden value (" + str(self.pedestal) + ") on element of KrosmasterFigure.pedestal.")

    def _boundFunc(self, param1):
        self.bound = param1.read_boolean()


class StatisticDataBoolean(StatisticData):
    protocolId = 482

    def __init__(self):
        super().__init__()
        self.value = False

    def getTypeId(self):
        return 482

    def initStatisticDataBoolean(self, param1=False):
        self.value = param1
        return self

    def reset(self):
        self.value = False

    def serialize(self, param1):
        self.serializeAs_StatisticDataBoolean(param1)

    def serializeAs_StatisticDataBoolean(self, param1):
        super().serializeAs_StatisticData(param1)
        param1.write_boolean(self.value)

    def deserialize(self, param1):
        self.deserializeAs_StatisticDataBoolean(param1)

    def deserializeAs_StatisticDataBoolean(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_StatisticDataBoolean(param1)

    def deserializeAsyncAs_StatisticDataBoolean(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_boolean()


class StatisticDataByte(StatisticData):
    protocolId = 486

    def __init__(self):
        super().__init__()
        self.value = 0

    def getTypeId(self):
        return 486

    def initStatisticDataByte(self, param1=0):
        self.value = param1
        return self

    def reset(self):
        self.value = 0

    def serialize(self, param1):
        self.serializeAs_StatisticDataByte(param1)

    def serializeAs_StatisticDataByte(self, param1):
        super().serializeAs_StatisticData(param1)
        param1.write_byte(self.value)

    def deserialize(self, param1):
        self.deserializeAs_StatisticDataByte(param1)

    def deserializeAs_StatisticDataByte(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_StatisticDataByte(param1)

    def deserializeAsyncAs_StatisticDataByte(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_byte()


class StatisticDataInt(StatisticData):
    protocolId = 485

    def __init__(self):
        super().__init__()
        self.value = 0

    def getTypeId(self):
        return 485

    def initStatisticDataInt(self, param1=0):
        self.value = param1
        return self

    def reset(self):
        self.value = 0

    def serialize(self, param1):
        self.serializeAs_StatisticDataInt(param1)

    def serializeAs_StatisticDataInt(self, param1):
        super().serializeAs_StatisticData(param1)
        param1.write_int(self.value)

    def deserialize(self, param1):
        self.deserializeAs_StatisticDataInt(param1)

    def deserializeAs_StatisticDataInt(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_StatisticDataInt(param1)

    def deserializeAsyncAs_StatisticDataInt(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_int()


class StatisticDataShort(StatisticData):
    protocolId = 488

    def __init__(self):
        super().__init__()
        self.value = 0

    def getTypeId(self):
        return 488

    def initStatisticDataShort(self, param1=0):
        self.value = param1
        return self

    def reset(self):
        self.value = 0

    def serialize(self, param1):
        self.serializeAs_StatisticDataShort(param1)

    def serializeAs_StatisticDataShort(self, param1):
        super().serializeAs_StatisticData(param1)
        param1.write_short(self.value)

    def deserialize(self, param1):
        self.deserializeAs_StatisticDataShort(param1)

    def deserializeAs_StatisticDataShort(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_StatisticDataShort(param1)

    def deserializeAsyncAs_StatisticDataShort(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_short()


class StatisticDataString(StatisticData):
    protocolId = 487

    def __init__(self):
        super().__init__()
        self.value = ""

    def getTypeId(self):
        return 487

    def initStatisticDataString(self, param1=""):
        self.value = param1
        return self

    def reset(self):
        self.value = ""

    def serialize(self, param1):
        self.serializeAs_StatisticDataString(param1)

    def serializeAs_StatisticDataString(self, param1):
        super().serializeAs_StatisticData(param1)
        param1.write_utf(self.value)

    def deserialize(self, param1):
        self.deserializeAs_StatisticDataString(param1)

    def deserializeAs_StatisticDataString(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_StatisticDataString(param1)

    def deserializeAsyncAs_StatisticDataString(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_utf()


class AchievementStartedObjective(AchievementObjective):
    protocolId = 402

    def __init__(self):
        super().__init__()
        self.value = 0

    def getTypeId(self):
        return 402

    def initAchievementStartedObjective(self, param1=0, param2=0, param3=0):
        super().initAchievementObjective(param1,param2)
        self.value = param3
        return self

    def reset(self):
        super().reset()
        self.value = 0

    def serialize(self, param1):
        self.serializeAs_AchievementStartedObjective(param1)

    def serializeAs_AchievementStartedObjective(self, param1):
        super().serializeAs_AchievementObjective(param1)
        if self.value < 0:
            raise RuntimeError("Forbidden value (" + str(self.value) + ") on element value.")
        param1.write_var_short(self.value)

    def deserialize(self, param1):
        self.deserializeAs_AchievementStartedObjective(param1)

    def deserializeAs_AchievementStartedObjective(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AchievementStartedObjective(param1)

    def deserializeAsyncAs_AchievementStartedObjective(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_var_uh_short()
        if self.value < 0:
            raise RuntimeError("Forbidden value (" + str(self.value) + ") on element of AchievementStartedObjective.value.")


class FightTemporaryBoostEffect(AbstractFightDispellableEffect):
    protocolId = 209

    def __init__(self):
        super().__init__()
        self.delta = 0

    def getTypeId(self):
        return 209

    def initFightTemporaryBoostEffect(self, param1=0, param2=0, param3=0, param4=1, param5=0, param6=0, param7=0, param8=0):
        super().initAbstractFightDispellableEffect(param1,param2,param3,param4,param5,param6,param7)
        self.delta = param8
        return self

    def reset(self):
        super().reset()
        self.delta = 0

    def serialize(self, param1):
        self.serializeAs_FightTemporaryBoostEffect(param1)

    def serializeAs_FightTemporaryBoostEffect(self, param1):
        super().serializeAs_AbstractFightDispellableEffect(param1)
        param1.write_short(self.delta)

    def deserialize(self, param1):
        self.deserializeAs_FightTemporaryBoostEffect(param1)

    def deserializeAs_FightTemporaryBoostEffect(self, param1):
        super().deserialize(param1)
        self._deltaFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTemporaryBoostEffect(param1)

    def deserializeAsyncAs_FightTemporaryBoostEffect(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._deltaFunc)

    def _deltaFunc(self, param1):
        self.delta = param1.read_short()


class FightTemporarySpellImmunityEffect(AbstractFightDispellableEffect):
    protocolId = 366

    def __init__(self):
        super().__init__()
        self.immuneSpellId = 0

    def getTypeId(self):
        return 366

    def initFightTemporarySpellImmunityEffect(self, param1=0, param2=0, param3=0, param4=1, param5=0, param6=0, param7=0, param8=0):
        super().initAbstractFightDispellableEffect(param1,param2,param3,param4,param5,param6,param7)
        self.immuneSpellId = param8
        return self

    def reset(self):
        super().reset()
        self.immuneSpellId = 0

    def serialize(self, param1):
        self.serializeAs_FightTemporarySpellImmunityEffect(param1)

    def serializeAs_FightTemporarySpellImmunityEffect(self, param1):
        super().serializeAs_AbstractFightDispellableEffect(param1)
        param1.write_int(self.immuneSpellId)

    def deserialize(self, param1):
        self.deserializeAs_FightTemporarySpellImmunityEffect(param1)

    def deserializeAs_FightTemporarySpellImmunityEffect(self, param1):
        super().deserialize(param1)
        self._immuneSpellIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTemporarySpellImmunityEffect(param1)

    def deserializeAsyncAs_FightTemporarySpellImmunityEffect(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._immuneSpellIdFunc)

    def _immuneSpellIdFunc(self, param1):
        self.immuneSpellId = param1.read_int()


class FightTriggeredEffect(AbstractFightDispellableEffect):
    protocolId = 210

    def __init__(self):
        super().__init__()
        self.param1 = 0
        self.param2 = 0
        self.param3 = 0
        self.delay = 0

    def getTypeId(self):
        return 210

    def initFightTriggeredEffect(self, param1=0, param2=0, param3=0, param4=1, param5=0, param6=0, param7=0, param8=0, param9=0, param10=0, param11=0):
        super().initAbstractFightDispellableEffect(param1,param2,param3,param4,param5,param6,param7)
        self.param1 = param8
        self.param2 = param9
        self.param3 = param10
        self.delay = param11
        return self

    def reset(self):
        super().reset()
        self.param1 = 0
        self.param2 = 0
        self.param3 = 0
        self.delay = 0

    def serialize(self, param1):
        self.serializeAs_FightTriggeredEffect(param1)

    def serializeAs_FightTriggeredEffect(self, param1):
        super().serializeAs_AbstractFightDispellableEffect(param1)
        param1.write_int(self.param1)
        param1.write_int(self.param2)
        param1.write_int(self.param3)
        param1.write_short(self.delay)

    def deserialize(self, param1):
        self.deserializeAs_FightTriggeredEffect(param1)

    def deserializeAs_FightTriggeredEffect(self, param1):
        super().deserialize(param1)
        self._param1Func(param1)
        self._param2Func(param1)
        self._param3Func(param1)
        self._delayFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTriggeredEffect(param1)

    def deserializeAsyncAs_FightTriggeredEffect(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._param1Func)
        param1.add_child(self._param2Func)
        param1.add_child(self._param3Func)
        param1.add_child(self._delayFunc)

    def _param1Func(self, param1):
        self.param1 = param1.read_int()

    def _param2Func(self, param1):
        self.param2 = param1.read_int()

    def _param3Func(self, param1):
        self.param3 = param1.read_int()

    def _delayFunc(self, param1):
        self.delay = param1.read_short()


class ServerSessionConstantInteger(ServerSessionConstant):
    protocolId = 433

    def __init__(self):
        super().__init__()
        self.value = 0

    def getTypeId(self):
        return 433

    def initServerSessionConstantInteger(self, param1=0, param2=0):
        super().initServerSessionConstant(param1)
        self.value = param2
        return self

    def reset(self):
        super().reset()
        self.value = 0

    def serialize(self, param1):
        self.serializeAs_ServerSessionConstantInteger(param1)

    def serializeAs_ServerSessionConstantInteger(self, param1):
        super().serializeAs_ServerSessionConstant(param1)
        param1.write_int(self.value)

    def deserialize(self, param1):
        self.deserializeAs_ServerSessionConstantInteger(param1)

    def deserializeAs_ServerSessionConstantInteger(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ServerSessionConstantInteger(param1)

    def deserializeAsyncAs_ServerSessionConstantInteger(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_int()


class ServerSessionConstantLong(ServerSessionConstant):
    protocolId = 429

    def __init__(self):
        super().__init__()
        self.value = 0

    def getTypeId(self):
        return 429

    def initServerSessionConstantLong(self, param1=0, param2=0):
        super().initServerSessionConstant(param1)
        self.value = param2
        return self

    def reset(self):
        super().reset()
        self.value = 0

    def serialize(self, param1):
        self.serializeAs_ServerSessionConstantLong(param1)

    def serializeAs_ServerSessionConstantLong(self, param1):
        super().serializeAs_ServerSessionConstant(param1)
        if self.value < -9007199254740990 or self.value > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.value) + ") on element value.")
        param1.write_double(self.value)

    def deserialize(self, param1):
        self.deserializeAs_ServerSessionConstantLong(param1)

    def deserializeAs_ServerSessionConstantLong(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ServerSessionConstantLong(param1)

    def deserializeAsyncAs_ServerSessionConstantLong(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_double()
        if self.value < -9007199254740990 or self.value > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.value) + ") on element of ServerSessionConstantLong.value.")


class ServerSessionConstantString(ServerSessionConstant):
    protocolId = 436

    def __init__(self):
        super().__init__()
        self.value = ""

    def getTypeId(self):
        return 436

    def initServerSessionConstantString(self, param1=0, param2=""):
        super().initServerSessionConstant(param1)
        self.value = param2
        return self

    def reset(self):
        super().reset()
        self.value = ""

    def serialize(self, param1):
        self.serializeAs_ServerSessionConstantString(param1)

    def serializeAs_ServerSessionConstantString(self, param1):
        super().serializeAs_ServerSessionConstant(param1)
        param1.write_utf(self.value)

    def deserialize(self, param1):
        self.deserializeAs_ServerSessionConstantString(param1)

    def deserializeAs_ServerSessionConstantString(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ServerSessionConstantString(param1)

    def deserializeAsyncAs_ServerSessionConstantString(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_utf()


class CharacterBasicMinimalInformations(AbstractCharacterInformation):
    protocolId = 503

    def __init__(self):
        super().__init__()
        self.name = ""

    def getTypeId(self):
        return 503

    def initCharacterBasicMinimalInformations(self, param1=0, param2=""):
        super().initAbstractCharacterInformation(param1)
        self.name = param2
        return self

    def reset(self):
        super().reset()
        self.name = ""

    def serialize(self, param1):
        self.serializeAs_CharacterBasicMinimalInformations(param1)

    def serializeAs_CharacterBasicMinimalInformations(self, param1):
        super().serializeAs_AbstractCharacterInformation(param1)
        param1.write_utf(self.name)

    def deserialize(self, param1):
        self.deserializeAs_CharacterBasicMinimalInformations(param1)

    def deserializeAs_CharacterBasicMinimalInformations(self, param1):
        super().deserialize(param1)
        self._nameFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterBasicMinimalInformations(param1)

    def deserializeAsyncAs_CharacterBasicMinimalInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nameFunc)

    def _nameFunc(self, param1):
        self.name = param1.read_utf()


class ActorExtendedAlignmentInformations(ActorAlignmentInformations):
    protocolId = 202

    def __init__(self):
        super().__init__()
        self.honor = 0
        self.honorGradeFloor = 0
        self.honorNextGradeFloor = 0
        self.aggressable = 0

    def getTypeId(self):
        return 202

    def initActorExtendedAlignmentInformations(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0, param8=0):
        super().initActorAlignmentInformations(param1,param2,param3,param4)
        self.honor = param5
        self.honorGradeFloor = param6
        self.honorNextGradeFloor = param7
        self.aggressable = param8
        return self

    def reset(self):
        super().reset()
        self.honor = 0
        self.honorGradeFloor = 0
        self.honorNextGradeFloor = 0
        self.aggressable = 0

    def serialize(self, param1):
        self.serializeAs_ActorExtendedAlignmentInformations(param1)

    def serializeAs_ActorExtendedAlignmentInformations(self, param1):
        super().serializeAs_ActorAlignmentInformations(param1)
        if self.honor < 0 or self.honor > 20000:
            raise RuntimeError("Forbidden value (" + str(self.honor) + ") on element honor.")
        param1.write_var_short(self.honor)
        if self.honorGradeFloor < 0 or self.honorGradeFloor > 20000:
            raise RuntimeError("Forbidden value (" + str(self.honorGradeFloor) + ") on element honorGradeFloor.")
        param1.write_var_short(self.honorGradeFloor)
        if self.honorNextGradeFloor < 0 or self.honorNextGradeFloor > 20000:
            raise RuntimeError("Forbidden value (" + str(self.honorNextGradeFloor) + ") on element honorNextGradeFloor.")
        param1.write_var_short(self.honorNextGradeFloor)
        param1.write_byte(self.aggressable)

    def deserialize(self, param1):
        self.deserializeAs_ActorExtendedAlignmentInformations(param1)

    def deserializeAs_ActorExtendedAlignmentInformations(self, param1):
        super().deserialize(param1)
        self._honorFunc(param1)
        self._honorGradeFloorFunc(param1)
        self._honorNextGradeFloorFunc(param1)
        self._aggressableFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ActorExtendedAlignmentInformations(param1)

    def deserializeAsyncAs_ActorExtendedAlignmentInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._honorFunc)
        param1.add_child(self._honorGradeFloorFunc)
        param1.add_child(self._honorNextGradeFloorFunc)
        param1.add_child(self._aggressableFunc)

    def _honorFunc(self, param1):
        self.honor = param1.read_var_uh_short()
        if self.honor < 0 or self.honor > 20000:
            raise RuntimeError("Forbidden value (" + str(self.honor) + ") on element of ActorExtendedAlignmentInformations.honor.")

    def _honorGradeFloorFunc(self, param1):
        self.honorGradeFloor = param1.read_var_uh_short()
        if self.honorGradeFloor < 0 or self.honorGradeFloor > 20000:
            raise RuntimeError("Forbidden value (" + str(self.honorGradeFloor) + ") on element of ActorExtendedAlignmentInformations.honorGradeFloor.")

    def _honorNextGradeFloorFunc(self, param1):
        self.honorNextGradeFloor = param1.read_var_uh_short()
        if self.honorNextGradeFloor < 0 or self.honorNextGradeFloor > 20000:
            raise RuntimeError("Forbidden value (" + str(self.honorNextGradeFloor) + ") on element of ActorExtendedAlignmentInformations.honorNextGradeFloor.")

    def _aggressableFunc(self, param1):
        self.aggressable = param1.read_byte()
        if self.aggressable < 0:
            raise RuntimeError("Forbidden value (" + str(self.aggressable) + ") on element of ActorExtendedAlignmentInformations.aggressable.")


class AbstractCharacterToRefurbishInformation(AbstractCharacterInformation):
    protocolId = 475

    def __init__(self):
        super().__init__()
        self.colors = []
        self.cosmeticId = 0
        self._colorstree = FuncTree()

    def getTypeId(self):
        return 475

    def initAbstractCharacterToRefurbishInformation(self, param1=0, param2=[], param3=0):
        super().initAbstractCharacterInformation(param1)
        self.colors = param2
        self.cosmeticId = param3
        return self

    def reset(self):
        super().reset()
        self.colors = []
        self.cosmeticId = 0

    def serialize(self, param1):
        self.serializeAs_AbstractCharacterToRefurbishInformation(param1)

    def serializeAs_AbstractCharacterToRefurbishInformation(self, param1):
        super().serializeAs_AbstractCharacterInformation(param1)
        param1.write_short(len(self.colors))
        _loc2_ = 0
        while _loc2_ < len(self.colors):
            param1.write_int(self.colors[_loc2_])
            _loc2_ += 1
        if self.cosmeticId < 0:
            raise RuntimeError("Forbidden value (" + str(self.cosmeticId) + ") on element cosmeticId.")
        param1.write_var_int(self.cosmeticId)

    def deserialize(self, param1):
        self.deserializeAs_AbstractCharacterToRefurbishInformation(param1)

    def deserializeAs_AbstractCharacterToRefurbishInformation(self, param1):
        _loc4_ = 0
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_int()
            self.colors.append(_loc4_)
            _loc3_ += 1
        self._cosmeticIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AbstractCharacterToRefurbishInformation(param1)

    def deserializeAsyncAs_AbstractCharacterToRefurbishInformation(self, param1):
        super().deserializeAsync(param1)
        self._colorstree = param1.add_child(self._colorstreeFunc)
        param1.add_child(self._cosmeticIdFunc)

    def _colorstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._colorstree.add_child(self._colorsFunc)
            _loc3_ += 1

    def _colorsFunc(self, param1):
        _loc2_ = param1.read_int()
        self.colors.append(_loc2_)

    def _cosmeticIdFunc(self, param1):
        self.cosmeticId = param1.read_var_uh_int()
        if self.cosmeticId < 0:
            raise RuntimeError("Forbidden value (" + str(self.cosmeticId) + ") on element of AbstractCharacterToRefurbishInformation.cosmeticId.")


class CharacterRemodelingInformation(AbstractCharacterInformation):
    protocolId = 479

    def __init__(self):
        super().__init__()
        self.name = ""
        self.breed = 0
        self.sex = False
        self.cosmeticId = 0
        self.colors = []
        self._colorstree = FuncTree()

    def getTypeId(self):
        return 479

    def initCharacterRemodelingInformation(self, param1=0, param2="", param3=0, param4=False, param5=0, param6=[]):
        super().initAbstractCharacterInformation(param1)
        self.name = param2
        self.breed = param3
        self.sex = param4
        self.cosmeticId = param5
        self.colors = param6
        return self

    def reset(self):
        super().reset()
        self.name = ""
        self.breed = 0
        self.sex = False
        self.cosmeticId = 0
        self.colors = []

    def serialize(self, param1):
        self.serializeAs_CharacterRemodelingInformation(param1)

    def serializeAs_CharacterRemodelingInformation(self, param1):
        super().serializeAs_AbstractCharacterInformation(param1)
        param1.write_utf(self.name)
        param1.write_byte(self.breed)
        param1.write_boolean(self.sex)
        if self.cosmeticId < 0:
            raise RuntimeError("Forbidden value (" + str(self.cosmeticId) + ") on element cosmeticId.")
        param1.write_var_short(self.cosmeticId)
        param1.write_short(len(self.colors))
        _loc2_ = 0
        while _loc2_ < len(self.colors):
            param1.write_int(self.colors[_loc2_])
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_CharacterRemodelingInformation(param1)

    def deserializeAs_CharacterRemodelingInformation(self, param1):
        _loc4_ = 0
        super().deserialize(param1)
        self._nameFunc(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)
        self._cosmeticIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_int()
            self.colors.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterRemodelingInformation(param1)

    def deserializeAsyncAs_CharacterRemodelingInformation(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nameFunc)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)
        param1.add_child(self._cosmeticIdFunc)
        self._colorstree = param1.add_child(self._colorstreeFunc)

    def _nameFunc(self, param1):
        self.name = param1.read_utf()

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()

    def _cosmeticIdFunc(self, param1):
        self.cosmeticId = param1.read_var_uh_short()
        if self.cosmeticId < 0:
            raise RuntimeError("Forbidden value (" + str(self.cosmeticId) + ") on element of CharacterRemodelingInformation.cosmeticId.")

    def _colorstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._colorstree.add_child(self._colorsFunc)
            _loc3_ += 1

    def _colorsFunc(self, param1):
        _loc2_ = param1.read_int()
        self.colors.append(_loc2_)


class PlayerStatusExtended(PlayerStatus):
    protocolId = 414

    def __init__(self):
        super().__init__()
        self.message = ""

    def getTypeId(self):
        return 414

    def initPlayerStatusExtended(self, param1=1, param2=""):
        super().initPlayerStatus(param1)
        self.message = param2
        return self

    def reset(self):
        super().reset()
        self.message = ""

    def serialize(self, param1):
        self.serializeAs_PlayerStatusExtended(param1)

    def serializeAs_PlayerStatusExtended(self, param1):
        super().serializeAs_PlayerStatus(param1)
        param1.write_utf(self.message)

    def deserialize(self, param1):
        self.deserializeAs_PlayerStatusExtended(param1)

    def deserializeAs_PlayerStatusExtended(self, param1):
        super().deserialize(param1)
        self._messageFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PlayerStatusExtended(param1)

    def deserializeAsyncAs_PlayerStatusExtended(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._messageFunc)

    def _messageFunc(self, param1):
        self.message = param1.read_utf()


class FightEntityDispositionInformations(EntityDispositionInformations):
    protocolId = 217

    def __init__(self):
        super().__init__()
        self.carryingCharacterId = 0

    def getTypeId(self):
        return 217

    def initFightEntityDispositionInformations(self, param1=0, param2=1, param3=0):
        super().initEntityDispositionInformations(param1,param2)
        self.carryingCharacterId = param3
        return self

    def reset(self):
        super().reset()
        self.carryingCharacterId = 0

    def serialize(self, param1):
        self.serializeAs_FightEntityDispositionInformations(param1)

    def serializeAs_FightEntityDispositionInformations(self, param1):
        super().serializeAs_EntityDispositionInformations(param1)
        if self.carryingCharacterId < -9007199254740990 or self.carryingCharacterId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.carryingCharacterId) + ") on element carryingCharacterId.")
        param1.write_double(self.carryingCharacterId)

    def deserialize(self, param1):
        self.deserializeAs_FightEntityDispositionInformations(param1)

    def deserializeAs_FightEntityDispositionInformations(self, param1):
        super().deserialize(param1)
        self._carryingCharacterIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightEntityDispositionInformations(param1)

    def deserializeAsyncAs_FightEntityDispositionInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._carryingCharacterIdFunc)

    def _carryingCharacterIdFunc(self, param1):
        self.carryingCharacterId = param1.read_double()
        if self.carryingCharacterId < -9007199254740990 or self.carryingCharacterId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.carryingCharacterId) + ") on element of FightEntityDispositionInformations.carryingCharacterId.")


class IdentifiedEntityDispositionInformations(EntityDispositionInformations):
    protocolId = 107

    def __init__(self):
        super().__init__()
        self.id = 0

    def getTypeId(self):
        return 107

    def initIdentifiedEntityDispositionInformations(self, param1=0, param2=1, param3=0):
        super().initEntityDispositionInformations(param1,param2)
        self.id = param3
        return self

    def reset(self):
        super().reset()
        self.id = 0

    def serialize(self, param1):
        self.serializeAs_IdentifiedEntityDispositionInformations(param1)

    def serializeAs_IdentifiedEntityDispositionInformations(self, param1):
        super().serializeAs_EntityDispositionInformations(param1)
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_double(self.id)

    def deserialize(self, param1):
        self.deserializeAs_IdentifiedEntityDispositionInformations(param1)

    def deserializeAs_IdentifiedEntityDispositionInformations(self, param1):
        super().deserialize(param1)
        self._idFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_IdentifiedEntityDispositionInformations(param1)

    def deserializeAsyncAs_IdentifiedEntityDispositionInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._idFunc)

    def _idFunc(self, param1):
        self.id = param1.read_double()
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of IdentifiedEntityDispositionInformations.id.")


class MapCoordinatesAndId(MapCoordinates):
    protocolId = 392

    def __init__(self):
        super().__init__()
        self.mapId = 0

    def getTypeId(self):
        return 392

    def initMapCoordinatesAndId(self, param1=0, param2=0, param3=0):
        super().initMapCoordinates(param1,param2)
        self.mapId = param3
        return self

    def reset(self):
        super().reset()
        self.mapId = 0

    def serialize(self, param1):
        self.serializeAs_MapCoordinatesAndId(param1)

    def serializeAs_MapCoordinatesAndId(self, param1):
        super().serializeAs_MapCoordinates(param1)
        param1.write_int(self.mapId)

    def deserialize(self, param1):
        self.deserializeAs_MapCoordinatesAndId(param1)

    def deserializeAs_MapCoordinatesAndId(self, param1):
        super().deserialize(param1)
        self._mapIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MapCoordinatesAndId(param1)

    def deserializeAsyncAs_MapCoordinatesAndId(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._mapIdFunc)

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()


class TaxCollectorStaticExtendedInformations(TaxCollectorStaticInformations):
    protocolId = 440

    def __init__(self):
        super().__init__()
        self.allianceIdentity = AllianceInformations()
        self._allianceIdentitytree = FuncTree()

    def getTypeId(self):
        return 440

    def initTaxCollectorStaticExtendedInformations(self, param1=0, param2=0, param3=None, param4=None):
        super().initTaxCollectorStaticInformations(param1,param2,param3)
        self.allianceIdentity = param4
        return self

    def reset(self):
        super().reset()
        self.allianceIdentity = AllianceInformations()

    def serialize(self, param1):
        self.serializeAs_TaxCollectorStaticExtendedInformations(param1)

    def serializeAs_TaxCollectorStaticExtendedInformations(self, param1):
        super().serializeAs_TaxCollectorStaticInformations(param1)
        self.allianceIdentity.serializeAs_AllianceInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorStaticExtendedInformations(param1)

    def deserializeAs_TaxCollectorStaticExtendedInformations(self, param1):
        super().deserialize(param1)
        self.allianceIdentity = AllianceInformations()
        self.allianceIdentity.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorStaticExtendedInformations(param1)

    def deserializeAsyncAs_TaxCollectorStaticExtendedInformations(self, param1):
        super().deserializeAsync(param1)
        self._allianceIdentitytree = param1.add_child(self._allianceIdentitytreeFunc)

    def _allianceIdentitytreeFunc(self, param1):
        self.allianceIdentity = AllianceInformations()
        self.allianceIdentity.deserializeAsync(self._allianceIdentitytree)


class FightResultExperienceData(FightResultAdditionalData):
    protocolId = 192

    def __init__(self):
        super().__init__()
        self.experience = 0
        self.showExperience = False
        self.experienceLevelFloor = 0
        self.showExperienceLevelFloor = False
        self.experienceNextLevelFloor = 0
        self.showExperienceNextLevelFloor = False
        self.experienceFightDelta = 0
        self.showExperienceFightDelta = False
        self.experienceForGuild = 0
        self.showExperienceForGuild = False
        self.experienceForMount = 0
        self.showExperienceForMount = False
        self.isIncarnationExperience = False
        self.rerollExperienceMul = 0

    def getTypeId(self):
        return 192

    def initFightResultExperienceData(self, param1=0, param2=False, param3=0, param4=False, param5=0, param6=False, param7=0, param8=False, param9=0, param10=False, param11=0, param12=False, param13=False, param14=0):
        self.experience = param1
        self.showExperience = param2
        self.experienceLevelFloor = param3
        self.showExperienceLevelFloor = param4
        self.experienceNextLevelFloor = param5
        self.showExperienceNextLevelFloor = param6
        self.experienceFightDelta = param7
        self.showExperienceFightDelta = param8
        self.experienceForGuild = param9
        self.showExperienceForGuild = param10
        self.experienceForMount = param11
        self.showExperienceForMount = param12
        self.isIncarnationExperience = param13
        self.rerollExperienceMul = param14
        return self

    def reset(self):
        self.experience = 0
        self.showExperience = False
        self.experienceLevelFloor = 0
        self.showExperienceLevelFloor = False
        self.experienceNextLevelFloor = 0
        self.showExperienceNextLevelFloor = False
        self.experienceFightDelta = 0
        self.showExperienceFightDelta = False
        self.experienceForGuild = 0
        self.showExperienceForGuild = False
        self.experienceForMount = 0
        self.showExperienceForMount = False
        self.isIncarnationExperience = False
        self.rerollExperienceMul = 0

    def serialize(self, param1):
        self.serializeAs_FightResultExperienceData(param1)

    def serializeAs_FightResultExperienceData(self, param1):
        super().serializeAs_FightResultAdditionalData(param1)
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.showExperience)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.showExperienceLevelFloor)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,2,self.showExperienceNextLevelFloor)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,3,self.showExperienceFightDelta)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,4,self.showExperienceForGuild)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,5,self.showExperienceForMount)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,6,self.isIncarnationExperience)
        param1.write_byte(_loc2_)
        if self.experience < 0 or self.experience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element experience.")
        param1.write_var_long(self.experience)
        if self.experienceLevelFloor < 0 or self.experienceLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceLevelFloor) + ") on element experienceLevelFloor.")
        param1.write_var_long(self.experienceLevelFloor)
        if self.experienceNextLevelFloor < 0 or self.experienceNextLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceNextLevelFloor) + ") on element experienceNextLevelFloor.")
        param1.write_var_long(self.experienceNextLevelFloor)
        if self.experienceFightDelta < 0 or self.experienceFightDelta > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceFightDelta) + ") on element experienceFightDelta.")
        param1.write_var_long(self.experienceFightDelta)
        if self.experienceForGuild < 0 or self.experienceForGuild > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceForGuild) + ") on element experienceForGuild.")
        param1.write_var_long(self.experienceForGuild)
        if self.experienceForMount < 0 or self.experienceForMount > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceForMount) + ") on element experienceForMount.")
        param1.write_var_long(self.experienceForMount)
        if self.rerollExperienceMul < 0:
            raise RuntimeError("Forbidden value (" + str(self.rerollExperienceMul) + ") on element rerollExperienceMul.")
        param1.write_byte(self.rerollExperienceMul)

    def deserialize(self, param1):
        self.deserializeAs_FightResultExperienceData(param1)

    def deserializeAs_FightResultExperienceData(self, param1):
        super().deserialize(param1)
        self.deserializeByteBoxes(param1)
        self._experienceFunc(param1)
        self._experienceLevelFloorFunc(param1)
        self._experienceNextLevelFloorFunc(param1)
        self._experienceFightDeltaFunc(param1)
        self._experienceForGuildFunc(param1)
        self._experienceForMountFunc(param1)
        self._rerollExperienceMulFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightResultExperienceData(param1)

    def deserializeAsyncAs_FightResultExperienceData(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self.deserializeByteBoxes)
        param1.add_child(self._experienceFunc)
        param1.add_child(self._experienceLevelFloorFunc)
        param1.add_child(self._experienceNextLevelFloorFunc)
        param1.add_child(self._experienceFightDeltaFunc)
        param1.add_child(self._experienceForGuildFunc)
        param1.add_child(self._experienceForMountFunc)
        param1.add_child(self._rerollExperienceMulFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.showExperience = BooleanByteWrapper.get_flag(_loc2_,0)
        self.showExperienceLevelFloor = BooleanByteWrapper.get_flag(_loc2_,1)
        self.showExperienceNextLevelFloor = BooleanByteWrapper.get_flag(_loc2_,2)
        self.showExperienceFightDelta = BooleanByteWrapper.get_flag(_loc2_,3)
        self.showExperienceForGuild = BooleanByteWrapper.get_flag(_loc2_,4)
        self.showExperienceForMount = BooleanByteWrapper.get_flag(_loc2_,5)
        self.isIncarnationExperience = BooleanByteWrapper.get_flag(_loc2_,6)

    def _experienceFunc(self, param1):
        self.experience = param1.read_var_uh_long()
        if self.experience < 0 or self.experience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element of FightResultExperienceData.experience.")

    def _experienceLevelFloorFunc(self, param1):
        self.experienceLevelFloor = param1.read_var_uh_long()
        if self.experienceLevelFloor < 0 or self.experienceLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceLevelFloor) + ") on element of FightResultExperienceData.experienceLevelFloor.")

    def _experienceNextLevelFloorFunc(self, param1):
        self.experienceNextLevelFloor = param1.read_var_uh_long()
        if self.experienceNextLevelFloor < 0 or self.experienceNextLevelFloor > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceNextLevelFloor) + ") on element of FightResultExperienceData.experienceNextLevelFloor.")

    def _experienceFightDeltaFunc(self, param1):
        self.experienceFightDelta = param1.read_var_uh_long()
        if self.experienceFightDelta < 0 or self.experienceFightDelta > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceFightDelta) + ") on element of FightResultExperienceData.experienceFightDelta.")

    def _experienceForGuildFunc(self, param1):
        self.experienceForGuild = param1.read_var_uh_long()
        if self.experienceForGuild < 0 or self.experienceForGuild > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceForGuild) + ") on element of FightResultExperienceData.experienceForGuild.")

    def _experienceForMountFunc(self, param1):
        self.experienceForMount = param1.read_var_uh_long()
        if self.experienceForMount < 0 or self.experienceForMount > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experienceForMount) + ") on element of FightResultExperienceData.experienceForMount.")

    def _rerollExperienceMulFunc(self, param1):
        self.rerollExperienceMul = param1.read_byte()
        if self.rerollExperienceMul < 0:
            raise RuntimeError("Forbidden value (" + str(self.rerollExperienceMul) + ") on element of FightResultExperienceData.rerollExperienceMul.")


class FightResultFighterListEntry(FightResultListEntry):
    protocolId = 189

    def __init__(self):
        super().__init__()
        self.id = 0
        self.alive = False

    def getTypeId(self):
        return 189

    def initFightResultFighterListEntry(self, param1=0, param2=0, param3=None, param4=0, param5=False):
        super().initFightResultListEntry(param1,param2,param3)
        self.id = param4
        self.alive = param5
        return self

    def reset(self):
        super().reset()
        self.id = 0
        self.alive = False

    def serialize(self, param1):
        self.serializeAs_FightResultFighterListEntry(param1)

    def serializeAs_FightResultFighterListEntry(self, param1):
        super().serializeAs_FightResultListEntry(param1)
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element id.")
        param1.write_double(self.id)
        param1.write_boolean(self.alive)

    def deserialize(self, param1):
        self.deserializeAs_FightResultFighterListEntry(param1)

    def deserializeAs_FightResultFighterListEntry(self, param1):
        super().deserialize(param1)
        self._idFunc(param1)
        self._aliveFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightResultFighterListEntry(param1)

    def deserializeAsyncAs_FightResultFighterListEntry(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._idFunc)
        param1.add_child(self._aliveFunc)

    def _idFunc(self, param1):
        self.id = param1.read_double()
        if self.id < -9007199254740990 or self.id > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of FightResultFighterListEntry.id.")

    def _aliveFunc(self, param1):
        self.alive = param1.read_boolean()


class FightResultPvpData(FightResultAdditionalData):
    protocolId = 190

    def __init__(self):
        super().__init__()
        self.grade = 0
        self.minHonorForGrade = 0
        self.maxHonorForGrade = 0
        self.honor = 0
        self.honorDelta = 0

    def getTypeId(self):
        return 190

    def initFightResultPvpData(self, param1=0, param2=0, param3=0, param4=0, param5=0):
        self.grade = param1
        self.minHonorForGrade = param2
        self.maxHonorForGrade = param3
        self.honor = param4
        self.honorDelta = param5
        return self

    def reset(self):
        self.grade = 0
        self.minHonorForGrade = 0
        self.maxHonorForGrade = 0
        self.honor = 0
        self.honorDelta = 0

    def serialize(self, param1):
        self.serializeAs_FightResultPvpData(param1)

    def serializeAs_FightResultPvpData(self, param1):
        super().serializeAs_FightResultAdditionalData(param1)
        if self.grade < 0 or self.grade > 255:
            raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element grade.")
        param1.write_byte(self.grade)
        if self.minHonorForGrade < 0 or self.minHonorForGrade > 20000:
            raise RuntimeError("Forbidden value (" + str(self.minHonorForGrade) + ") on element minHonorForGrade.")
        param1.write_var_short(self.minHonorForGrade)
        if self.maxHonorForGrade < 0 or self.maxHonorForGrade > 20000:
            raise RuntimeError("Forbidden value (" + str(self.maxHonorForGrade) + ") on element maxHonorForGrade.")
        param1.write_var_short(self.maxHonorForGrade)
        if self.honor < 0 or self.honor > 20000:
            raise RuntimeError("Forbidden value (" + str(self.honor) + ") on element honor.")
        param1.write_var_short(self.honor)
        param1.write_var_short(self.honorDelta)

    def deserialize(self, param1):
        self.deserializeAs_FightResultPvpData(param1)

    def deserializeAs_FightResultPvpData(self, param1):
        super().deserialize(param1)
        self._gradeFunc(param1)
        self._minHonorForGradeFunc(param1)
        self._maxHonorForGradeFunc(param1)
        self._honorFunc(param1)
        self._honorDeltaFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightResultPvpData(param1)

    def deserializeAsyncAs_FightResultPvpData(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._gradeFunc)
        param1.add_child(self._minHonorForGradeFunc)
        param1.add_child(self._maxHonorForGradeFunc)
        param1.add_child(self._honorFunc)
        param1.add_child(self._honorDeltaFunc)

    def _gradeFunc(self, param1):
        self.grade = param1.read_unsigned_byte()
        if self.grade < 0 or self.grade > 255:
            raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element of FightResultPvpData.grade.")

    def _minHonorForGradeFunc(self, param1):
        self.minHonorForGrade = param1.read_var_uh_short()
        if self.minHonorForGrade < 0 or self.minHonorForGrade > 20000:
            raise RuntimeError("Forbidden value (" + str(self.minHonorForGrade) + ") on element of FightResultPvpData.minHonorForGrade.")

    def _maxHonorForGradeFunc(self, param1):
        self.maxHonorForGrade = param1.read_var_uh_short()
        if self.maxHonorForGrade < 0 or self.maxHonorForGrade > 20000:
            raise RuntimeError("Forbidden value (" + str(self.maxHonorForGrade) + ") on element of FightResultPvpData.maxHonorForGrade.")

    def _honorFunc(self, param1):
        self.honor = param1.read_var_uh_short()
        if self.honor < 0 or self.honor > 20000:
            raise RuntimeError("Forbidden value (" + str(self.honor) + ") on element of FightResultPvpData.honor.")

    def _honorDeltaFunc(self, param1):
        self.honorDelta = param1.read_var_short()


class FightTeamInformations(AbstractFightTeamInformations):
    protocolId = 33

    def __init__(self):
        super().__init__()
        self.teamMembers = []
        self._teamMemberstree = FuncTree()

    def getTypeId(self):
        return 33

    def initFightTeamInformations(self, param1=2, param2=0, param3=0, param4=0, param5=0, param6=[]):
        super().initAbstractFightTeamInformations(param1,param2,param3,param4,param5)
        self.teamMembers = param6
        return self

    def reset(self):
        super().reset()
        self.teamMembers = []

    def serialize(self, param1):
        self.serializeAs_FightTeamInformations(param1)

    def serializeAs_FightTeamInformations(self, param1):
        super().serializeAs_AbstractFightTeamInformations(param1)
        param1.write_short(len(self.teamMembers))
        _loc2_ = 0
        while _loc2_ < len(self.teamMembers):
            param1.write_short(as_parent(self.teamMembers[_loc2_], FightTeamMemberInformations).getTypeId())
            as_parent(self.teamMembers[_loc2_], FightTeamMemberInformations).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_FightTeamInformations(param1)

    def deserializeAs_FightTeamInformations(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(FightTeamMemberInformations,_loc4_)
            _loc5_.deserialize(param1)
            self.teamMembers.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTeamInformations(param1)

    def deserializeAsyncAs_FightTeamInformations(self, param1):
        super().deserializeAsync(param1)
        self._teamMemberstree = param1.add_child(self._teamMemberstreeFunc)

    def _teamMemberstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._teamMemberstree.add_child(self._teamMembersFunc)
            _loc3_ += 1

    def _teamMembersFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(FightTeamMemberInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.teamMembers.append(_loc3_)


class FightTeamLightInformations(AbstractFightTeamInformations):
    protocolId = 115

    def __init__(self):
        super().__init__()
        self.teamMembersCount = 0
        self.meanLevel = 0
        self.hasFriend = False
        self.hasGuildMember = False
        self.hasAllianceMember = False
        self.hasGroupMember = False
        self.hasMyTaxCollector = False

    def getTypeId(self):
        return 115

    def initFightTeamLightInformations(self, param1=2, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0, param8=False, param9=False, param10=False, param11=False, param12=False):
        super().initAbstractFightTeamInformations(param1,param2,param3,param4,param5)
        self.teamMembersCount = param6
        self.meanLevel = param7
        self.hasFriend = param8
        self.hasGuildMember = param9
        self.hasAllianceMember = param10
        self.hasGroupMember = param11
        self.hasMyTaxCollector = param12
        return self

    def reset(self):
        super().reset()
        self.teamMembersCount = 0
        self.meanLevel = 0
        self.hasFriend = False
        self.hasGuildMember = False
        self.hasAllianceMember = False
        self.hasGroupMember = False
        self.hasMyTaxCollector = False

    def serialize(self, param1):
        self.serializeAs_FightTeamLightInformations(param1)

    def serializeAs_FightTeamLightInformations(self, param1):
        super().serializeAs_AbstractFightTeamInformations(param1)
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.hasFriend)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.hasGuildMember)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,2,self.hasAllianceMember)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,3,self.hasGroupMember)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,4,self.hasMyTaxCollector)
        param1.write_byte(_loc2_)
        if self.teamMembersCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.teamMembersCount) + ") on element teamMembersCount.")
        param1.write_byte(self.teamMembersCount)
        if self.meanLevel < 0:
            raise RuntimeError("Forbidden value (" + str(self.meanLevel) + ") on element meanLevel.")
        param1.write_var_int(self.meanLevel)

    def deserialize(self, param1):
        self.deserializeAs_FightTeamLightInformations(param1)

    def deserializeAs_FightTeamLightInformations(self, param1):
        super().deserialize(param1)
        self.deserializeByteBoxes(param1)
        self._teamMembersCountFunc(param1)
        self._meanLevelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTeamLightInformations(param1)

    def deserializeAsyncAs_FightTeamLightInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self.deserializeByteBoxes)
        param1.add_child(self._teamMembersCountFunc)
        param1.add_child(self._meanLevelFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.hasFriend = BooleanByteWrapper.get_flag(_loc2_,0)
        self.hasGuildMember = BooleanByteWrapper.get_flag(_loc2_,1)
        self.hasAllianceMember = BooleanByteWrapper.get_flag(_loc2_,2)
        self.hasGroupMember = BooleanByteWrapper.get_flag(_loc2_,3)
        self.hasMyTaxCollector = BooleanByteWrapper.get_flag(_loc2_,4)

    def _teamMembersCountFunc(self, param1):
        self.teamMembersCount = param1.read_byte()
        if self.teamMembersCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.teamMembersCount) + ") on element of FightTeamLightInformations.teamMembersCount.")

    def _meanLevelFunc(self, param1):
        self.meanLevel = param1.read_var_uh_int()
        if self.meanLevel < 0:
            raise RuntimeError("Forbidden value (" + str(self.meanLevel) + ") on element of FightTeamLightInformations.meanLevel.")


class FightTeamMemberCharacterInformations(FightTeamMemberInformations):
    protocolId = 13

    def __init__(self):
        super().__init__()
        self.name = ""
        self.level = 0

    def getTypeId(self):
        return 13

    def initFightTeamMemberCharacterInformations(self, param1=0, param2="", param3=0):
        super().initFightTeamMemberInformations(param1)
        self.name = param2
        self.level = param3
        return self

    def reset(self):
        super().reset()
        self.name = ""
        self.level = 0

    def serialize(self, param1):
        self.serializeAs_FightTeamMemberCharacterInformations(param1)

    def serializeAs_FightTeamMemberCharacterInformations(self, param1):
        super().serializeAs_FightTeamMemberInformations(param1)
        param1.write_utf(self.name)
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)

    def deserialize(self, param1):
        self.deserializeAs_FightTeamMemberCharacterInformations(param1)

    def deserializeAs_FightTeamMemberCharacterInformations(self, param1):
        super().deserialize(param1)
        self._nameFunc(param1)
        self._levelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTeamMemberCharacterInformations(param1)

    def deserializeAsyncAs_FightTeamMemberCharacterInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nameFunc)
        param1.add_child(self._levelFunc)

    def _nameFunc(self, param1):
        self.name = param1.read_utf()

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightTeamMemberCharacterInformations.level.")


class FightTeamMemberCompanionInformations(FightTeamMemberInformations):
    protocolId = 451

    def __init__(self):
        super().__init__()
        self.companionId = 0
        self.level = 0
        self.masterId = 0

    def getTypeId(self):
        return 451

    def initFightTeamMemberCompanionInformations(self, param1=0, param2=0, param3=0, param4=0):
        super().initFightTeamMemberInformations(param1)
        self.companionId = param2
        self.level = param3
        self.masterId = param4
        return self

    def reset(self):
        super().reset()
        self.companionId = 0
        self.level = 0
        self.masterId = 0

    def serialize(self, param1):
        self.serializeAs_FightTeamMemberCompanionInformations(param1)

    def serializeAs_FightTeamMemberCompanionInformations(self, param1):
        super().serializeAs_FightTeamMemberInformations(param1)
        if self.companionId < 0:
            raise RuntimeError("Forbidden value (" + str(self.companionId) + ") on element companionId.")
        param1.write_byte(self.companionId)
        if self.level < 1 or self.level > 200:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)
        if self.masterId < -9007199254740990 or self.masterId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element masterId.")
        param1.write_double(self.masterId)

    def deserialize(self, param1):
        self.deserializeAs_FightTeamMemberCompanionInformations(param1)

    def deserializeAs_FightTeamMemberCompanionInformations(self, param1):
        super().deserialize(param1)
        self._companionIdFunc(param1)
        self._levelFunc(param1)
        self._masterIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTeamMemberCompanionInformations(param1)

    def deserializeAsyncAs_FightTeamMemberCompanionInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._companionIdFunc)
        param1.add_child(self._levelFunc)
        param1.add_child(self._masterIdFunc)

    def _companionIdFunc(self, param1):
        self.companionId = param1.read_byte()
        if self.companionId < 0:
            raise RuntimeError("Forbidden value (" + str(self.companionId) + ") on element of FightTeamMemberCompanionInformations.companionId.")

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 1 or self.level > 200:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightTeamMemberCompanionInformations.level.")

    def _masterIdFunc(self, param1):
        self.masterId = param1.read_double()
        if self.masterId < -9007199254740990 or self.masterId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element of FightTeamMemberCompanionInformations.masterId.")


class FightTeamMemberMonsterInformations(FightTeamMemberInformations):
    protocolId = 6

    def __init__(self):
        super().__init__()
        self.monsterId = 0
        self.grade = 0

    def getTypeId(self):
        return 6

    def initFightTeamMemberMonsterInformations(self, param1=0, param2=0, param3=0):
        super().initFightTeamMemberInformations(param1)
        self.monsterId = param2
        self.grade = param3
        return self

    def reset(self):
        super().reset()
        self.monsterId = 0
        self.grade = 0

    def serialize(self, param1):
        self.serializeAs_FightTeamMemberMonsterInformations(param1)

    def serializeAs_FightTeamMemberMonsterInformations(self, param1):
        super().serializeAs_FightTeamMemberInformations(param1)
        param1.write_int(self.monsterId)
        if self.grade < 0:
            raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element grade.")
        param1.write_byte(self.grade)

    def deserialize(self, param1):
        self.deserializeAs_FightTeamMemberMonsterInformations(param1)

    def deserializeAs_FightTeamMemberMonsterInformations(self, param1):
        super().deserialize(param1)
        self._monsterIdFunc(param1)
        self._gradeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTeamMemberMonsterInformations(param1)

    def deserializeAsyncAs_FightTeamMemberMonsterInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._monsterIdFunc)
        param1.add_child(self._gradeFunc)

    def _monsterIdFunc(self, param1):
        self.monsterId = param1.read_int()

    def _gradeFunc(self, param1):
        self.grade = param1.read_byte()
        if self.grade < 0:
            raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element of FightTeamMemberMonsterInformations.grade.")


class FightTeamMemberTaxCollectorInformations(FightTeamMemberInformations):
    protocolId = 177

    def __init__(self):
        super().__init__()
        self.firstNameId = 0
        self.lastNameId = 0
        self.level = 0
        self.guildId = 0
        self.uid = 0

    def getTypeId(self):
        return 177

    def initFightTeamMemberTaxCollectorInformations(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0):
        super().initFightTeamMemberInformations(param1)
        self.firstNameId = param2
        self.lastNameId = param3
        self.level = param4
        self.guildId = param5
        self.uid = param6
        return self

    def reset(self):
        super().reset()
        self.firstNameId = 0
        self.lastNameId = 0
        self.level = 0
        self.guildId = 0
        self.uid = 0

    def serialize(self, param1):
        self.serializeAs_FightTeamMemberTaxCollectorInformations(param1)

    def serializeAs_FightTeamMemberTaxCollectorInformations(self, param1):
        super().serializeAs_FightTeamMemberInformations(param1)
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element firstNameId.")
        param1.write_var_short(self.firstNameId)
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element lastNameId.")
        param1.write_var_short(self.lastNameId)
        if self.level < 1 or self.level > 200:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)
        if self.guildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element guildId.")
        param1.write_var_int(self.guildId)
        if self.uid < 0:
            raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element uid.")
        param1.write_var_int(self.uid)

    def deserialize(self, param1):
        self.deserializeAs_FightTeamMemberTaxCollectorInformations(param1)

    def deserializeAs_FightTeamMemberTaxCollectorInformations(self, param1):
        super().deserialize(param1)
        self._firstNameIdFunc(param1)
        self._lastNameIdFunc(param1)
        self._levelFunc(param1)
        self._guildIdFunc(param1)
        self._uidFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTeamMemberTaxCollectorInformations(param1)

    def deserializeAsyncAs_FightTeamMemberTaxCollectorInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._firstNameIdFunc)
        param1.add_child(self._lastNameIdFunc)
        param1.add_child(self._levelFunc)
        param1.add_child(self._guildIdFunc)
        param1.add_child(self._uidFunc)

    def _firstNameIdFunc(self, param1):
        self.firstNameId = param1.read_var_uh_short()
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of FightTeamMemberTaxCollectorInformations.firstNameId.")

    def _lastNameIdFunc(self, param1):
        self.lastNameId = param1.read_var_uh_short()
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of FightTeamMemberTaxCollectorInformations.lastNameId.")

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 1 or self.level > 200:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightTeamMemberTaxCollectorInformations.level.")

    def _guildIdFunc(self, param1):
        self.guildId = param1.read_var_uh_int()
        if self.guildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of FightTeamMemberTaxCollectorInformations.guildId.")

    def _uidFunc(self, param1):
        self.uid = param1.read_var_uh_int()
        if self.uid < 0:
            raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element of FightTeamMemberTaxCollectorInformations.uid.")


class GameFightFighterCompanionLightInformations(GameFightFighterLightInformations):
    protocolId = 454

    def __init__(self):
        super().__init__()
        self.companionId = 0
        self.masterId = 0

    def getTypeId(self):
        return 454

    def initGameFightFighterCompanionLightInformations(self, param1=0, param2=0, param3=0, param4=0, param5=False, param6=False, param7=0, param8=0):
        super().initGameFightFighterLightInformations(param1,param2,param3,param4,param5,param6)
        self.companionId = param7
        self.masterId = param8
        return self

    def reset(self):
        super().reset()
        self.companionId = 0
        self.masterId = 0

    def serialize(self, param1):
        self.serializeAs_GameFightFighterCompanionLightInformations(param1)

    def serializeAs_GameFightFighterCompanionLightInformations(self, param1):
        super().serializeAs_GameFightFighterLightInformations(param1)
        if self.companionId < 0:
            raise RuntimeError("Forbidden value (" + str(self.companionId) + ") on element companionId.")
        param1.write_byte(self.companionId)
        if self.masterId < -9007199254740990 or self.masterId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element masterId.")
        param1.write_double(self.masterId)

    def deserialize(self, param1):
        self.deserializeAs_GameFightFighterCompanionLightInformations(param1)

    def deserializeAs_GameFightFighterCompanionLightInformations(self, param1):
        super().deserialize(param1)
        self._companionIdFunc(param1)
        self._masterIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightFighterCompanionLightInformations(param1)

    def deserializeAsyncAs_GameFightFighterCompanionLightInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._companionIdFunc)
        param1.add_child(self._masterIdFunc)

    def _companionIdFunc(self, param1):
        self.companionId = param1.read_byte()
        if self.companionId < 0:
            raise RuntimeError("Forbidden value (" + str(self.companionId) + ") on element of GameFightFighterCompanionLightInformations.companionId.")

    def _masterIdFunc(self, param1):
        self.masterId = param1.read_double()
        if self.masterId < -9007199254740990 or self.masterId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element of GameFightFighterCompanionLightInformations.masterId.")


class GameFightFighterInformations(GameContextActorInformations):
    protocolId = 143

    def __init__(self):
        super().__init__()
        self.teamId = 2
        self.wave = 0
        self.alive = False
        self.stats = GameFightMinimalStats()
        self.previousPositions = []
        self._statstree = FuncTree()
        self._previousPositionstree = FuncTree()

    def getTypeId(self):
        return 143

    def initGameFightFighterInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[]):
        super().initGameContextActorInformations(param1,param2,param3)
        self.teamId = param4
        self.wave = param5
        self.alive = param6
        self.stats = param7
        self.previousPositions = param8
        return self

    def reset(self):
        super().reset()
        self.teamId = 2
        self.wave = 0
        self.alive = False
        self.stats = GameFightMinimalStats()

    def serialize(self, param1):
        self.serializeAs_GameFightFighterInformations(param1)

    def serializeAs_GameFightFighterInformations(self, param1):
        super().serializeAs_GameContextActorInformations(param1)
        param1.write_byte(self.teamId)
        if self.wave < 0:
            raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element wave.")
        param1.write_byte(self.wave)
        param1.write_boolean(self.alive)
        param1.write_short(self.stats.getTypeId())
        self.stats.serialize(param1)
        param1.write_short(len(self.previousPositions))
        _loc2_ = 0
        while _loc2_ < len(self.previousPositions):
            if self.previousPositions[_loc2_] < 0 or self.previousPositions[_loc2_] > 559:
                raise RuntimeError("Forbidden value (" + str(self.previousPositions[_loc2_]) + ") on element 5 (starting at 1) of previousPositions.")
            param1.write_var_short(self.previousPositions[_loc2_])
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_GameFightFighterInformations(param1)

    def deserializeAs_GameFightFighterInformations(self, param1):
        _loc5_ = 0
        super().deserialize(param1)
        self._teamIdFunc(param1)
        self._waveFunc(param1)
        self._aliveFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        self.stats = ProtocolTypeManager.get_instance(GameFightMinimalStats,_loc2_)
        self.stats.deserialize(param1)
        _loc3_ = param1.read_unsigned_short()
        _loc4_ = 0
        while _loc4_ < _loc3_:
            _loc5_ = param1.read_var_uh_short()
            if _loc5_ < 0 or _loc5_ > 559:
                raise RuntimeError("Forbidden value (" + str(_loc5_) + ") on elements of previousPositions.")
            self.previousPositions.append(_loc5_)
            _loc4_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightFighterInformations(param1)

    def deserializeAsyncAs_GameFightFighterInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._teamIdFunc)
        param1.add_child(self._waveFunc)
        param1.add_child(self._aliveFunc)
        self._statstree = param1.add_child(self._statstreeFunc)
        self._previousPositionstree = param1.add_child(self._previousPositionstreeFunc)

    def _teamIdFunc(self, param1):
        self.teamId = param1.read_byte()
        if self.teamId < 0:
            raise RuntimeError("Forbidden value (" + str(self.teamId) + ") on element of GameFightFighterInformations.teamId.")

    def _waveFunc(self, param1):
        self.wave = param1.read_byte()
        if self.wave < 0:
            raise RuntimeError("Forbidden value (" + str(self.wave) + ") on element of GameFightFighterInformations.wave.")

    def _aliveFunc(self, param1):
        self.alive = param1.read_boolean()

    def _statstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.stats = ProtocolTypeManager.get_instance(GameFightMinimalStats,_loc2_)
        self.stats.deserializeAsync(self._statstree)

    def _previousPositionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._previousPositionstree.add_child(self._previousPositionsFunc)
            _loc3_ += 1

    def _previousPositionsFunc(self, param1):
        _loc2_ = param1.read_var_uh_short()
        if _loc2_ < 0 or _loc2_ > 559:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of previousPositions.")
        self.previousPositions.append(_loc2_)


class GameFightFighterMonsterLightInformations(GameFightFighterLightInformations):
    protocolId = 455

    def __init__(self):
        super().__init__()
        self.creatureGenericId = 0

    def getTypeId(self):
        return 455

    def initGameFightFighterMonsterLightInformations(self, param1=0, param2=0, param3=0, param4=0, param5=False, param6=False, param7=0):
        super().initGameFightFighterLightInformations(param1,param2,param3,param4,param5,param6)
        self.creatureGenericId = param7
        return self

    def reset(self):
        super().reset()
        self.creatureGenericId = 0

    def serialize(self, param1):
        self.serializeAs_GameFightFighterMonsterLightInformations(param1)

    def serializeAs_GameFightFighterMonsterLightInformations(self, param1):
        super().serializeAs_GameFightFighterLightInformations(param1)
        if self.creatureGenericId < 0:
            raise RuntimeError("Forbidden value (" + str(self.creatureGenericId) + ") on element creatureGenericId.")
        param1.write_var_short(self.creatureGenericId)

    def deserialize(self, param1):
        self.deserializeAs_GameFightFighterMonsterLightInformations(param1)

    def deserializeAs_GameFightFighterMonsterLightInformations(self, param1):
        super().deserialize(param1)
        self._creatureGenericIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightFighterMonsterLightInformations(param1)

    def deserializeAsyncAs_GameFightFighterMonsterLightInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._creatureGenericIdFunc)

    def _creatureGenericIdFunc(self, param1):
        self.creatureGenericId = param1.read_var_uh_short()
        if self.creatureGenericId < 0:
            raise RuntimeError("Forbidden value (" + str(self.creatureGenericId) + ") on element of GameFightFighterMonsterLightInformations.creatureGenericId.")


class GameFightFighterNamedLightInformations(GameFightFighterLightInformations):
    protocolId = 456

    def __init__(self):
        super().__init__()
        self.name = ""

    def getTypeId(self):
        return 456

    def initGameFightFighterNamedLightInformations(self, param1=0, param2=0, param3=0, param4=0, param5=False, param6=False, param7=""):
        super().initGameFightFighterLightInformations(param1,param2,param3,param4,param5,param6)
        self.name = param7
        return self

    def reset(self):
        super().reset()
        self.name = ""

    def serialize(self, param1):
        self.serializeAs_GameFightFighterNamedLightInformations(param1)

    def serializeAs_GameFightFighterNamedLightInformations(self, param1):
        super().serializeAs_GameFightFighterLightInformations(param1)
        param1.write_utf(self.name)

    def deserialize(self, param1):
        self.deserializeAs_GameFightFighterNamedLightInformations(param1)

    def deserializeAs_GameFightFighterNamedLightInformations(self, param1):
        super().deserialize(param1)
        self._nameFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightFighterNamedLightInformations(param1)

    def deserializeAsyncAs_GameFightFighterNamedLightInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nameFunc)

    def _nameFunc(self, param1):
        self.name = param1.read_utf()


class GameFightFighterTaxCollectorLightInformations(GameFightFighterLightInformations):
    protocolId = 457

    def __init__(self):
        super().__init__()
        self.firstNameId = 0
        self.lastNameId = 0

    def getTypeId(self):
        return 457

    def initGameFightFighterTaxCollectorLightInformations(self, param1=0, param2=0, param3=0, param4=0, param5=False, param6=False, param7=0, param8=0):
        super().initGameFightFighterLightInformations(param1,param2,param3,param4,param5,param6)
        self.firstNameId = param7
        self.lastNameId = param8
        return self

    def reset(self):
        super().reset()
        self.firstNameId = 0
        self.lastNameId = 0

    def serialize(self, param1):
        self.serializeAs_GameFightFighterTaxCollectorLightInformations(param1)

    def serializeAs_GameFightFighterTaxCollectorLightInformations(self, param1):
        super().serializeAs_GameFightFighterLightInformations(param1)
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element firstNameId.")
        param1.write_var_short(self.firstNameId)
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element lastNameId.")
        param1.write_var_short(self.lastNameId)

    def deserialize(self, param1):
        self.deserializeAs_GameFightFighterTaxCollectorLightInformations(param1)

    def deserializeAs_GameFightFighterTaxCollectorLightInformations(self, param1):
        super().deserialize(param1)
        self._firstNameIdFunc(param1)
        self._lastNameIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightFighterTaxCollectorLightInformations(param1)

    def deserializeAsyncAs_GameFightFighterTaxCollectorLightInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._firstNameIdFunc)
        param1.add_child(self._lastNameIdFunc)

    def _firstNameIdFunc(self, param1):
        self.firstNameId = param1.read_var_uh_short()
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of GameFightFighterTaxCollectorLightInformations.firstNameId.")

    def _lastNameIdFunc(self, param1):
        self.lastNameId = param1.read_var_uh_short()
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of GameFightFighterTaxCollectorLightInformations.lastNameId.")


class GameFightMinimalStatsPreparation(GameFightMinimalStats):
    protocolId = 360

    def __init__(self):
        super().__init__()
        self.initiative = 0

    def getTypeId(self):
        return 360

    def initGameFightMinimalStatsPreparation(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0, param8=0, param9=0, param10=0, param11=False, param12=0, param13=0, param14=0, param15=0, param16=0, param17=0, param18=0, param19=0, param20=0, param21=0, param22=0, param23=0, param24=0, param25=0, param26=0, param27=0, param28=0, param29=0, param30=0, param31=0, param32=0, param33=0, param34=0, param35=0, param36=0, param37=0, param38=0, param39=0, param40=0, param41=0, param42=0, param43=0, param44=0):
        super().initGameFightMinimalStats(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12,param13,param14,param15,param16,param17,param18,param19,param20,param21,param22,param23,param24,param25,param26,param27,param28,param29,param30,param31,param32,param33,param34,param35,param36,param37,param38,param39,param40,param41,param42,param43)
        self.initiative = param44
        return self

    def reset(self):
        super().reset()
        self.initiative = 0

    def serialize(self, param1):
        self.serializeAs_GameFightMinimalStatsPreparation(param1)

    def serializeAs_GameFightMinimalStatsPreparation(self, param1):
        super().serializeAs_GameFightMinimalStats(param1)
        if self.initiative < 0:
            raise RuntimeError("Forbidden value (" + str(self.initiative) + ") on element initiative.")
        param1.write_var_int(self.initiative)

    def deserialize(self, param1):
        self.deserializeAs_GameFightMinimalStatsPreparation(param1)

    def deserializeAs_GameFightMinimalStatsPreparation(self, param1):
        super().deserialize(param1)
        self._initiativeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightMinimalStatsPreparation(param1)

    def deserializeAsyncAs_GameFightMinimalStatsPreparation(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._initiativeFunc)

    def _initiativeFunc(self, param1):
        self.initiative = param1.read_var_uh_int()
        if self.initiative < 0:
            raise RuntimeError("Forbidden value (" + str(self.initiative) + ") on element of GameFightMinimalStatsPreparation.initiative.")


class BasicAllianceInformations(AbstractSocialGroupInfos):
    protocolId = 419

    def __init__(self):
        super().__init__()
        self.allianceId = 0
        self.allianceTag = ""

    def getTypeId(self):
        return 419

    def initBasicAllianceInformations(self, param1=0, param2=""):
        self.allianceId = param1
        self.allianceTag = param2
        return self

    def reset(self):
        self.allianceId = 0
        self.allianceTag = ""

    def serialize(self, param1):
        self.serializeAs_BasicAllianceInformations(param1)

    def serializeAs_BasicAllianceInformations(self, param1):
        super().serializeAs_AbstractSocialGroupInfos(param1)
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element allianceId.")
        param1.write_var_int(self.allianceId)
        param1.write_utf(self.allianceTag)

    def deserialize(self, param1):
        self.deserializeAs_BasicAllianceInformations(param1)

    def deserializeAs_BasicAllianceInformations(self, param1):
        super().deserialize(param1)
        self._allianceIdFunc(param1)
        self._allianceTagFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_BasicAllianceInformations(param1)

    def deserializeAsyncAs_BasicAllianceInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._allianceIdFunc)
        param1.add_child(self._allianceTagFunc)

    def _allianceIdFunc(self, param1):
        self.allianceId = param1.read_var_uh_int()
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element of BasicAllianceInformations.allianceId.")

    def _allianceTagFunc(self, param1):
        self.allianceTag = param1.read_utf()


class BasicGuildInformations(AbstractSocialGroupInfos):
    protocolId = 365

    def __init__(self):
        super().__init__()
        self.guildId = 0
        self.guildName = ""
        self.guildLevel = 0

    def getTypeId(self):
        return 365

    def initBasicGuildInformations(self, param1=0, param2="", param3=0):
        self.guildId = param1
        self.guildName = param2
        self.guildLevel = param3
        return self

    def reset(self):
        self.guildId = 0
        self.guildName = ""
        self.guildLevel = 0

    def serialize(self, param1):
        self.serializeAs_BasicGuildInformations(param1)

    def serializeAs_BasicGuildInformations(self, param1):
        super().serializeAs_AbstractSocialGroupInfos(param1)
        if self.guildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element guildId.")
        param1.write_var_int(self.guildId)
        param1.write_utf(self.guildName)
        if self.guildLevel < 0 or self.guildLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.guildLevel) + ") on element guildLevel.")
        param1.write_byte(self.guildLevel)

    def deserialize(self, param1):
        self.deserializeAs_BasicGuildInformations(param1)

    def deserializeAs_BasicGuildInformations(self, param1):
        super().deserialize(param1)
        self._guildIdFunc(param1)
        self._guildNameFunc(param1)
        self._guildLevelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_BasicGuildInformations(param1)

    def deserializeAsyncAs_BasicGuildInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._guildIdFunc)
        param1.add_child(self._guildNameFunc)
        param1.add_child(self._guildLevelFunc)

    def _guildIdFunc(self, param1):
        self.guildId = param1.read_var_uh_int()
        if self.guildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of BasicGuildInformations.guildId.")

    def _guildNameFunc(self, param1):
        self.guildName = param1.read_utf()

    def _guildLevelFunc(self, param1):
        self.guildLevel = param1.read_unsigned_byte()
        if self.guildLevel < 0 or self.guildLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.guildLevel) + ") on element of BasicGuildInformations.guildLevel.")


class GameRolePlayActorInformations(GameContextActorInformations):
    protocolId = 141

    def getTypeId(self):
        return 141

    def initGameRolePlayActorInformations(self, param1=0, param2=None, param3=None):
        super().initGameContextActorInformations(param1,param2,param3)
        return self

    def reset(self):
        super().reset()

    def serialize(self, param1):
        self.serializeAs_GameRolePlayActorInformations(param1)

    def serializeAs_GameRolePlayActorInformations(self, param1):
        super().serializeAs_GameContextActorInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayActorInformations(param1)

    def deserializeAs_GameRolePlayActorInformations(self, param1):
        super().deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayActorInformations(param1)

    def deserializeAsyncAs_GameRolePlayActorInformations(self, param1):
        super().deserializeAsync(param1)


class GroupMonsterStaticInformationsWithAlternatives(GroupMonsterStaticInformations):
    protocolId = 396

    def __init__(self):
        super().__init__()
        self.alternatives = []
        self._alternativestree = FuncTree()

    def getTypeId(self):
        return 396

    def initGroupMonsterStaticInformationsWithAlternatives(self, param1=None, param2=[], param3=[]):
        super().initGroupMonsterStaticInformations(param1,param2)
        self.alternatives = param3
        return self

    def reset(self):
        super().reset()
        self.alternatives = []

    def serialize(self, param1):
        self.serializeAs_GroupMonsterStaticInformationsWithAlternatives(param1)

    def serializeAs_GroupMonsterStaticInformationsWithAlternatives(self, param1):
        super().serializeAs_GroupMonsterStaticInformations(param1)
        param1.write_short(len(self.alternatives))
        _loc2_ = 0
        while _loc2_ < len(self.alternatives):
            as_parent(self.alternatives[_loc2_], AlternativeMonstersInGroupLightInformations).serializeAs_AlternativeMonstersInGroupLightInformations(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_GroupMonsterStaticInformationsWithAlternatives(param1)

    def deserializeAs_GroupMonsterStaticInformationsWithAlternatives(self, param1):
        _loc4_ = None
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = AlternativeMonstersInGroupLightInformations()
            _loc4_.deserialize(param1)
            self.alternatives.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GroupMonsterStaticInformationsWithAlternatives(param1)

    def deserializeAsyncAs_GroupMonsterStaticInformationsWithAlternatives(self, param1):
        super().deserializeAsync(param1)
        self._alternativestree = param1.add_child(self._alternativestreeFunc)

    def _alternativestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._alternativestree.add_child(self._alternativesFunc)
            _loc3_ += 1

    def _alternativesFunc(self, param1):
        _loc2_ = AlternativeMonstersInGroupLightInformations()
        _loc2_.deserialize(param1)
        self.alternatives.append(_loc2_)


class HumanOptionAlliance(HumanOption):
    protocolId = 425

    def __init__(self):
        super().__init__()
        self.allianceInformations = AllianceInformations()
        self.aggressable = 0
        self._allianceInformationstree = FuncTree()

    def getTypeId(self):
        return 425

    def initHumanOptionAlliance(self, param1=None, param2=0):
        self.allianceInformations = param1
        self.aggressable = param2
        return self

    def reset(self):
        self.allianceInformations = AllianceInformations()

    def serialize(self, param1):
        self.serializeAs_HumanOptionAlliance(param1)

    def serializeAs_HumanOptionAlliance(self, param1):
        super().serializeAs_HumanOption(param1)
        self.allianceInformations.serializeAs_AllianceInformations(param1)
        param1.write_byte(self.aggressable)

    def deserialize(self, param1):
        self.deserializeAs_HumanOptionAlliance(param1)

    def deserializeAs_HumanOptionAlliance(self, param1):
        super().deserialize(param1)
        self.allianceInformations = AllianceInformations()
        self.allianceInformations.deserialize(param1)
        self._aggressableFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanOptionAlliance(param1)

    def deserializeAsyncAs_HumanOptionAlliance(self, param1):
        super().deserializeAsync(param1)
        self._allianceInformationstree = param1.add_child(self._allianceInformationstreeFunc)
        param1.add_child(self._aggressableFunc)

    def _allianceInformationstreeFunc(self, param1):
        self.allianceInformations = AllianceInformations()
        self.allianceInformations.deserializeAsync(self._allianceInformationstree)

    def _aggressableFunc(self, param1):
        self.aggressable = param1.read_byte()
        if self.aggressable < 0:
            raise RuntimeError("Forbidden value (" + str(self.aggressable) + ") on element of HumanOptionAlliance.aggressable.")


class HumanOptionEmote(HumanOption):
    protocolId = 407

    def __init__(self):
        super().__init__()
        self.emoteId = 0
        self.emoteStartTime = 0

    def getTypeId(self):
        return 407

    def initHumanOptionEmote(self, param1=0, param2=0):
        self.emoteId = param1
        self.emoteStartTime = param2
        return self

    def reset(self):
        self.emoteId = 0
        self.emoteStartTime = 0

    def serialize(self, param1):
        self.serializeAs_HumanOptionEmote(param1)

    def serializeAs_HumanOptionEmote(self, param1):
        super().serializeAs_HumanOption(param1)
        if self.emoteId < 0 or self.emoteId > 255:
            raise RuntimeError("Forbidden value (" + str(self.emoteId) + ") on element emoteId.")
        param1.write_byte(self.emoteId)
        if self.emoteStartTime < -9007199254740990 or self.emoteStartTime > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.emoteStartTime) + ") on element emoteStartTime.")
        param1.write_double(self.emoteStartTime)

    def deserialize(self, param1):
        self.deserializeAs_HumanOptionEmote(param1)

    def deserializeAs_HumanOptionEmote(self, param1):
        super().deserialize(param1)
        self._emoteIdFunc(param1)
        self._emoteStartTimeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanOptionEmote(param1)

    def deserializeAsyncAs_HumanOptionEmote(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._emoteIdFunc)
        param1.add_child(self._emoteStartTimeFunc)

    def _emoteIdFunc(self, param1):
        self.emoteId = param1.read_unsigned_byte()
        if self.emoteId < 0 or self.emoteId > 255:
            raise RuntimeError("Forbidden value (" + str(self.emoteId) + ") on element of HumanOptionEmote.emoteId.")

    def _emoteStartTimeFunc(self, param1):
        self.emoteStartTime = param1.read_double()
        if self.emoteStartTime < -9007199254740990 or self.emoteStartTime > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.emoteStartTime) + ") on element of HumanOptionEmote.emoteStartTime.")


class HumanOptionFollowers(HumanOption):
    protocolId = 410

    def __init__(self):
        super().__init__()
        self.followingCharactersLook = []
        self._followingCharactersLooktree = FuncTree()

    def getTypeId(self):
        return 410

    def initHumanOptionFollowers(self, param1=[]):
        self.followingCharactersLook = param1
        return self

    def reset(self):
        self.followingCharactersLook = []

    def serialize(self, param1):
        self.serializeAs_HumanOptionFollowers(param1)

    def serializeAs_HumanOptionFollowers(self, param1):
        super().serializeAs_HumanOption(param1)
        param1.write_short(len(self.followingCharactersLook))
        _loc2_ = 0
        while _loc2_ < len(self.followingCharactersLook):
            as_parent(self.followingCharactersLook[_loc2_], IndexedEntityLook).serializeAs_IndexedEntityLook(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_HumanOptionFollowers(param1)

    def deserializeAs_HumanOptionFollowers(self, param1):
        _loc4_ = None
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = IndexedEntityLook()
            _loc4_.deserialize(param1)
            self.followingCharactersLook.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanOptionFollowers(param1)

    def deserializeAsyncAs_HumanOptionFollowers(self, param1):
        super().deserializeAsync(param1)
        self._followingCharactersLooktree = param1.add_child(self._followingCharactersLooktreeFunc)

    def _followingCharactersLooktreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._followingCharactersLooktree.add_child(self._followingCharactersLookFunc)
            _loc3_ += 1

    def _followingCharactersLookFunc(self, param1):
        _loc2_ = IndexedEntityLook()
        _loc2_.deserialize(param1)
        self.followingCharactersLook.append(_loc2_)


class HumanOptionGuild(HumanOption):
    protocolId = 409

    def __init__(self):
        super().__init__()
        self.guildInformations = GuildInformations()
        self._guildInformationstree = FuncTree()

    def getTypeId(self):
        return 409

    def initHumanOptionGuild(self, param1=None):
        self.guildInformations = param1
        return self

    def reset(self):
        self.guildInformations = GuildInformations()

    def serialize(self, param1):
        self.serializeAs_HumanOptionGuild(param1)

    def serializeAs_HumanOptionGuild(self, param1):
        super().serializeAs_HumanOption(param1)
        self.guildInformations.serializeAs_GuildInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_HumanOptionGuild(param1)

    def deserializeAs_HumanOptionGuild(self, param1):
        super().deserialize(param1)
        self.guildInformations = GuildInformations()
        self.guildInformations.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanOptionGuild(param1)

    def deserializeAsyncAs_HumanOptionGuild(self, param1):
        super().deserializeAsync(param1)
        self._guildInformationstree = param1.add_child(self._guildInformationstreeFunc)

    def _guildInformationstreeFunc(self, param1):
        self.guildInformations = GuildInformations()
        self.guildInformations.deserializeAsync(self._guildInformationstree)


class HumanOptionObjectUse(HumanOption):
    protocolId = 449

    def __init__(self):
        super().__init__()
        self.delayTypeId = 0
        self.delayEndTime = 0
        self.objectGID = 0

    def getTypeId(self):
        return 449

    def initHumanOptionObjectUse(self, param1=0, param2=0, param3=0):
        self.delayTypeId = param1
        self.delayEndTime = param2
        self.objectGID = param3
        return self

    def reset(self):
        self.delayTypeId = 0
        self.delayEndTime = 0
        self.objectGID = 0

    def serialize(self, param1):
        self.serializeAs_HumanOptionObjectUse(param1)

    def serializeAs_HumanOptionObjectUse(self, param1):
        super().serializeAs_HumanOption(param1)
        param1.write_byte(self.delayTypeId)
        if self.delayEndTime < 0 or self.delayEndTime > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.delayEndTime) + ") on element delayEndTime.")
        param1.write_double(self.delayEndTime)
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element objectGID.")
        param1.write_var_short(self.objectGID)

    def deserialize(self, param1):
        self.deserializeAs_HumanOptionObjectUse(param1)

    def deserializeAs_HumanOptionObjectUse(self, param1):
        super().deserialize(param1)
        self._delayTypeIdFunc(param1)
        self._delayEndTimeFunc(param1)
        self._objectGIDFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanOptionObjectUse(param1)

    def deserializeAsyncAs_HumanOptionObjectUse(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._delayTypeIdFunc)
        param1.add_child(self._delayEndTimeFunc)
        param1.add_child(self._objectGIDFunc)

    def _delayTypeIdFunc(self, param1):
        self.delayTypeId = param1.read_byte()
        if self.delayTypeId < 0:
            raise RuntimeError("Forbidden value (" + str(self.delayTypeId) + ") on element of HumanOptionObjectUse.delayTypeId.")

    def _delayEndTimeFunc(self, param1):
        self.delayEndTime = param1.read_double()
        if self.delayEndTime < 0 or self.delayEndTime > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.delayEndTime) + ") on element of HumanOptionObjectUse.delayEndTime.")

    def _objectGIDFunc(self, param1):
        self.objectGID = param1.read_var_uh_short()
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of HumanOptionObjectUse.objectGID.")


class HumanOptionOrnament(HumanOption):
    protocolId = 411

    def __init__(self):
        super().__init__()
        self.ornamentId = 0

    def getTypeId(self):
        return 411

    def initHumanOptionOrnament(self, param1=0):
        self.ornamentId = param1
        return self

    def reset(self):
        self.ornamentId = 0

    def serialize(self, param1):
        self.serializeAs_HumanOptionOrnament(param1)

    def serializeAs_HumanOptionOrnament(self, param1):
        super().serializeAs_HumanOption(param1)
        if self.ornamentId < 0:
            raise RuntimeError("Forbidden value (" + str(self.ornamentId) + ") on element ornamentId.")
        param1.write_var_short(self.ornamentId)

    def deserialize(self, param1):
        self.deserializeAs_HumanOptionOrnament(param1)

    def deserializeAs_HumanOptionOrnament(self, param1):
        super().deserialize(param1)
        self._ornamentIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanOptionOrnament(param1)

    def deserializeAsyncAs_HumanOptionOrnament(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._ornamentIdFunc)

    def _ornamentIdFunc(self, param1):
        self.ornamentId = param1.read_var_uh_short()
        if self.ornamentId < 0:
            raise RuntimeError("Forbidden value (" + str(self.ornamentId) + ") on element of HumanOptionOrnament.ornamentId.")


class HumanOptionSkillUse(HumanOption):
    protocolId = 495

    def __init__(self):
        super().__init__()
        self.elementId = 0
        self.skillId = 0
        self.skillEndTime = 0

    def getTypeId(self):
        return 495

    def initHumanOptionSkillUse(self, param1=0, param2=0, param3=0):
        self.elementId = param1
        self.skillId = param2
        self.skillEndTime = param3
        return self

    def reset(self):
        self.elementId = 0
        self.skillId = 0
        self.skillEndTime = 0

    def serialize(self, param1):
        self.serializeAs_HumanOptionSkillUse(param1)

    def serializeAs_HumanOptionSkillUse(self, param1):
        super().serializeAs_HumanOption(param1)
        if self.elementId < 0:
            raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element elementId.")
        param1.write_var_int(self.elementId)
        if self.skillId < 0:
            raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element skillId.")
        param1.write_var_short(self.skillId)
        if self.skillEndTime < -9007199254740990 or self.skillEndTime > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.skillEndTime) + ") on element skillEndTime.")
        param1.write_double(self.skillEndTime)

    def deserialize(self, param1):
        self.deserializeAs_HumanOptionSkillUse(param1)

    def deserializeAs_HumanOptionSkillUse(self, param1):
        super().deserialize(param1)
        self._elementIdFunc(param1)
        self._skillIdFunc(param1)
        self._skillEndTimeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanOptionSkillUse(param1)

    def deserializeAsyncAs_HumanOptionSkillUse(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._elementIdFunc)
        param1.add_child(self._skillIdFunc)
        param1.add_child(self._skillEndTimeFunc)

    def _elementIdFunc(self, param1):
        self.elementId = param1.read_var_uh_int()
        if self.elementId < 0:
            raise RuntimeError("Forbidden value (" + str(self.elementId) + ") on element of HumanOptionSkillUse.elementId.")

    def _skillIdFunc(self, param1):
        self.skillId = param1.read_var_uh_short()
        if self.skillId < 0:
            raise RuntimeError("Forbidden value (" + str(self.skillId) + ") on element of HumanOptionSkillUse.skillId.")

    def _skillEndTimeFunc(self, param1):
        self.skillEndTime = param1.read_double()
        if self.skillEndTime < -9007199254740990 or self.skillEndTime > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.skillEndTime) + ") on element of HumanOptionSkillUse.skillEndTime.")


class HumanOptionTitle(HumanOption):
    protocolId = 408

    def __init__(self):
        super().__init__()
        self.titleId = 0
        self.titleParam = ""

    def getTypeId(self):
        return 408

    def initHumanOptionTitle(self, param1=0, param2=""):
        self.titleId = param1
        self.titleParam = param2
        return self

    def reset(self):
        self.titleId = 0
        self.titleParam = ""

    def serialize(self, param1):
        self.serializeAs_HumanOptionTitle(param1)

    def serializeAs_HumanOptionTitle(self, param1):
        super().serializeAs_HumanOption(param1)
        if self.titleId < 0:
            raise RuntimeError("Forbidden value (" + str(self.titleId) + ") on element titleId.")
        param1.write_var_short(self.titleId)
        param1.write_utf(self.titleParam)

    def deserialize(self, param1):
        self.deserializeAs_HumanOptionTitle(param1)

    def deserializeAs_HumanOptionTitle(self, param1):
        super().deserialize(param1)
        self._titleIdFunc(param1)
        self._titleParamFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HumanOptionTitle(param1)

    def deserializeAsyncAs_HumanOptionTitle(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._titleIdFunc)
        param1.add_child(self._titleParamFunc)

    def _titleIdFunc(self, param1):
        self.titleId = param1.read_var_uh_short()
        if self.titleId < 0:
            raise RuntimeError("Forbidden value (" + str(self.titleId) + ") on element of HumanOptionTitle.titleId.")

    def _titleParamFunc(self, param1):
        self.titleParam = param1.read_utf()


class MonsterInGroupInformations(MonsterInGroupLightInformations):
    protocolId = 144

    def __init__(self):
        super().__init__()
        self.look = EntityLook()
        self._looktree = FuncTree()

    def getTypeId(self):
        return 144

    def initMonsterInGroupInformations(self, param1=0, param2=0, param3=None):
        super().initMonsterInGroupLightInformations(param1,param2)
        self.look = param3
        return self

    def reset(self):
        super().reset()
        self.look = EntityLook()

    def serialize(self, param1):
        self.serializeAs_MonsterInGroupInformations(param1)

    def serializeAs_MonsterInGroupInformations(self, param1):
        super().serializeAs_MonsterInGroupLightInformations(param1)
        self.look.serializeAs_EntityLook(param1)

    def deserialize(self, param1):
        self.deserializeAs_MonsterInGroupInformations(param1)

    def deserializeAs_MonsterInGroupInformations(self, param1):
        super().deserialize(param1)
        self.look = EntityLook()
        self.look.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MonsterInGroupInformations(param1)

    def deserializeAsyncAs_MonsterInGroupInformations(self, param1):
        super().deserializeAsync(param1)
        self._looktree = param1.add_child(self._looktreeFunc)

    def _looktreeFunc(self, param1):
        self.look = EntityLook()
        self.look.deserializeAsync(self._looktree)


class PartyCompanionMemberInformations(PartyCompanionBaseInformations):
    protocolId = 452

    def __init__(self):
        super().__init__()
        self.initiative = 0
        self.lifePoints = 0
        self.maxLifePoints = 0
        self.prospecting = 0
        self.regenRate = 0

    def getTypeId(self):
        return 452

    def initPartyCompanionMemberInformations(self, param1=0, param2=0, param3=None, param4=0, param5=0, param6=0, param7=0, param8=0):
        super().initPartyCompanionBaseInformations(param1,param2,param3)
        self.initiative = param4
        self.lifePoints = param5
        self.maxLifePoints = param6
        self.prospecting = param7
        self.regenRate = param8
        return self

    def reset(self):
        super().reset()
        self.initiative = 0
        self.lifePoints = 0
        self.maxLifePoints = 0
        self.prospecting = 0
        self.regenRate = 0

    def serialize(self, param1):
        self.serializeAs_PartyCompanionMemberInformations(param1)

    def serializeAs_PartyCompanionMemberInformations(self, param1):
        super().serializeAs_PartyCompanionBaseInformations(param1)
        if self.initiative < 0:
            raise RuntimeError("Forbidden value (" + str(self.initiative) + ") on element initiative.")
        param1.write_var_short(self.initiative)
        if self.lifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element lifePoints.")
        param1.write_var_int(self.lifePoints)
        if self.maxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element maxLifePoints.")
        param1.write_var_int(self.maxLifePoints)
        if self.prospecting < 0:
            raise RuntimeError("Forbidden value (" + str(self.prospecting) + ") on element prospecting.")
        param1.write_var_short(self.prospecting)
        if self.regenRate < 0 or self.regenRate > 255:
            raise RuntimeError("Forbidden value (" + str(self.regenRate) + ") on element regenRate.")
        param1.write_byte(self.regenRate)

    def deserialize(self, param1):
        self.deserializeAs_PartyCompanionMemberInformations(param1)

    def deserializeAs_PartyCompanionMemberInformations(self, param1):
        super().deserialize(param1)
        self._initiativeFunc(param1)
        self._lifePointsFunc(param1)
        self._maxLifePointsFunc(param1)
        self._prospectingFunc(param1)
        self._regenRateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PartyCompanionMemberInformations(param1)

    def deserializeAsyncAs_PartyCompanionMemberInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._initiativeFunc)
        param1.add_child(self._lifePointsFunc)
        param1.add_child(self._maxLifePointsFunc)
        param1.add_child(self._prospectingFunc)
        param1.add_child(self._regenRateFunc)

    def _initiativeFunc(self, param1):
        self.initiative = param1.read_var_uh_short()
        if self.initiative < 0:
            raise RuntimeError("Forbidden value (" + str(self.initiative) + ") on element of PartyCompanionMemberInformations.initiative.")

    def _lifePointsFunc(self, param1):
        self.lifePoints = param1.read_var_uh_int()
        if self.lifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element of PartyCompanionMemberInformations.lifePoints.")

    def _maxLifePointsFunc(self, param1):
        self.maxLifePoints = param1.read_var_uh_int()
        if self.maxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element of PartyCompanionMemberInformations.maxLifePoints.")

    def _prospectingFunc(self, param1):
        self.prospecting = param1.read_var_uh_short()
        if self.prospecting < 0:
            raise RuntimeError("Forbidden value (" + str(self.prospecting) + ") on element of PartyCompanionMemberInformations.prospecting.")

    def _regenRateFunc(self, param1):
        self.regenRate = param1.read_unsigned_byte()
        if self.regenRate < 0 or self.regenRate > 255:
            raise RuntimeError("Forbidden value (" + str(self.regenRate) + ") on element of PartyCompanionMemberInformations.regenRate.")


class QuestActiveDetailedInformations(QuestActiveInformations):
    protocolId = 382

    def __init__(self):
        super().__init__()
        self.stepId = 0
        self.objectives = []
        self._objectivestree = FuncTree()

    def getTypeId(self):
        return 382

    def initQuestActiveDetailedInformations(self, param1=0, param2=0, param3=[]):
        super().initQuestActiveInformations(param1)
        self.stepId = param2
        self.objectives = param3
        return self

    def reset(self):
        super().reset()
        self.stepId = 0
        self.objectives = []

    def serialize(self, param1):
        self.serializeAs_QuestActiveDetailedInformations(param1)

    def serializeAs_QuestActiveDetailedInformations(self, param1):
        super().serializeAs_QuestActiveInformations(param1)
        if self.stepId < 0:
            raise RuntimeError("Forbidden value (" + str(self.stepId) + ") on element stepId.")
        param1.write_var_short(self.stepId)
        param1.write_short(len(self.objectives))
        _loc2_ = 0
        while _loc2_ < len(self.objectives):
            param1.write_short(as_parent(self.objectives[_loc2_], QuestObjectiveInformations).getTypeId())
            as_parent(self.objectives[_loc2_], QuestObjectiveInformations).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_QuestActiveDetailedInformations(param1)

    def deserializeAs_QuestActiveDetailedInformations(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._stepIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(QuestObjectiveInformations,_loc4_)
            _loc5_.deserialize(param1)
            self.objectives.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_QuestActiveDetailedInformations(param1)

    def deserializeAsyncAs_QuestActiveDetailedInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._stepIdFunc)
        self._objectivestree = param1.add_child(self._objectivestreeFunc)

    def _stepIdFunc(self, param1):
        self.stepId = param1.read_var_uh_short()
        if self.stepId < 0:
            raise RuntimeError("Forbidden value (" + str(self.stepId) + ") on element of QuestActiveDetailedInformations.stepId.")

    def _objectivestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._objectivestree.add_child(self._objectivesFunc)
            _loc3_ += 1

    def _objectivesFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(QuestObjectiveInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.objectives.append(_loc3_)


class QuestObjectiveInformationsWithCompletion(QuestObjectiveInformations):
    protocolId = 386

    def __init__(self):
        super().__init__()
        self.curCompletion = 0
        self.maxCompletion = 0

    def getTypeId(self):
        return 386

    def initQuestObjectiveInformationsWithCompletion(self, param1=0, param2=False, param3=[], param4=0, param5=0):
        super().initQuestObjectiveInformations(param1,param2,param3)
        self.curCompletion = param4
        self.maxCompletion = param5
        return self

    def reset(self):
        super().reset()
        self.curCompletion = 0
        self.maxCompletion = 0

    def serialize(self, param1):
        self.serializeAs_QuestObjectiveInformationsWithCompletion(param1)

    def serializeAs_QuestObjectiveInformationsWithCompletion(self, param1):
        super().serializeAs_QuestObjectiveInformations(param1)
        if self.curCompletion < 0:
            raise RuntimeError("Forbidden value (" + str(self.curCompletion) + ") on element curCompletion.")
        param1.write_var_short(self.curCompletion)
        if self.maxCompletion < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxCompletion) + ") on element maxCompletion.")
        param1.write_var_short(self.maxCompletion)

    def deserialize(self, param1):
        self.deserializeAs_QuestObjectiveInformationsWithCompletion(param1)

    def deserializeAs_QuestObjectiveInformationsWithCompletion(self, param1):
        super().deserialize(param1)
        self._curCompletionFunc(param1)
        self._maxCompletionFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_QuestObjectiveInformationsWithCompletion(param1)

    def deserializeAsyncAs_QuestObjectiveInformationsWithCompletion(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._curCompletionFunc)
        param1.add_child(self._maxCompletionFunc)

    def _curCompletionFunc(self, param1):
        self.curCompletion = param1.read_var_uh_short()
        if self.curCompletion < 0:
            raise RuntimeError("Forbidden value (" + str(self.curCompletion) + ") on element of QuestObjectiveInformationsWithCompletion.curCompletion.")

    def _maxCompletionFunc(self, param1):
        self.maxCompletion = param1.read_var_uh_short()
        if self.maxCompletion < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxCompletion) + ") on element of QuestObjectiveInformationsWithCompletion.maxCompletion.")


class TreasureHuntStepDig(TreasureHuntStep):
    protocolId = 465

    def getTypeId(self):
        return 465

    def initTreasureHuntStepDig(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_TreasureHuntStepDig(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_TreasureHuntStepDig(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_TreasureHuntStepDig(self, param1):
        pass


class TreasureHuntStepFight(TreasureHuntStep):
    protocolId = 462

    def getTypeId(self):
        return 462

    def initTreasureHuntStepFight(self):
        return self

    def reset(self):
        pass

    def serialize(self, param1):
        pass

    def serializeAs_TreasureHuntStepFight(self, param1):
        pass

    def deserialize(self, param1):
        pass

    def deserializeAs_TreasureHuntStepFight(self, param1):
        pass

    def deserializeAsync(self, param1):
        pass

    def deserializeAsyncAs_TreasureHuntStepFight(self, param1):
        pass


class TreasureHuntStepFollowDirection(TreasureHuntStep):
    protocolId = 468

    def __init__(self):
        super().__init__()
        self.direction = 1
        self.mapCount = 0

    def getTypeId(self):
        return 468

    def initTreasureHuntStepFollowDirection(self, param1=1, param2=0):
        self.direction = param1
        self.mapCount = param2
        return self

    def reset(self):
        self.direction = 1
        self.mapCount = 0

    def serialize(self, param1):
        self.serializeAs_TreasureHuntStepFollowDirection(param1)

    def serializeAs_TreasureHuntStepFollowDirection(self, param1):
        super().serializeAs_TreasureHuntStep(param1)
        param1.write_byte(self.direction)
        if self.mapCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.mapCount) + ") on element mapCount.")
        param1.write_var_short(self.mapCount)

    def deserialize(self, param1):
        self.deserializeAs_TreasureHuntStepFollowDirection(param1)

    def deserializeAs_TreasureHuntStepFollowDirection(self, param1):
        super().deserialize(param1)
        self._directionFunc(param1)
        self._mapCountFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TreasureHuntStepFollowDirection(param1)

    def deserializeAsyncAs_TreasureHuntStepFollowDirection(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._directionFunc)
        param1.add_child(self._mapCountFunc)

    def _directionFunc(self, param1):
        self.direction = param1.read_byte()
        if self.direction < 0:
            raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of TreasureHuntStepFollowDirection.direction.")

    def _mapCountFunc(self, param1):
        self.mapCount = param1.read_var_uh_short()
        if self.mapCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.mapCount) + ") on element of TreasureHuntStepFollowDirection.mapCount.")


class TreasureHuntStepFollowDirectionToHint(TreasureHuntStep):
    protocolId = 472

    def __init__(self):
        super().__init__()
        self.direction = 1
        self.npcId = 0

    def getTypeId(self):
        return 472

    def initTreasureHuntStepFollowDirectionToHint(self, param1=1, param2=0):
        self.direction = param1
        self.npcId = param2
        return self

    def reset(self):
        self.direction = 1
        self.npcId = 0

    def serialize(self, param1):
        self.serializeAs_TreasureHuntStepFollowDirectionToHint(param1)

    def serializeAs_TreasureHuntStepFollowDirectionToHint(self, param1):
        super().serializeAs_TreasureHuntStep(param1)
        param1.write_byte(self.direction)
        if self.npcId < 0:
            raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element npcId.")
        param1.write_var_short(self.npcId)

    def deserialize(self, param1):
        self.deserializeAs_TreasureHuntStepFollowDirectionToHint(param1)

    def deserializeAs_TreasureHuntStepFollowDirectionToHint(self, param1):
        super().deserialize(param1)
        self._directionFunc(param1)
        self._npcIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TreasureHuntStepFollowDirectionToHint(param1)

    def deserializeAsyncAs_TreasureHuntStepFollowDirectionToHint(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._directionFunc)
        param1.add_child(self._npcIdFunc)

    def _directionFunc(self, param1):
        self.direction = param1.read_byte()
        if self.direction < 0:
            raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of TreasureHuntStepFollowDirectionToHint.direction.")

    def _npcIdFunc(self, param1):
        self.npcId = param1.read_var_uh_short()
        if self.npcId < 0:
            raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element of TreasureHuntStepFollowDirectionToHint.npcId.")


class TreasureHuntStepFollowDirectionToPOI(TreasureHuntStep):
    protocolId = 461

    def __init__(self):
        super().__init__()
        self.direction = 1
        self.poiLabelId = 0

    def getTypeId(self):
        return 461

    def initTreasureHuntStepFollowDirectionToPOI(self, param1=1, param2=0):
        self.direction = param1
        self.poiLabelId = param2
        return self

    def reset(self):
        self.direction = 1
        self.poiLabelId = 0

    def serialize(self, param1):
        self.serializeAs_TreasureHuntStepFollowDirectionToPOI(param1)

    def serializeAs_TreasureHuntStepFollowDirectionToPOI(self, param1):
        super().serializeAs_TreasureHuntStep(param1)
        param1.write_byte(self.direction)
        if self.poiLabelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.poiLabelId) + ") on element poiLabelId.")
        param1.write_var_short(self.poiLabelId)

    def deserialize(self, param1):
        self.deserializeAs_TreasureHuntStepFollowDirectionToPOI(param1)

    def deserializeAs_TreasureHuntStepFollowDirectionToPOI(self, param1):
        super().deserialize(param1)
        self._directionFunc(param1)
        self._poiLabelIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TreasureHuntStepFollowDirectionToPOI(param1)

    def deserializeAsyncAs_TreasureHuntStepFollowDirectionToPOI(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._directionFunc)
        param1.add_child(self._poiLabelIdFunc)

    def _directionFunc(self, param1):
        self.direction = param1.read_byte()
        if self.direction < 0:
            raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of TreasureHuntStepFollowDirectionToPOI.direction.")

    def _poiLabelIdFunc(self, param1):
        self.poiLabelId = param1.read_var_uh_short()
        if self.poiLabelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.poiLabelId) + ") on element of TreasureHuntStepFollowDirectionToPOI.poiLabelId.")


class GoldItem(Item):
    protocolId = 123

    def __init__(self):
        super().__init__()
        self.sum = 0

    def getTypeId(self):
        return 123

    def initGoldItem(self, param1=0):
        self.sum = param1
        return self

    def reset(self):
        self.sum = 0

    def serialize(self, param1):
        self.serializeAs_GoldItem(param1)

    def serializeAs_GoldItem(self, param1):
        super().serializeAs_Item(param1)
        if self.sum < 0 or self.sum > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.sum) + ") on element sum.")
        param1.write_var_long(self.sum)

    def deserialize(self, param1):
        self.deserializeAs_GoldItem(param1)

    def deserializeAs_GoldItem(self, param1):
        super().deserialize(param1)
        self._sumFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GoldItem(param1)

    def deserializeAsyncAs_GoldItem(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._sumFunc)

    def _sumFunc(self, param1):
        self.sum = param1.read_var_uh_long()
        if self.sum < 0 or self.sum > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.sum) + ") on element of GoldItem.sum.")


class ObjectItem(Item):
    protocolId = 37

    def __init__(self):
        super().__init__()
        self.position = 63
        self.objectGID = 0
        self.effects = []
        self.objectUID = 0
        self.quantity = 0
        self._effectstree = FuncTree()

    def getTypeId(self):
        return 37

    def initObjectItem(self, param1=63, param2=0, param3=[], param4=0, param5=0):
        self.position = param1
        self.objectGID = param2
        self.effects = param3
        self.objectUID = param4
        self.quantity = param5
        return self

    def reset(self):
        self.position = 63
        self.objectGID = 0
        self.effects = []
        self.objectUID = 0
        self.quantity = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItem(param1)

    def serializeAs_ObjectItem(self, param1):
        super().serializeAs_Item(param1)
        param1.write_byte(self.position)
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element objectGID.")
        param1.write_var_short(self.objectGID)
        param1.write_short(len(self.effects))
        _loc2_ = 0
        while _loc2_ < len(self.effects):
            param1.write_short(as_parent(self.effects[_loc2_], ObjectEffect).getTypeId())
            as_parent(self.effects[_loc2_], ObjectEffect).serialize(param1)
            _loc2_ += 1
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element objectUID.")
        param1.write_var_int(self.objectUID)
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element quantity.")
        param1.write_var_int(self.quantity)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItem(param1)

    def deserializeAs_ObjectItem(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._positionFunc(param1)
        self._objectGIDFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc4_)
            _loc5_.deserialize(param1)
            self.effects.append(_loc5_)
            _loc3_ += 1
        self._objectUIDFunc(param1)
        self._quantityFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItem(param1)

    def deserializeAsyncAs_ObjectItem(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._positionFunc)
        param1.add_child(self._objectGIDFunc)
        self._effectstree = param1.add_child(self._effectstreeFunc)
        param1.add_child(self._objectUIDFunc)
        param1.add_child(self._quantityFunc)

    def _positionFunc(self, param1):
        self.position = param1.read_unsigned_byte()
        if self.position < 0 or self.position > 255:
            raise RuntimeError("Forbidden value (" + str(self.position) + ") on element of ObjectItem.position.")

    def _objectGIDFunc(self, param1):
        self.objectGID = param1.read_var_uh_short()
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItem.objectGID.")

    def _effectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._effectstree.add_child(self._effectsFunc)
            _loc3_ += 1

    def _effectsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc2_)
        _loc3_.deserialize(param1)
        self.effects.append(_loc3_)

    def _objectUIDFunc(self, param1):
        self.objectUID = param1.read_var_uh_int()
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectItem.objectUID.")

    def _quantityFunc(self, param1):
        self.quantity = param1.read_var_uh_int()
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItem.quantity.")


class ObjectItemGenericQuantity(Item):
    protocolId = 483

    def __init__(self):
        super().__init__()
        self.objectGID = 0
        self.quantity = 0

    def getTypeId(self):
        return 483

    def initObjectItemGenericQuantity(self, param1=0, param2=0):
        self.objectGID = param1
        self.quantity = param2
        return self

    def reset(self):
        self.objectGID = 0
        self.quantity = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemGenericQuantity(param1)

    def serializeAs_ObjectItemGenericQuantity(self, param1):
        super().serializeAs_Item(param1)
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element objectGID.")
        param1.write_var_short(self.objectGID)
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element quantity.")
        param1.write_var_int(self.quantity)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemGenericQuantity(param1)

    def deserializeAs_ObjectItemGenericQuantity(self, param1):
        super().deserialize(param1)
        self._objectGIDFunc(param1)
        self._quantityFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemGenericQuantity(param1)

    def deserializeAsyncAs_ObjectItemGenericQuantity(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._objectGIDFunc)
        param1.add_child(self._quantityFunc)

    def _objectGIDFunc(self, param1):
        self.objectGID = param1.read_var_uh_short()
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItemGenericQuantity.objectGID.")

    def _quantityFunc(self, param1):
        self.quantity = param1.read_var_uh_int()
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItemGenericQuantity.quantity.")


class ObjectItemMinimalInformation(Item):
    protocolId = 124

    def __init__(self):
        super().__init__()
        self.objectGID = 0
        self.effects = []
        self._effectstree = FuncTree()

    def getTypeId(self):
        return 124

    def initObjectItemMinimalInformation(self, param1=0, param2=[]):
        self.objectGID = param1
        self.effects = param2
        return self

    def reset(self):
        self.objectGID = 0
        self.effects = []

    def serialize(self, param1):
        self.serializeAs_ObjectItemMinimalInformation(param1)

    def serializeAs_ObjectItemMinimalInformation(self, param1):
        super().serializeAs_Item(param1)
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element objectGID.")
        param1.write_var_short(self.objectGID)
        param1.write_short(len(self.effects))
        _loc2_ = 0
        while _loc2_ < len(self.effects):
            param1.write_short(as_parent(self.effects[_loc2_], ObjectEffect).getTypeId())
            as_parent(self.effects[_loc2_], ObjectEffect).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemMinimalInformation(param1)

    def deserializeAs_ObjectItemMinimalInformation(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._objectGIDFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc4_)
            _loc5_.deserialize(param1)
            self.effects.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemMinimalInformation(param1)

    def deserializeAsyncAs_ObjectItemMinimalInformation(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._objectGIDFunc)
        self._effectstree = param1.add_child(self._effectstreeFunc)

    def _objectGIDFunc(self, param1):
        self.objectGID = param1.read_var_uh_short()
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItemMinimalInformation.objectGID.")

    def _effectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._effectstree.add_child(self._effectsFunc)
            _loc3_ += 1

    def _effectsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc2_)
        _loc3_.deserialize(param1)
        self.effects.append(_loc3_)


class ObjectItemNotInContainer(Item):
    protocolId = 134

    def __init__(self):
        super().__init__()
        self.objectGID = 0
        self.effects = []
        self.objectUID = 0
        self.quantity = 0
        self._effectstree = FuncTree()

    def getTypeId(self):
        return 134

    def initObjectItemNotInContainer(self, param1=0, param2=[], param3=0, param4=0):
        self.objectGID = param1
        self.effects = param2
        self.objectUID = param3
        self.quantity = param4
        return self

    def reset(self):
        self.objectGID = 0
        self.effects = []
        self.objectUID = 0
        self.quantity = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemNotInContainer(param1)

    def serializeAs_ObjectItemNotInContainer(self, param1):
        super().serializeAs_Item(param1)
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element objectGID.")
        param1.write_var_short(self.objectGID)
        param1.write_short(len(self.effects))
        _loc2_ = 0
        while _loc2_ < len(self.effects):
            param1.write_short(as_parent(self.effects[_loc2_], ObjectEffect).getTypeId())
            as_parent(self.effects[_loc2_], ObjectEffect).serialize(param1)
            _loc2_ += 1
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element objectUID.")
        param1.write_var_int(self.objectUID)
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element quantity.")
        param1.write_var_int(self.quantity)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemNotInContainer(param1)

    def deserializeAs_ObjectItemNotInContainer(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._objectGIDFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc4_)
            _loc5_.deserialize(param1)
            self.effects.append(_loc5_)
            _loc3_ += 1
        self._objectUIDFunc(param1)
        self._quantityFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemNotInContainer(param1)

    def deserializeAsyncAs_ObjectItemNotInContainer(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._objectGIDFunc)
        self._effectstree = param1.add_child(self._effectstreeFunc)
        param1.add_child(self._objectUIDFunc)
        param1.add_child(self._quantityFunc)

    def _objectGIDFunc(self, param1):
        self.objectGID = param1.read_var_uh_short()
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItemNotInContainer.objectGID.")

    def _effectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._effectstree.add_child(self._effectsFunc)
            _loc3_ += 1

    def _effectsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc2_)
        _loc3_.deserialize(param1)
        self.effects.append(_loc3_)

    def _objectUIDFunc(self, param1):
        self.objectUID = param1.read_var_uh_int()
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectItemNotInContainer.objectUID.")

    def _quantityFunc(self, param1):
        self.quantity = param1.read_var_uh_int()
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItemNotInContainer.quantity.")


class ObjectItemQuantity(Item):
    protocolId = 119

    def __init__(self):
        super().__init__()
        self.objectUID = 0
        self.quantity = 0

    def getTypeId(self):
        return 119

    def initObjectItemQuantity(self, param1=0, param2=0):
        self.objectUID = param1
        self.quantity = param2
        return self

    def reset(self):
        self.objectUID = 0
        self.quantity = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemQuantity(param1)

    def serializeAs_ObjectItemQuantity(self, param1):
        super().serializeAs_Item(param1)
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element objectUID.")
        param1.write_var_int(self.objectUID)
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element quantity.")
        param1.write_var_int(self.quantity)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemQuantity(param1)

    def deserializeAs_ObjectItemQuantity(self, param1):
        super().deserialize(param1)
        self._objectUIDFunc(param1)
        self._quantityFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemQuantity(param1)

    def deserializeAsyncAs_ObjectItemQuantity(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._objectUIDFunc)
        param1.add_child(self._quantityFunc)

    def _objectUIDFunc(self, param1):
        self.objectUID = param1.read_var_uh_int()
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectItemQuantity.objectUID.")

    def _quantityFunc(self, param1):
        self.quantity = param1.read_var_uh_int()
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItemQuantity.quantity.")


class ObjectItemToSell(Item):
    protocolId = 120

    def __init__(self):
        super().__init__()
        self.objectGID = 0
        self.effects = []
        self.objectUID = 0
        self.quantity = 0
        self.objectPrice = 0
        self._effectstree = FuncTree()

    def getTypeId(self):
        return 120

    def initObjectItemToSell(self, param1=0, param2=[], param3=0, param4=0, param5=0):
        self.objectGID = param1
        self.effects = param2
        self.objectUID = param3
        self.quantity = param4
        self.objectPrice = param5
        return self

    def reset(self):
        self.objectGID = 0
        self.effects = []
        self.objectUID = 0
        self.quantity = 0
        self.objectPrice = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemToSell(param1)

    def serializeAs_ObjectItemToSell(self, param1):
        super().serializeAs_Item(param1)
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element objectGID.")
        param1.write_var_short(self.objectGID)
        param1.write_short(len(self.effects))
        _loc2_ = 0
        while _loc2_ < len(self.effects):
            param1.write_short(as_parent(self.effects[_loc2_], ObjectEffect).getTypeId())
            as_parent(self.effects[_loc2_], ObjectEffect).serialize(param1)
            _loc2_ += 1
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element objectUID.")
        param1.write_var_int(self.objectUID)
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element quantity.")
        param1.write_var_int(self.quantity)
        if self.objectPrice < 0 or self.objectPrice > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.objectPrice) + ") on element objectPrice.")
        param1.write_var_long(self.objectPrice)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemToSell(param1)

    def deserializeAs_ObjectItemToSell(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._objectGIDFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc4_)
            _loc5_.deserialize(param1)
            self.effects.append(_loc5_)
            _loc3_ += 1
        self._objectUIDFunc(param1)
        self._quantityFunc(param1)
        self._objectPriceFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemToSell(param1)

    def deserializeAsyncAs_ObjectItemToSell(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._objectGIDFunc)
        self._effectstree = param1.add_child(self._effectstreeFunc)
        param1.add_child(self._objectUIDFunc)
        param1.add_child(self._quantityFunc)
        param1.add_child(self._objectPriceFunc)

    def _objectGIDFunc(self, param1):
        self.objectGID = param1.read_var_uh_short()
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItemToSell.objectGID.")

    def _effectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._effectstree.add_child(self._effectsFunc)
            _loc3_ += 1

    def _effectsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc2_)
        _loc3_.deserialize(param1)
        self.effects.append(_loc3_)

    def _objectUIDFunc(self, param1):
        self.objectUID = param1.read_var_uh_int()
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectItemToSell.objectUID.")

    def _quantityFunc(self, param1):
        self.quantity = param1.read_var_uh_int()
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItemToSell.quantity.")

    def _objectPriceFunc(self, param1):
        self.objectPrice = param1.read_var_uh_long()
        if self.objectPrice < 0 or self.objectPrice > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.objectPrice) + ") on element of ObjectItemToSell.objectPrice.")


class ObjectItemToSellInHumanVendorShop(Item):
    protocolId = 359

    def __init__(self):
        super().__init__()
        self.objectGID = 0
        self.effects = []
        self.objectUID = 0
        self.quantity = 0
        self.objectPrice = 0
        self.publicPrice = 0
        self._effectstree = FuncTree()

    def getTypeId(self):
        return 359

    def initObjectItemToSellInHumanVendorShop(self, param1=0, param2=[], param3=0, param4=0, param5=0, param6=0):
        self.objectGID = param1
        self.effects = param2
        self.objectUID = param3
        self.quantity = param4
        self.objectPrice = param5
        self.publicPrice = param6
        return self

    def reset(self):
        self.objectGID = 0
        self.effects = []
        self.objectUID = 0
        self.quantity = 0
        self.objectPrice = 0
        self.publicPrice = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemToSellInHumanVendorShop(param1)

    def serializeAs_ObjectItemToSellInHumanVendorShop(self, param1):
        super().serializeAs_Item(param1)
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element objectGID.")
        param1.write_var_short(self.objectGID)
        param1.write_short(len(self.effects))
        _loc2_ = 0
        while _loc2_ < len(self.effects):
            param1.write_short(as_parent(self.effects[_loc2_], ObjectEffect).getTypeId())
            as_parent(self.effects[_loc2_], ObjectEffect).serialize(param1)
            _loc2_ += 1
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element objectUID.")
        param1.write_var_int(self.objectUID)
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element quantity.")
        param1.write_var_int(self.quantity)
        if self.objectPrice < 0 or self.objectPrice > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.objectPrice) + ") on element objectPrice.")
        param1.write_var_long(self.objectPrice)
        if self.publicPrice < 0 or self.publicPrice > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.publicPrice) + ") on element publicPrice.")
        param1.write_var_long(self.publicPrice)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemToSellInHumanVendorShop(param1)

    def deserializeAs_ObjectItemToSellInHumanVendorShop(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._objectGIDFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc4_)
            _loc5_.deserialize(param1)
            self.effects.append(_loc5_)
            _loc3_ += 1
        self._objectUIDFunc(param1)
        self._quantityFunc(param1)
        self._objectPriceFunc(param1)
        self._publicPriceFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemToSellInHumanVendorShop(param1)

    def deserializeAsyncAs_ObjectItemToSellInHumanVendorShop(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._objectGIDFunc)
        self._effectstree = param1.add_child(self._effectstreeFunc)
        param1.add_child(self._objectUIDFunc)
        param1.add_child(self._quantityFunc)
        param1.add_child(self._objectPriceFunc)
        param1.add_child(self._publicPriceFunc)

    def _objectGIDFunc(self, param1):
        self.objectGID = param1.read_var_uh_short()
        if self.objectGID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ObjectItemToSellInHumanVendorShop.objectGID.")

    def _effectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._effectstree.add_child(self._effectsFunc)
            _loc3_ += 1

    def _effectsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(ObjectEffect,_loc2_)
        _loc3_.deserialize(param1)
        self.effects.append(_loc3_)

    def _objectUIDFunc(self, param1):
        self.objectUID = param1.read_var_uh_int()
        if self.objectUID < 0:
            raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectItemToSellInHumanVendorShop.objectUID.")

    def _quantityFunc(self, param1):
        self.quantity = param1.read_var_uh_int()
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItemToSellInHumanVendorShop.quantity.")

    def _objectPriceFunc(self, param1):
        self.objectPrice = param1.read_var_uh_long()
        if self.objectPrice < 0 or self.objectPrice > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.objectPrice) + ") on element of ObjectItemToSellInHumanVendorShop.objectPrice.")

    def _publicPriceFunc(self, param1):
        self.publicPrice = param1.read_var_uh_long()
        if self.publicPrice < 0 or self.publicPrice > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.publicPrice) + ") on element of ObjectItemToSellInHumanVendorShop.publicPrice.")


class SpellItem(Item):
    protocolId = 49

    def __init__(self):
        super().__init__()
        self.spellId = 0
        self.spellLevel = 0

    def getTypeId(self):
        return 49

    def initSpellItem(self, param1=0, param2=0):
        self.spellId = param1
        self.spellLevel = param2
        return self

    def reset(self):
        self.spellId = 0
        self.spellLevel = 0

    def serialize(self, param1):
        self.serializeAs_SpellItem(param1)

    def serializeAs_SpellItem(self, param1):
        super().serializeAs_Item(param1)
        param1.write_int(self.spellId)
        if self.spellLevel < 1 or self.spellLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.spellLevel) + ") on element spellLevel.")
        param1.write_short(self.spellLevel)

    def deserialize(self, param1):
        self.deserializeAs_SpellItem(param1)

    def deserializeAs_SpellItem(self, param1):
        super().deserialize(param1)
        self._spellIdFunc(param1)
        self._spellLevelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_SpellItem(param1)

    def deserializeAsyncAs_SpellItem(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._spellIdFunc)
        param1.add_child(self._spellLevelFunc)

    def _spellIdFunc(self, param1):
        self.spellId = param1.read_int()

    def _spellLevelFunc(self, param1):
        self.spellLevel = param1.read_short()
        if self.spellLevel < 1 or self.spellLevel > 200:
            raise RuntimeError("Forbidden value (" + str(self.spellLevel) + ") on element of SpellItem.spellLevel.")


class ObjectEffectCreature(ObjectEffect):
    protocolId = 71

    def __init__(self):
        super().__init__()
        self.monsterFamilyId = 0

    def getTypeId(self):
        return 71

    def initObjectEffectCreature(self, param1=0, param2=0):
        super().initObjectEffect(param1)
        self.monsterFamilyId = param2
        return self

    def reset(self):
        super().reset()
        self.monsterFamilyId = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffectCreature(param1)

    def serializeAs_ObjectEffectCreature(self, param1):
        super().serializeAs_ObjectEffect(param1)
        if self.monsterFamilyId < 0:
            raise RuntimeError("Forbidden value (" + str(self.monsterFamilyId) + ") on element monsterFamilyId.")
        param1.write_var_short(self.monsterFamilyId)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectCreature(param1)

    def deserializeAs_ObjectEffectCreature(self, param1):
        super().deserialize(param1)
        self._monsterFamilyIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectCreature(param1)

    def deserializeAsyncAs_ObjectEffectCreature(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._monsterFamilyIdFunc)

    def _monsterFamilyIdFunc(self, param1):
        self.monsterFamilyId = param1.read_var_uh_short()
        if self.monsterFamilyId < 0:
            raise RuntimeError("Forbidden value (" + str(self.monsterFamilyId) + ") on element of ObjectEffectCreature.monsterFamilyId.")


class ObjectEffectDate(ObjectEffect):
    protocolId = 72

    def __init__(self):
        super().__init__()
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0

    def getTypeId(self):
        return 72

    def initObjectEffectDate(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0):
        super().initObjectEffect(param1)
        self.year = param2
        self.month = param3
        self.day = param4
        self.hour = param5
        self.minute = param6
        return self

    def reset(self):
        super().reset()
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffectDate(param1)

    def serializeAs_ObjectEffectDate(self, param1):
        super().serializeAs_ObjectEffect(param1)
        if self.year < 0:
            raise RuntimeError("Forbidden value (" + str(self.year) + ") on element year.")
        param1.write_var_short(self.year)
        if self.month < 0:
            raise RuntimeError("Forbidden value (" + str(self.month) + ") on element month.")
        param1.write_byte(self.month)
        if self.day < 0:
            raise RuntimeError("Forbidden value (" + str(self.day) + ") on element day.")
        param1.write_byte(self.day)
        if self.hour < 0:
            raise RuntimeError("Forbidden value (" + str(self.hour) + ") on element hour.")
        param1.write_byte(self.hour)
        if self.minute < 0:
            raise RuntimeError("Forbidden value (" + str(self.minute) + ") on element minute.")
        param1.write_byte(self.minute)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectDate(param1)

    def deserializeAs_ObjectEffectDate(self, param1):
        super().deserialize(param1)
        self._yearFunc(param1)
        self._monthFunc(param1)
        self._dayFunc(param1)
        self._hourFunc(param1)
        self._minuteFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectDate(param1)

    def deserializeAsyncAs_ObjectEffectDate(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._yearFunc)
        param1.add_child(self._monthFunc)
        param1.add_child(self._dayFunc)
        param1.add_child(self._hourFunc)
        param1.add_child(self._minuteFunc)

    def _yearFunc(self, param1):
        self.year = param1.read_var_uh_short()
        if self.year < 0:
            raise RuntimeError("Forbidden value (" + str(self.year) + ") on element of ObjectEffectDate.year.")

    def _monthFunc(self, param1):
        self.month = param1.read_byte()
        if self.month < 0:
            raise RuntimeError("Forbidden value (" + str(self.month) + ") on element of ObjectEffectDate.month.")

    def _dayFunc(self, param1):
        self.day = param1.read_byte()
        if self.day < 0:
            raise RuntimeError("Forbidden value (" + str(self.day) + ") on element of ObjectEffectDate.day.")

    def _hourFunc(self, param1):
        self.hour = param1.read_byte()
        if self.hour < 0:
            raise RuntimeError("Forbidden value (" + str(self.hour) + ") on element of ObjectEffectDate.hour.")

    def _minuteFunc(self, param1):
        self.minute = param1.read_byte()
        if self.minute < 0:
            raise RuntimeError("Forbidden value (" + str(self.minute) + ") on element of ObjectEffectDate.minute.")


class ObjectEffectDice(ObjectEffect):
    protocolId = 73

    def __init__(self):
        super().__init__()
        self.diceNum = 0
        self.diceSide = 0
        self.diceConst = 0

    def getTypeId(self):
        return 73

    def initObjectEffectDice(self, param1=0, param2=0, param3=0, param4=0):
        super().initObjectEffect(param1)
        self.diceNum = param2
        self.diceSide = param3
        self.diceConst = param4
        return self

    def reset(self):
        super().reset()
        self.diceNum = 0
        self.diceSide = 0
        self.diceConst = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffectDice(param1)

    def serializeAs_ObjectEffectDice(self, param1):
        super().serializeAs_ObjectEffect(param1)
        if self.diceNum < 0:
            raise RuntimeError("Forbidden value (" + str(self.diceNum) + ") on element diceNum.")
        param1.write_var_short(self.diceNum)
        if self.diceSide < 0:
            raise RuntimeError("Forbidden value (" + str(self.diceSide) + ") on element diceSide.")
        param1.write_var_short(self.diceSide)
        if self.diceConst < 0:
            raise RuntimeError("Forbidden value (" + str(self.diceConst) + ") on element diceConst.")
        param1.write_var_short(self.diceConst)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectDice(param1)

    def deserializeAs_ObjectEffectDice(self, param1):
        super().deserialize(param1)
        self._diceNumFunc(param1)
        self._diceSideFunc(param1)
        self._diceConstFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectDice(param1)

    def deserializeAsyncAs_ObjectEffectDice(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._diceNumFunc)
        param1.add_child(self._diceSideFunc)
        param1.add_child(self._diceConstFunc)

    def _diceNumFunc(self, param1):
        self.diceNum = param1.read_var_uh_short()
        if self.diceNum < 0:
            raise RuntimeError("Forbidden value (" + str(self.diceNum) + ") on element of ObjectEffectDice.diceNum.")

    def _diceSideFunc(self, param1):
        self.diceSide = param1.read_var_uh_short()
        if self.diceSide < 0:
            raise RuntimeError("Forbidden value (" + str(self.diceSide) + ") on element of ObjectEffectDice.diceSide.")

    def _diceConstFunc(self, param1):
        self.diceConst = param1.read_var_uh_short()
        if self.diceConst < 0:
            raise RuntimeError("Forbidden value (" + str(self.diceConst) + ") on element of ObjectEffectDice.diceConst.")


class ObjectEffectDuration(ObjectEffect):
    protocolId = 75

    def __init__(self):
        super().__init__()
        self.days = 0
        self.hours = 0
        self.minutes = 0

    def getTypeId(self):
        return 75

    def initObjectEffectDuration(self, param1=0, param2=0, param3=0, param4=0):
        super().initObjectEffect(param1)
        self.days = param2
        self.hours = param3
        self.minutes = param4
        return self

    def reset(self):
        super().reset()
        self.days = 0
        self.hours = 0
        self.minutes = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffectDuration(param1)

    def serializeAs_ObjectEffectDuration(self, param1):
        super().serializeAs_ObjectEffect(param1)
        if self.days < 0:
            raise RuntimeError("Forbidden value (" + str(self.days) + ") on element days.")
        param1.write_var_short(self.days)
        if self.hours < 0:
            raise RuntimeError("Forbidden value (" + str(self.hours) + ") on element hours.")
        param1.write_byte(self.hours)
        if self.minutes < 0:
            raise RuntimeError("Forbidden value (" + str(self.minutes) + ") on element minutes.")
        param1.write_byte(self.minutes)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectDuration(param1)

    def deserializeAs_ObjectEffectDuration(self, param1):
        super().deserialize(param1)
        self._daysFunc(param1)
        self._hoursFunc(param1)
        self._minutesFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectDuration(param1)

    def deserializeAsyncAs_ObjectEffectDuration(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._daysFunc)
        param1.add_child(self._hoursFunc)
        param1.add_child(self._minutesFunc)

    def _daysFunc(self, param1):
        self.days = param1.read_var_uh_short()
        if self.days < 0:
            raise RuntimeError("Forbidden value (" + str(self.days) + ") on element of ObjectEffectDuration.days.")

    def _hoursFunc(self, param1):
        self.hours = param1.read_byte()
        if self.hours < 0:
            raise RuntimeError("Forbidden value (" + str(self.hours) + ") on element of ObjectEffectDuration.hours.")

    def _minutesFunc(self, param1):
        self.minutes = param1.read_byte()
        if self.minutes < 0:
            raise RuntimeError("Forbidden value (" + str(self.minutes) + ") on element of ObjectEffectDuration.minutes.")


class ObjectEffectInteger(ObjectEffect):
    protocolId = 70

    def __init__(self):
        super().__init__()
        self.value = 0

    def getTypeId(self):
        return 70

    def initObjectEffectInteger(self, param1=0, param2=0):
        super().initObjectEffect(param1)
        self.value = param2
        return self

    def reset(self):
        super().reset()
        self.value = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffectInteger(param1)

    def serializeAs_ObjectEffectInteger(self, param1):
        super().serializeAs_ObjectEffect(param1)
        if self.value < 0:
            raise RuntimeError("Forbidden value (" + str(self.value) + ") on element value.")
        param1.write_var_int(self.value)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectInteger(param1)

    def deserializeAs_ObjectEffectInteger(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectInteger(param1)

    def deserializeAsyncAs_ObjectEffectInteger(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_var_uh_int()
        if self.value < 0:
            raise RuntimeError("Forbidden value (" + str(self.value) + ") on element of ObjectEffectInteger.value.")


class ObjectEffectMinMax(ObjectEffect):
    protocolId = 82

    def __init__(self):
        super().__init__()
        self.min = 0
        self.max = 0

    def getTypeId(self):
        return 82

    def initObjectEffectMinMax(self, param1=0, param2=0, param3=0):
        super().initObjectEffect(param1)
        self.min = param2
        self.max = param3
        return self

    def reset(self):
        super().reset()
        self.min = 0
        self.max = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffectMinMax(param1)

    def serializeAs_ObjectEffectMinMax(self, param1):
        super().serializeAs_ObjectEffect(param1)
        if self.min < 0:
            raise RuntimeError("Forbidden value (" + str(self.min) + ") on element min.")
        param1.write_var_int(self.min)
        if self.max < 0:
            raise RuntimeError("Forbidden value (" + str(self.max) + ") on element max.")
        param1.write_var_int(self.max)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectMinMax(param1)

    def deserializeAs_ObjectEffectMinMax(self, param1):
        super().deserialize(param1)
        self._minFunc(param1)
        self._maxFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectMinMax(param1)

    def deserializeAsyncAs_ObjectEffectMinMax(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._minFunc)
        param1.add_child(self._maxFunc)

    def _minFunc(self, param1):
        self.min = param1.read_var_uh_int()
        if self.min < 0:
            raise RuntimeError("Forbidden value (" + str(self.min) + ") on element of ObjectEffectMinMax.min.")

    def _maxFunc(self, param1):
        self.max = param1.read_var_uh_int()
        if self.max < 0:
            raise RuntimeError("Forbidden value (" + str(self.max) + ") on element of ObjectEffectMinMax.max.")


class ObjectEffectMount(ObjectEffect):
    protocolId = 179

    def __init__(self):
        super().__init__()
        self.mountId = 0
        self.date = 0
        self.modelId = 0

    def getTypeId(self):
        return 179

    def initObjectEffectMount(self, param1=0, param2=0, param3=0, param4=0):
        super().initObjectEffect(param1)
        self.mountId = param2
        self.date = param3
        self.modelId = param4
        return self

    def reset(self):
        super().reset()
        self.mountId = 0
        self.date = 0
        self.modelId = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffectMount(param1)

    def serializeAs_ObjectEffectMount(self, param1):
        super().serializeAs_ObjectEffect(param1)
        if self.mountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.mountId) + ") on element mountId.")
        param1.write_int(self.mountId)
        if self.date < -9007199254740990 or self.date > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.date) + ") on element date.")
        param1.write_double(self.date)
        if self.modelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element modelId.")
        param1.write_var_short(self.modelId)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectMount(param1)

    def deserializeAs_ObjectEffectMount(self, param1):
        super().deserialize(param1)
        self._mountIdFunc(param1)
        self._dateFunc(param1)
        self._modelIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectMount(param1)

    def deserializeAsyncAs_ObjectEffectMount(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._mountIdFunc)
        param1.add_child(self._dateFunc)
        param1.add_child(self._modelIdFunc)

    def _mountIdFunc(self, param1):
        self.mountId = param1.read_int()
        if self.mountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.mountId) + ") on element of ObjectEffectMount.mountId.")

    def _dateFunc(self, param1):
        self.date = param1.read_double()
        if self.date < -9007199254740990 or self.date > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.date) + ") on element of ObjectEffectMount.date.")

    def _modelIdFunc(self, param1):
        self.modelId = param1.read_var_uh_short()
        if self.modelId < 0:
            raise RuntimeError("Forbidden value (" + str(self.modelId) + ") on element of ObjectEffectMount.modelId.")


class ObjectEffectString(ObjectEffect):
    protocolId = 74

    def __init__(self):
        super().__init__()
        self.value = ""

    def getTypeId(self):
        return 74

    def initObjectEffectString(self, param1=0, param2=""):
        super().initObjectEffect(param1)
        self.value = param2
        return self

    def reset(self):
        super().reset()
        self.value = ""

    def serialize(self, param1):
        self.serializeAs_ObjectEffectString(param1)

    def serializeAs_ObjectEffectString(self, param1):
        super().serializeAs_ObjectEffect(param1)
        param1.write_utf(self.value)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectString(param1)

    def deserializeAs_ObjectEffectString(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectString(param1)

    def deserializeAsyncAs_ObjectEffectString(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_utf()


class FriendInformations(AbstractContactInformations):
    protocolId = 78

    def __init__(self):
        super().__init__()
        self.playerState = 99
        self.lastConnection = 0
        self.achievementPoints = 0

    def getTypeId(self):
        return 78

    def initFriendInformations(self, param1=0, param2="", param3=99, param4=0, param5=0):
        super().initAbstractContactInformations(param1,param2)
        self.playerState = param3
        self.lastConnection = param4
        self.achievementPoints = param5
        return self

    def reset(self):
        super().reset()
        self.playerState = 99
        self.lastConnection = 0
        self.achievementPoints = 0

    def serialize(self, param1):
        self.serializeAs_FriendInformations(param1)

    def serializeAs_FriendInformations(self, param1):
        super().serializeAs_AbstractContactInformations(param1)
        param1.write_byte(self.playerState)
        if self.lastConnection < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastConnection) + ") on element lastConnection.")
        param1.write_var_short(self.lastConnection)
        param1.write_int(self.achievementPoints)

    def deserialize(self, param1):
        self.deserializeAs_FriendInformations(param1)

    def deserializeAs_FriendInformations(self, param1):
        super().deserialize(param1)
        self._playerStateFunc(param1)
        self._lastConnectionFunc(param1)
        self._achievementPointsFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FriendInformations(param1)

    def deserializeAsyncAs_FriendInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._playerStateFunc)
        param1.add_child(self._lastConnectionFunc)
        param1.add_child(self._achievementPointsFunc)

    def _playerStateFunc(self, param1):
        self.playerState = param1.read_byte()
        if self.playerState < 0:
            raise RuntimeError("Forbidden value (" + str(self.playerState) + ") on element of FriendInformations.playerState.")

    def _lastConnectionFunc(self, param1):
        self.lastConnection = param1.read_var_uh_short()
        if self.lastConnection < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastConnection) + ") on element of FriendInformations.lastConnection.")

    def _achievementPointsFunc(self, param1):
        self.achievementPoints = param1.read_int()


class FriendSpouseOnlineInformations(FriendSpouseInformations):
    protocolId = 93

    def __init__(self):
        super().__init__()
        self.mapId = 0
        self.subAreaId = 0
        self.inFight = False
        self.followSpouse = False

    def getTypeId(self):
        return 93

    def initFriendSpouseOnlineInformations(self, param1=0, param2=0, param3="", param4=0, param5=0, param6=0, param7=None, param8=None, param9=0, param10=0, param11=0, param12=False, param13=False):
        super().initFriendSpouseInformations(param1,param2,param3,param4,param5,param6,param7,param8,param9)
        self.mapId = param10
        self.subAreaId = param11
        self.inFight = param12
        self.followSpouse = param13
        return self

    def reset(self):
        super().reset()
        self.mapId = 0
        self.subAreaId = 0
        self.inFight = False
        self.followSpouse = False

    def serialize(self, param1):
        self.serializeAs_FriendSpouseOnlineInformations(param1)

    def serializeAs_FriendSpouseOnlineInformations(self, param1):
        super().serializeAs_FriendSpouseInformations(param1)
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.inFight)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.followSpouse)
        param1.write_byte(_loc2_)
        if self.mapId < 0:
            raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element mapId.")
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)

    def deserialize(self, param1):
        self.deserializeAs_FriendSpouseOnlineInformations(param1)

    def deserializeAs_FriendSpouseOnlineInformations(self, param1):
        super().deserialize(param1)
        self.deserializeByteBoxes(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FriendSpouseOnlineInformations(param1)

    def deserializeAsyncAs_FriendSpouseOnlineInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self.deserializeByteBoxes)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.inFight = BooleanByteWrapper.get_flag(_loc2_,0)
        self.followSpouse = BooleanByteWrapper.get_flag(_loc2_,1)

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()
        if self.mapId < 0:
            raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of FriendSpouseOnlineInformations.mapId.")

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of FriendSpouseOnlineInformations.subAreaId.")


class IgnoredInformations(AbstractContactInformations):
    protocolId = 106

    def getTypeId(self):
        return 106

    def initIgnoredInformations(self, param1=0, param2=""):
        super().initAbstractContactInformations(param1,param2)
        return self

    def reset(self):
        super().reset()

    def serialize(self, param1):
        self.serializeAs_IgnoredInformations(param1)

    def serializeAs_IgnoredInformations(self, param1):
        super().serializeAs_AbstractContactInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_IgnoredInformations(param1)

    def deserializeAs_IgnoredInformations(self, param1):
        super().deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_IgnoredInformations(param1)

    def deserializeAsyncAs_IgnoredInformations(self, param1):
        super().deserializeAsync(param1)


class TaxCollectorGuildInformations(TaxCollectorComplementaryInformations):
    protocolId = 446

    def __init__(self):
        super().__init__()
        self.guild = BasicGuildInformations()
        self._guildtree = FuncTree()

    def getTypeId(self):
        return 446

    def initTaxCollectorGuildInformations(self, param1=None):
        self.guild = param1
        return self

    def reset(self):
        self.guild = BasicGuildInformations()

    def serialize(self, param1):
        self.serializeAs_TaxCollectorGuildInformations(param1)

    def serializeAs_TaxCollectorGuildInformations(self, param1):
        super().serializeAs_TaxCollectorComplementaryInformations(param1)
        self.guild.serializeAs_BasicGuildInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorGuildInformations(param1)

    def deserializeAs_TaxCollectorGuildInformations(self, param1):
        super().deserialize(param1)
        self.guild = BasicGuildInformations()
        self.guild.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorGuildInformations(param1)

    def deserializeAsyncAs_TaxCollectorGuildInformations(self, param1):
        super().deserializeAsync(param1)
        self._guildtree = param1.add_child(self._guildtreeFunc)

    def _guildtreeFunc(self, param1):
        self.guild = BasicGuildInformations()
        self.guild.deserializeAsync(self._guildtree)


class TaxCollectorLootInformations(TaxCollectorComplementaryInformations):
    protocolId = 372

    def __init__(self):
        super().__init__()
        self.kamas = 0
        self.experience = 0
        self.pods = 0
        self.itemsValue = 0

    def getTypeId(self):
        return 372

    def initTaxCollectorLootInformations(self, param1=0, param2=0, param3=0, param4=0):
        self.kamas = param1
        self.experience = param2
        self.pods = param3
        self.itemsValue = param4
        return self

    def reset(self):
        self.kamas = 0
        self.experience = 0
        self.pods = 0
        self.itemsValue = 0

    def serialize(self, param1):
        self.serializeAs_TaxCollectorLootInformations(param1)

    def serializeAs_TaxCollectorLootInformations(self, param1):
        super().serializeAs_TaxCollectorComplementaryInformations(param1)
        if self.kamas < 0 or self.kamas > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element kamas.")
        param1.write_var_long(self.kamas)
        if self.experience < 0 or self.experience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element experience.")
        param1.write_var_long(self.experience)
        if self.pods < 0:
            raise RuntimeError("Forbidden value (" + str(self.pods) + ") on element pods.")
        param1.write_var_int(self.pods)
        if self.itemsValue < 0 or self.itemsValue > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.itemsValue) + ") on element itemsValue.")
        param1.write_var_long(self.itemsValue)

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorLootInformations(param1)

    def deserializeAs_TaxCollectorLootInformations(self, param1):
        super().deserialize(param1)
        self._kamasFunc(param1)
        self._experienceFunc(param1)
        self._podsFunc(param1)
        self._itemsValueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorLootInformations(param1)

    def deserializeAsyncAs_TaxCollectorLootInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._kamasFunc)
        param1.add_child(self._experienceFunc)
        param1.add_child(self._podsFunc)
        param1.add_child(self._itemsValueFunc)

    def _kamasFunc(self, param1):
        self.kamas = param1.read_var_uh_long()
        if self.kamas < 0 or self.kamas > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.kamas) + ") on element of TaxCollectorLootInformations.kamas.")

    def _experienceFunc(self, param1):
        self.experience = param1.read_var_uh_long()
        if self.experience < 0 or self.experience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element of TaxCollectorLootInformations.experience.")

    def _podsFunc(self, param1):
        self.pods = param1.read_var_uh_int()
        if self.pods < 0:
            raise RuntimeError("Forbidden value (" + str(self.pods) + ") on element of TaxCollectorLootInformations.pods.")

    def _itemsValueFunc(self, param1):
        self.itemsValue = param1.read_var_uh_long()
        if self.itemsValue < 0 or self.itemsValue > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.itemsValue) + ") on element of TaxCollectorLootInformations.itemsValue.")


class TaxCollectorWaitingForHelpInformations(TaxCollectorComplementaryInformations):
    protocolId = 447

    def __init__(self):
        super().__init__()
        self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo()
        self._waitingForHelpInfotree = FuncTree()

    def getTypeId(self):
        return 447

    def initTaxCollectorWaitingForHelpInformations(self, param1=None):
        self.waitingForHelpInfo = param1
        return self

    def reset(self):
        self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo()

    def serialize(self, param1):
        self.serializeAs_TaxCollectorWaitingForHelpInformations(param1)

    def serializeAs_TaxCollectorWaitingForHelpInformations(self, param1):
        super().serializeAs_TaxCollectorComplementaryInformations(param1)
        self.waitingForHelpInfo.serializeAs_ProtectedEntityWaitingForHelpInfo(param1)

    def deserialize(self, param1):
        self.deserializeAs_TaxCollectorWaitingForHelpInformations(param1)

    def deserializeAs_TaxCollectorWaitingForHelpInformations(self, param1):
        super().deserialize(param1)
        self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo()
        self.waitingForHelpInfo.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_TaxCollectorWaitingForHelpInformations(param1)

    def deserializeAsyncAs_TaxCollectorWaitingForHelpInformations(self, param1):
        super().deserializeAsync(param1)
        self._waitingForHelpInfotree = param1.add_child(self._waitingForHelpInfotreeFunc)

    def _waitingForHelpInfotreeFunc(self, param1):
        self.waitingForHelpInfo = ProtectedEntityWaitingForHelpInfo()
        self.waitingForHelpInfo.deserializeAsync(self._waitingForHelpInfotree)


class AccountHouseInformations(HouseInformations):
    protocolId = 390

    def __init__(self):
        super().__init__()
        self.houseInfos = HouseInstanceInformations()
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self._houseInfostree = FuncTree()

    def getTypeId(self):
        return 390

    def initAccountHouseInformations(self, param1=0, param2=0, param3=None, param4=0, param5=0, param6=0, param7=0):
        super().initHouseInformations(param1,param2)
        self.houseInfos = param3
        self.worldX = param4
        self.worldY = param5
        self.mapId = param6
        self.subAreaId = param7
        return self

    def reset(self):
        super().reset()
        self.houseInfos = HouseInstanceInformations()
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0

    def serialize(self, param1):
        self.serializeAs_AccountHouseInformations(param1)

    def serializeAs_AccountHouseInformations(self, param1):
        super().serializeAs_HouseInformations(param1)
        param1.write_short(self.houseInfos.getTypeId())
        self.houseInfos.serialize(param1)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)

    def deserialize(self, param1):
        self.deserializeAs_AccountHouseInformations(param1)

    def deserializeAs_AccountHouseInformations(self, param1):
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        self.houseInfos = ProtocolTypeManager.get_instance(HouseInstanceInformations,_loc2_)
        self.houseInfos.deserialize(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AccountHouseInformations(param1)

    def deserializeAsyncAs_AccountHouseInformations(self, param1):
        super().deserializeAsync(param1)
        self._houseInfostree = param1.add_child(self._houseInfostreeFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)

    def _houseInfostreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.houseInfos = ProtocolTypeManager.get_instance(HouseInstanceInformations,_loc2_)
        self.houseInfos.deserializeAsync(self._houseInfostree)

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of AccountHouseInformations.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of AccountHouseInformations.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of AccountHouseInformations.subAreaId.")


class HouseGuildedInformations(HouseInstanceInformations):
    protocolId = 512

    def __init__(self):
        super().__init__()
        self.guildInfo = GuildInformations()
        self._guildInfotree = FuncTree()

    def getTypeId(self):
        return 512

    def initHouseGuildedInformations(self, param1=0, param2=False, param3=False, param4="", param5=0, param6=False, param7=None):
        super().initHouseInstanceInformations(param1,param2,param3,param4,param5,param6)
        self.guildInfo = param7
        return self

    def reset(self):
        super().reset()
        self.guildInfo = GuildInformations()

    def serialize(self, param1):
        self.serializeAs_HouseGuildedInformations(param1)

    def serializeAs_HouseGuildedInformations(self, param1):
        super().serializeAs_HouseInstanceInformations(param1)
        self.guildInfo.serializeAs_GuildInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_HouseGuildedInformations(param1)

    def deserializeAs_HouseGuildedInformations(self, param1):
        super().deserialize(param1)
        self.guildInfo = GuildInformations()
        self.guildInfo.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HouseGuildedInformations(param1)

    def deserializeAsyncAs_HouseGuildedInformations(self, param1):
        super().deserializeAsync(param1)
        self._guildInfotree = param1.add_child(self._guildInfotreeFunc)

    def _guildInfotreeFunc(self, param1):
        self.guildInfo = GuildInformations()
        self.guildInfo.deserializeAsync(self._guildInfotree)


class HouseInformationsForGuild(HouseInformations):
    protocolId = 170

    def __init__(self):
        super().__init__()
        self.instanceId = 0
        self.secondHand = False
        self.ownerName = ""
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.skillListIds = []
        self.guildshareParams = 0
        self._skillListIdstree = FuncTree()

    def getTypeId(self):
        return 170

    def initHouseInformationsForGuild(self, param1=0, param2=0, param3=0, param4=False, param5="", param6=0, param7=0, param8=0, param9=0, param10=[], param11=0):
        super().initHouseInformations(param1,param2)
        self.instanceId = param3
        self.secondHand = param4
        self.ownerName = param5
        self.worldX = param6
        self.worldY = param7
        self.mapId = param8
        self.subAreaId = param9
        self.skillListIds = param10
        self.guildshareParams = param11
        return self

    def reset(self):
        super().reset()
        self.instanceId = 0
        self.secondHand = False
        self.ownerName = ""
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.skillListIds = []
        self.guildshareParams = 0

    def serialize(self, param1):
        self.serializeAs_HouseInformationsForGuild(param1)

    def serializeAs_HouseInformationsForGuild(self, param1):
        super().serializeAs_HouseInformations(param1)
        if self.instanceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element instanceId.")
        param1.write_int(self.instanceId)
        param1.write_boolean(self.secondHand)
        param1.write_utf(self.ownerName)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        param1.write_short(len(self.skillListIds))
        _loc2_ = 0
        while _loc2_ < len(self.skillListIds):
            param1.write_int(self.skillListIds[_loc2_])
            _loc2_ += 1
        if self.guildshareParams < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildshareParams) + ") on element guildshareParams.")
        param1.write_var_int(self.guildshareParams)

    def deserialize(self, param1):
        self.deserializeAs_HouseInformationsForGuild(param1)

    def deserializeAs_HouseInformationsForGuild(self, param1):
        _loc4_ = 0
        super().deserialize(param1)
        self._instanceIdFunc(param1)
        self._secondHandFunc(param1)
        self._ownerNameFunc(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_int()
            self.skillListIds.append(_loc4_)
            _loc3_ += 1
        self._guildshareParamsFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HouseInformationsForGuild(param1)

    def deserializeAsyncAs_HouseInformationsForGuild(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._instanceIdFunc)
        param1.add_child(self._secondHandFunc)
        param1.add_child(self._ownerNameFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)
        self._skillListIdstree = param1.add_child(self._skillListIdstreeFunc)
        param1.add_child(self._guildshareParamsFunc)

    def _instanceIdFunc(self, param1):
        self.instanceId = param1.read_int()
        if self.instanceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of HouseInformationsForGuild.instanceId.")

    def _secondHandFunc(self, param1):
        self.secondHand = param1.read_boolean()

    def _ownerNameFunc(self, param1):
        self.ownerName = param1.read_utf()

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of HouseInformationsForGuild.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of HouseInformationsForGuild.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of HouseInformationsForGuild.subAreaId.")

    def _skillListIdstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._skillListIdstree.add_child(self._skillListIdsFunc)
            _loc3_ += 1

    def _skillListIdsFunc(self, param1):
        _loc2_ = param1.read_int()
        self.skillListIds.append(_loc2_)

    def _guildshareParamsFunc(self, param1):
        self.guildshareParams = param1.read_var_uh_int()
        if self.guildshareParams < 0:
            raise RuntimeError("Forbidden value (" + str(self.guildshareParams) + ") on element of HouseInformationsForGuild.guildshareParams.")


class HouseInformationsInside(HouseInformations):
    protocolId = 218

    def __init__(self):
        super().__init__()
        self.houseInfos = HouseInstanceInformations()
        self.worldX = 0
        self.worldY = 0
        self._houseInfostree = FuncTree()

    def getTypeId(self):
        return 218

    def initHouseInformationsInside(self, param1=0, param2=0, param3=None, param4=0, param5=0):
        super().initHouseInformations(param1,param2)
        self.houseInfos = param3
        self.worldX = param4
        self.worldY = param5
        return self

    def reset(self):
        super().reset()
        self.houseInfos = HouseInstanceInformations()
        self.worldY = 0

    def serialize(self, param1):
        self.serializeAs_HouseInformationsInside(param1)

    def serializeAs_HouseInformationsInside(self, param1):
        super().serializeAs_HouseInformations(param1)
        param1.write_short(self.houseInfos.getTypeId())
        self.houseInfos.serialize(param1)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)

    def deserialize(self, param1):
        self.deserializeAs_HouseInformationsInside(param1)

    def deserializeAs_HouseInformationsInside(self, param1):
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        self.houseInfos = ProtocolTypeManager.get_instance(HouseInstanceInformations,_loc2_)
        self.houseInfos.deserialize(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HouseInformationsInside(param1)

    def deserializeAsyncAs_HouseInformationsInside(self, param1):
        super().deserializeAsync(param1)
        self._houseInfostree = param1.add_child(self._houseInfostreeFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)

    def _houseInfostreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.houseInfos = ProtocolTypeManager.get_instance(HouseInstanceInformations,_loc2_)
        self.houseInfos.deserializeAsync(self._houseInfostree)

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of HouseInformationsInside.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of HouseInformationsInside.worldY.")


class HouseOnMapInformations(HouseInformations):
    protocolId = 510

    def __init__(self):
        super().__init__()
        self.doorsOnMap = []
        self.houseInstances = []
        self._doorsOnMaptree = FuncTree()
        self._houseInstancestree = FuncTree()

    def getTypeId(self):
        return 510

    def initHouseOnMapInformations(self, param1=0, param2=0, param3=[], param4=[]):
        super().initHouseInformations(param1,param2)
        self.doorsOnMap = param3
        self.houseInstances = param4
        return self

    def reset(self):
        super().reset()
        self.doorsOnMap = []
        self.houseInstances = []

    def serialize(self, param1):
        self.serializeAs_HouseOnMapInformations(param1)

    def serializeAs_HouseOnMapInformations(self, param1):
        super().serializeAs_HouseInformations(param1)
        param1.write_short(len(self.doorsOnMap))
        _loc2_ = 0
        while _loc2_ < len(self.doorsOnMap):
            if self.doorsOnMap[_loc2_] < 0:
                raise RuntimeError("Forbidden value (" + str(self.doorsOnMap[_loc2_]) + ") on element 1 (starting at 1) of doorsOnMap.")
            param1.write_int(self.doorsOnMap[_loc2_])
            _loc2_ += 1
        param1.write_short(len(self.houseInstances))
        _loc3_ = 0
        while _loc3_ < len(self.houseInstances):
            as_parent(self.houseInstances[_loc3_], HouseInstanceInformations).serializeAs_HouseInstanceInformations(param1)
            _loc3_ += 1

    def deserialize(self, param1):
        self.deserializeAs_HouseOnMapInformations(param1)

    def deserializeAs_HouseOnMapInformations(self, param1):
        _loc6_ = 0
        _loc7_ = None
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc6_ = param1.read_int()
            if _loc6_ < 0:
                raise RuntimeError("Forbidden value (" + str(_loc6_) + ") on elements of doorsOnMap.")
            self.doorsOnMap.append(_loc6_)
            _loc3_ += 1
        _loc4_ = param1.read_unsigned_short()
        _loc5_ = 0
        while _loc5_ < _loc4_:
            _loc7_ = HouseInstanceInformations()
            _loc7_.deserialize(param1)
            self.houseInstances.append(_loc7_)
            _loc5_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_HouseOnMapInformations(param1)

    def deserializeAsyncAs_HouseOnMapInformations(self, param1):
        super().deserializeAsync(param1)
        self._doorsOnMaptree = param1.add_child(self._doorsOnMaptreeFunc)
        self._houseInstancestree = param1.add_child(self._houseInstancestreeFunc)

    def _doorsOnMaptreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._doorsOnMaptree.add_child(self._doorsOnMapFunc)
            _loc3_ += 1

    def _doorsOnMapFunc(self, param1):
        _loc2_ = param1.read_int()
        if _loc2_ < 0:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of doorsOnMap.")
        self.doorsOnMap.append(_loc2_)

    def _houseInstancestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._houseInstancestree.add_child(self._houseInstancesFunc)
            _loc3_ += 1

    def _houseInstancesFunc(self, param1):
        _loc2_ = HouseInstanceInformations()
        _loc2_.deserialize(param1)
        self.houseInstances.append(_loc2_)


class PartyIdol(Idol):
    protocolId = 490

    def __init__(self):
        super().__init__()
        self.ownersIds = []
        self._ownersIdstree = FuncTree()

    def getTypeId(self):
        return 490

    def initPartyIdol(self, param1=0, param2=0, param3=0, param4=[]):
        super().initIdol(param1,param2,param3)
        self.ownersIds = param4
        return self

    def reset(self):
        super().reset()
        self.ownersIds = []

    def serialize(self, param1):
        self.serializeAs_PartyIdol(param1)

    def serializeAs_PartyIdol(self, param1):
        super().serializeAs_Idol(param1)
        param1.write_short(len(self.ownersIds))
        _loc2_ = 0
        while _loc2_ < len(self.ownersIds):
            if self.ownersIds[_loc2_] < 0 or self.ownersIds[_loc2_] > 9007199254740990:
                raise RuntimeError("Forbidden value (" + str(self.ownersIds[_loc2_]) + ") on element 1 (starting at 1) of ownersIds.")
            param1.write_var_long(self.ownersIds[_loc2_])
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_PartyIdol(param1)

    def deserializeAs_PartyIdol(self, param1):
        _loc4_ = None
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_var_uh_long()
            if _loc4_ < 0 or _loc4_ > 9007199254740990:
                raise RuntimeError("Forbidden value (" + str(_loc4_) + ") on elements of ownersIds.")
            self.ownersIds.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PartyIdol(param1)

    def deserializeAsyncAs_PartyIdol(self, param1):
        super().deserializeAsync(param1)
        self._ownersIdstree = param1.add_child(self._ownersIdstreeFunc)

    def _ownersIdstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._ownersIdstree.add_child(self._ownersIdsFunc)
            _loc3_ += 1

    def _ownersIdsFunc(self, param1):
        _loc2_ = param1.read_var_uh_long()
        if _loc2_ < 0 or _loc2_ > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(_loc2_) + ") on elements of ownersIds.")
        self.ownersIds.append(_loc2_)


class InteractiveElementNamedSkill(InteractiveElementSkill):
    protocolId = 220

    def __init__(self):
        super().__init__()
        self.nameId = 0

    def getTypeId(self):
        return 220

    def initInteractiveElementNamedSkill(self, param1=0, param2=0, param3=0):
        super().initInteractiveElementSkill(param1,param2)
        self.nameId = param3
        return self

    def reset(self):
        super().reset()
        self.nameId = 0

    def serialize(self, param1):
        self.serializeAs_InteractiveElementNamedSkill(param1)

    def serializeAs_InteractiveElementNamedSkill(self, param1):
        super().serializeAs_InteractiveElementSkill(param1)
        if self.nameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.nameId) + ") on element nameId.")
        param1.write_var_int(self.nameId)

    def deserialize(self, param1):
        self.deserializeAs_InteractiveElementNamedSkill(param1)

    def deserializeAs_InteractiveElementNamedSkill(self, param1):
        super().deserialize(param1)
        self._nameIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_InteractiveElementNamedSkill(param1)

    def deserializeAsyncAs_InteractiveElementNamedSkill(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nameIdFunc)

    def _nameIdFunc(self, param1):
        self.nameId = param1.read_var_uh_int()
        if self.nameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.nameId) + ") on element of InteractiveElementNamedSkill.nameId.")


class InteractiveElementWithAgeBonus(InteractiveElement):
    protocolId = 398

    def __init__(self):
        super().__init__()
        self.ageBonus = 0

    def getTypeId(self):
        return 398

    def initInteractiveElementWithAgeBonus(self, param1=0, param2=0, param3=[], param4=[], param5=False, param6=0):
        super().initInteractiveElement(param1,param2,param3,param4,param5)
        self.ageBonus = param6
        return self

    def reset(self):
        super().reset()
        self.ageBonus = 0

    def serialize(self, param1):
        self.serializeAs_InteractiveElementWithAgeBonus(param1)

    def serializeAs_InteractiveElementWithAgeBonus(self, param1):
        super().serializeAs_InteractiveElement(param1)
        if self.ageBonus < -1 or self.ageBonus > 1000:
            raise RuntimeError("Forbidden value (" + str(self.ageBonus) + ") on element ageBonus.")
        param1.write_short(self.ageBonus)

    def deserialize(self, param1):
        self.deserializeAs_InteractiveElementWithAgeBonus(param1)

    def deserializeAs_InteractiveElementWithAgeBonus(self, param1):
        super().deserialize(param1)
        self._ageBonusFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_InteractiveElementWithAgeBonus(param1)

    def deserializeAsyncAs_InteractiveElementWithAgeBonus(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._ageBonusFunc)

    def _ageBonusFunc(self, param1):
        self.ageBonus = param1.read_short()
        if self.ageBonus < -1 or self.ageBonus > 1000:
            raise RuntimeError("Forbidden value (" + str(self.ageBonus) + ") on element of InteractiveElementWithAgeBonus.ageBonus.")


class SkillActionDescriptionCraft(SkillActionDescription):
    protocolId = 100

    def __init__(self):
        super().__init__()
        self.probability = 0

    def getTypeId(self):
        return 100

    def initSkillActionDescriptionCraft(self, param1=0, param2=0):
        super().initSkillActionDescription(param1)
        self.probability = param2
        return self

    def reset(self):
        super().reset()
        self.probability = 0

    def serialize(self, param1):
        self.serializeAs_SkillActionDescriptionCraft(param1)

    def serializeAs_SkillActionDescriptionCraft(self, param1):
        super().serializeAs_SkillActionDescription(param1)
        if self.probability < 0:
            raise RuntimeError("Forbidden value (" + str(self.probability) + ") on element probability.")
        param1.write_byte(self.probability)

    def deserialize(self, param1):
        self.deserializeAs_SkillActionDescriptionCraft(param1)

    def deserializeAs_SkillActionDescriptionCraft(self, param1):
        super().deserialize(param1)
        self._probabilityFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_SkillActionDescriptionCraft(param1)

    def deserializeAsyncAs_SkillActionDescriptionCraft(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._probabilityFunc)

    def _probabilityFunc(self, param1):
        self.probability = param1.read_byte()
        if self.probability < 0:
            raise RuntimeError("Forbidden value (" + str(self.probability) + ") on element of SkillActionDescriptionCraft.probability.")


class SkillActionDescriptionTimed(SkillActionDescription):
    protocolId = 103

    def __init__(self):
        super().__init__()
        self.time = 0

    def getTypeId(self):
        return 103

    def initSkillActionDescriptionTimed(self, param1=0, param2=0):
        super().initSkillActionDescription(param1)
        self.time = param2
        return self

    def reset(self):
        super().reset()
        self.time = 0

    def serialize(self, param1):
        self.serializeAs_SkillActionDescriptionTimed(param1)

    def serializeAs_SkillActionDescriptionTimed(self, param1):
        super().serializeAs_SkillActionDescription(param1)
        if self.time < 0 or self.time > 255:
            raise RuntimeError("Forbidden value (" + str(self.time) + ") on element time.")
        param1.write_byte(self.time)

    def deserialize(self, param1):
        self.deserializeAs_SkillActionDescriptionTimed(param1)

    def deserializeAs_SkillActionDescriptionTimed(self, param1):
        super().deserialize(param1)
        self._timeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_SkillActionDescriptionTimed(param1)

    def deserializeAsyncAs_SkillActionDescriptionTimed(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._timeFunc)

    def _timeFunc(self, param1):
        self.time = param1.read_unsigned_byte()
        if self.time < 0 or self.time > 255:
            raise RuntimeError("Forbidden value (" + str(self.time) + ") on element of SkillActionDescriptionTimed.time.")


class UpdateMountIntBoost(UpdateMountBoost):
    protocolId = 357

    def __init__(self):
        super().__init__()
        self.value = 0

    def getTypeId(self):
        return 357

    def initUpdateMountIntBoost(self, param1=0, param2=0):
        super().initUpdateMountBoost(param1)
        self.value = param2
        return self

    def reset(self):
        super().reset()
        self.value = 0

    def serialize(self, param1):
        self.serializeAs_UpdateMountIntBoost(param1)

    def serializeAs_UpdateMountIntBoost(self, param1):
        super().serializeAs_UpdateMountBoost(param1)
        param1.write_int(self.value)

    def deserialize(self, param1):
        self.deserializeAs_UpdateMountIntBoost(param1)

    def deserializeAs_UpdateMountIntBoost(self, param1):
        super().deserialize(param1)
        self._valueFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_UpdateMountIntBoost(param1)

    def deserializeAsyncAs_UpdateMountIntBoost(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._valueFunc)

    def _valueFunc(self, param1):
        self.value = param1.read_int()


class PaddockContentInformations(PaddockInformations):
    protocolId = 183

    def __init__(self):
        super().__init__()
        self.paddockId = 0
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.abandonned = False
        self.mountsInformations = []
        self._mountsInformationstree = FuncTree()

    def getTypeId(self):
        return 183

    def initPaddockContentInformations(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0, param8=False, param9=[]):
        super().initPaddockInformations(param1,param2)
        self.paddockId = param3
        self.worldX = param4
        self.worldY = param5
        self.mapId = param6
        self.subAreaId = param7
        self.abandonned = param8
        self.mountsInformations = param9
        return self

    def reset(self):
        super().reset()
        self.paddockId = 0
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.abandonned = False
        self.mountsInformations = []

    def serialize(self, param1):
        self.serializeAs_PaddockContentInformations(param1)

    def serializeAs_PaddockContentInformations(self, param1):
        super().serializeAs_PaddockInformations(param1)
        param1.write_int(self.paddockId)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        param1.write_boolean(self.abandonned)
        param1.write_short(len(self.mountsInformations))
        _loc2_ = 0
        while _loc2_ < len(self.mountsInformations):
            as_parent(self.mountsInformations[_loc2_], MountInformationsForPaddock).serializeAs_MountInformationsForPaddock(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_PaddockContentInformations(param1)

    def deserializeAs_PaddockContentInformations(self, param1):
        _loc4_ = None
        super().deserialize(param1)
        self._paddockIdFunc(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)
        self._abandonnedFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = MountInformationsForPaddock()
            _loc4_.deserialize(param1)
            self.mountsInformations.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PaddockContentInformations(param1)

    def deserializeAsyncAs_PaddockContentInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._paddockIdFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)
        param1.add_child(self._abandonnedFunc)
        self._mountsInformationstree = param1.add_child(self._mountsInformationstreeFunc)

    def _paddockIdFunc(self, param1):
        self.paddockId = param1.read_int()

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PaddockContentInformations.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PaddockContentInformations.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PaddockContentInformations.subAreaId.")

    def _abandonnedFunc(self, param1):
        self.abandonned = param1.read_boolean()

    def _mountsInformationstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._mountsInformationstree.add_child(self._mountsInformationsFunc)
            _loc3_ += 1

    def _mountsInformationsFunc(self, param1):
        _loc2_ = MountInformationsForPaddock()
        _loc2_.deserialize(param1)
        self.mountsInformations.append(_loc2_)


class PaddockGuildedInformations(PaddockBuyableInformations):
    protocolId = 508

    def __init__(self):
        super().__init__()
        self.deserted = False
        self.guildInfo = GuildInformations()
        self._guildInfotree = FuncTree()

    def getTypeId(self):
        return 508

    def initPaddockGuildedInformations(self, param1=0, param2=False, param3=False, param4=None):
        super().initPaddockBuyableInformations(param1,param2)
        self.deserted = param3
        self.guildInfo = param4
        return self

    def reset(self):
        super().reset()
        self.deserted = False
        self.guildInfo = GuildInformations()

    def serialize(self, param1):
        self.serializeAs_PaddockGuildedInformations(param1)

    def serializeAs_PaddockGuildedInformations(self, param1):
        super().serializeAs_PaddockBuyableInformations(param1)
        param1.write_boolean(self.deserted)
        self.guildInfo.serializeAs_GuildInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_PaddockGuildedInformations(param1)

    def deserializeAs_PaddockGuildedInformations(self, param1):
        super().deserialize(param1)
        self._desertedFunc(param1)
        self.guildInfo = GuildInformations()
        self.guildInfo.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PaddockGuildedInformations(param1)

    def deserializeAsyncAs_PaddockGuildedInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._desertedFunc)
        self._guildInfotree = param1.add_child(self._guildInfotreeFunc)

    def _desertedFunc(self, param1):
        self.deserted = param1.read_boolean()

    def _guildInfotreeFunc(self, param1):
        self.guildInfo = GuildInformations()
        self.guildInfo.deserializeAsync(self._guildInfotree)


class PaddockInstancesInformations(PaddockInformations):
    protocolId = 509

    def __init__(self):
        super().__init__()
        self.paddocks = []
        self._paddockstree = FuncTree()

    def getTypeId(self):
        return 509

    def initPaddockInstancesInformations(self, param1=0, param2=0, param3=[]):
        super().initPaddockInformations(param1,param2)
        self.paddocks = param3
        return self

    def reset(self):
        super().reset()
        self.paddocks = []

    def serialize(self, param1):
        self.serializeAs_PaddockInstancesInformations(param1)

    def serializeAs_PaddockInstancesInformations(self, param1):
        super().serializeAs_PaddockInformations(param1)
        param1.write_short(len(self.paddocks))
        _loc2_ = 0
        while _loc2_ < len(self.paddocks):
            param1.write_short(as_parent(self.paddocks[_loc2_], PaddockBuyableInformations).getTypeId())
            as_parent(self.paddocks[_loc2_], PaddockBuyableInformations).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_PaddockInstancesInformations(param1)

    def deserializeAs_PaddockInstancesInformations(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(PaddockBuyableInformations,_loc4_)
            _loc5_.deserialize(param1)
            self.paddocks.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PaddockInstancesInformations(param1)

    def deserializeAsyncAs_PaddockInstancesInformations(self, param1):
        super().deserializeAsync(param1)
        self._paddockstree = param1.add_child(self._paddockstreeFunc)

    def _paddockstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._paddockstree.add_child(self._paddocksFunc)
            _loc3_ += 1

    def _paddocksFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(PaddockBuyableInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.paddocks.append(_loc3_)


class PaddockItem(ObjectItemInRolePlay):
    protocolId = 185

    def __init__(self):
        super().__init__()
        self.durability = ItemDurability()
        self._durabilitytree = FuncTree()

    def getTypeId(self):
        return 185

    def initPaddockItem(self, param1=0, param2=0, param3=None):
        super().initObjectItemInRolePlay(param1,param2)
        self.durability = param3
        return self

    def reset(self):
        super().reset()
        self.durability = ItemDurability()

    def serialize(self, param1):
        self.serializeAs_PaddockItem(param1)

    def serializeAs_PaddockItem(self, param1):
        super().serializeAs_ObjectItemInRolePlay(param1)
        self.durability.serializeAs_ItemDurability(param1)

    def deserialize(self, param1):
        self.deserializeAs_PaddockItem(param1)

    def deserializeAs_PaddockItem(self, param1):
        super().deserialize(param1)
        self.durability = ItemDurability()
        self.durability.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PaddockItem(param1)

    def deserializeAsyncAs_PaddockItem(self, param1):
        super().deserializeAsync(param1)
        self._durabilitytree = param1.add_child(self._durabilitytreeFunc)

    def _durabilitytreeFunc(self, param1):
        self.durability = ItemDurability()
        self.durability.deserializeAsync(self._durabilitytree)


class AllianceInsiderPrismInformation(PrismInformation):
    protocolId = 431

    def __init__(self):
        super().__init__()
        self.lastTimeSlotModificationDate = 0
        self.lastTimeSlotModificationAuthorGuildId = 0
        self.lastTimeSlotModificationAuthorId = 0
        self.lastTimeSlotModificationAuthorName = ""
        self.modulesObjects = []
        self._modulesObjectstree = FuncTree()

    def getTypeId(self):
        return 431

    def initAllianceInsiderPrismInformation(self, param1=0, param2=1, param3=0, param4=0, param5=0, param6=0, param7=0, param8=0, param9="", param10=[]):
        super().initPrismInformation(param1,param2,param3,param4,param5)
        self.lastTimeSlotModificationDate = param6
        self.lastTimeSlotModificationAuthorGuildId = param7
        self.lastTimeSlotModificationAuthorId = param8
        self.lastTimeSlotModificationAuthorName = param9
        self.modulesObjects = param10
        return self

    def reset(self):
        super().reset()
        self.lastTimeSlotModificationDate = 0
        self.lastTimeSlotModificationAuthorGuildId = 0
        self.lastTimeSlotModificationAuthorId = 0
        self.lastTimeSlotModificationAuthorName = ""
        self.modulesObjects = []

    def serialize(self, param1):
        self.serializeAs_AllianceInsiderPrismInformation(param1)

    def serializeAs_AllianceInsiderPrismInformation(self, param1):
        super().serializeAs_PrismInformation(param1)
        if self.lastTimeSlotModificationDate < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationDate) + ") on element lastTimeSlotModificationDate.")
        param1.write_int(self.lastTimeSlotModificationDate)
        if self.lastTimeSlotModificationAuthorGuildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationAuthorGuildId) + ") on element lastTimeSlotModificationAuthorGuildId.")
        param1.write_var_int(self.lastTimeSlotModificationAuthorGuildId)
        if self.lastTimeSlotModificationAuthorId < 0 or self.lastTimeSlotModificationAuthorId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationAuthorId) + ") on element lastTimeSlotModificationAuthorId.")
        param1.write_var_long(self.lastTimeSlotModificationAuthorId)
        param1.write_utf(self.lastTimeSlotModificationAuthorName)
        param1.write_short(len(self.modulesObjects))
        _loc2_ = 0
        while _loc2_ < len(self.modulesObjects):
            as_parent(self.modulesObjects[_loc2_], ObjectItem).serializeAs_ObjectItem(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_AllianceInsiderPrismInformation(param1)

    def deserializeAs_AllianceInsiderPrismInformation(self, param1):
        _loc4_ = None
        super().deserialize(param1)
        self._lastTimeSlotModificationDateFunc(param1)
        self._lastTimeSlotModificationAuthorGuildIdFunc(param1)
        self._lastTimeSlotModificationAuthorIdFunc(param1)
        self._lastTimeSlotModificationAuthorNameFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = ObjectItem()
            _loc4_.deserialize(param1)
            self.modulesObjects.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AllianceInsiderPrismInformation(param1)

    def deserializeAsyncAs_AllianceInsiderPrismInformation(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._lastTimeSlotModificationDateFunc)
        param1.add_child(self._lastTimeSlotModificationAuthorGuildIdFunc)
        param1.add_child(self._lastTimeSlotModificationAuthorIdFunc)
        param1.add_child(self._lastTimeSlotModificationAuthorNameFunc)
        self._modulesObjectstree = param1.add_child(self._modulesObjectstreeFunc)

    def _lastTimeSlotModificationDateFunc(self, param1):
        self.lastTimeSlotModificationDate = param1.read_int()
        if self.lastTimeSlotModificationDate < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationDate) + ") on element of AllianceInsiderPrismInformation.lastTimeSlotModificationDate.")

    def _lastTimeSlotModificationAuthorGuildIdFunc(self, param1):
        self.lastTimeSlotModificationAuthorGuildId = param1.read_var_uh_int()
        if self.lastTimeSlotModificationAuthorGuildId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationAuthorGuildId) + ") on element of AllianceInsiderPrismInformation.lastTimeSlotModificationAuthorGuildId.")

    def _lastTimeSlotModificationAuthorIdFunc(self, param1):
        self.lastTimeSlotModificationAuthorId = param1.read_var_uh_long()
        if self.lastTimeSlotModificationAuthorId < 0 or self.lastTimeSlotModificationAuthorId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.lastTimeSlotModificationAuthorId) + ") on element of AllianceInsiderPrismInformation.lastTimeSlotModificationAuthorId.")

    def _lastTimeSlotModificationAuthorNameFunc(self, param1):
        self.lastTimeSlotModificationAuthorName = param1.read_utf()

    def _modulesObjectstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._modulesObjectstree.add_child(self._modulesObjectsFunc)
            _loc3_ += 1

    def _modulesObjectsFunc(self, param1):
        _loc2_ = ObjectItem()
        _loc2_.deserialize(param1)
        self.modulesObjects.append(_loc2_)


class AlliancePrismInformation(PrismInformation):
    protocolId = 427

    def __init__(self):
        super().__init__()
        self.alliance = AllianceInformations()
        self._alliancetree = FuncTree()

    def getTypeId(self):
        return 427

    def initAlliancePrismInformation(self, param1=0, param2=1, param3=0, param4=0, param5=0, param6=None):
        super().initPrismInformation(param1,param2,param3,param4,param5)
        self.alliance = param6
        return self

    def reset(self):
        super().reset()
        self.alliance = AllianceInformations()

    def serialize(self, param1):
        self.serializeAs_AlliancePrismInformation(param1)

    def serializeAs_AlliancePrismInformation(self, param1):
        super().serializeAs_PrismInformation(param1)
        self.alliance.serializeAs_AllianceInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_AlliancePrismInformation(param1)

    def deserializeAs_AlliancePrismInformation(self, param1):
        super().deserialize(param1)
        self.alliance = AllianceInformations()
        self.alliance.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AlliancePrismInformation(param1)

    def deserializeAsyncAs_AlliancePrismInformation(self, param1):
        super().deserializeAsync(param1)
        self._alliancetree = param1.add_child(self._alliancetreeFunc)

    def _alliancetreeFunc(self, param1):
        self.alliance = AllianceInformations()
        self.alliance.deserializeAsync(self._alliancetree)


class PrismGeolocalizedInformation(PrismSubareaEmptyInfo):
    protocolId = 434

    def __init__(self):
        super().__init__()
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.prism = PrismInformation()
        self._prismtree = FuncTree()

    def getTypeId(self):
        return 434

    def initPrismGeolocalizedInformation(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=None):
        super().initPrismSubareaEmptyInfo(param1,param2)
        self.worldX = param3
        self.worldY = param4
        self.mapId = param5
        self.prism = param6
        return self

    def reset(self):
        super().reset()
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.prism = PrismInformation()

    def serialize(self, param1):
        self.serializeAs_PrismGeolocalizedInformation(param1)

    def serializeAs_PrismGeolocalizedInformation(self, param1):
        super().serializeAs_PrismSubareaEmptyInfo(param1)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        param1.write_short(self.prism.getTypeId())
        self.prism.serialize(param1)

    def deserialize(self, param1):
        self.deserializeAs_PrismGeolocalizedInformation(param1)

    def deserializeAs_PrismGeolocalizedInformation(self, param1):
        super().deserialize(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        self.prism = ProtocolTypeManager.get_instance(PrismInformation,_loc2_)
        self.prism.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PrismGeolocalizedInformation(param1)

    def deserializeAsyncAs_PrismGeolocalizedInformation(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        self._prismtree = param1.add_child(self._prismtreeFunc)

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PrismGeolocalizedInformation.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PrismGeolocalizedInformation.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _prismtreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.prism = ProtocolTypeManager.get_instance(PrismInformation,_loc2_)
        self.prism.deserializeAsync(self._prismtree)


class ShortcutEmote(Shortcut):
    protocolId = 389

    def __init__(self):
        super().__init__()
        self.emoteId = 0

    def getTypeId(self):
        return 389

    def initShortcutEmote(self, param1=0, param2=0):
        super().initShortcut(param1)
        self.emoteId = param2
        return self

    def reset(self):
        super().reset()
        self.emoteId = 0

    def serialize(self, param1):
        self.serializeAs_ShortcutEmote(param1)

    def serializeAs_ShortcutEmote(self, param1):
        super().serializeAs_Shortcut(param1)
        if self.emoteId < 0 or self.emoteId > 255:
            raise RuntimeError("Forbidden value (" + str(self.emoteId) + ") on element emoteId.")
        param1.write_byte(self.emoteId)

    def deserialize(self, param1):
        self.deserializeAs_ShortcutEmote(param1)

    def deserializeAs_ShortcutEmote(self, param1):
        super().deserialize(param1)
        self._emoteIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ShortcutEmote(param1)

    def deserializeAsyncAs_ShortcutEmote(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._emoteIdFunc)

    def _emoteIdFunc(self, param1):
        self.emoteId = param1.read_unsigned_byte()
        if self.emoteId < 0 or self.emoteId > 255:
            raise RuntimeError("Forbidden value (" + str(self.emoteId) + ") on element of ShortcutEmote.emoteId.")


class ShortcutObject(Shortcut):
    protocolId = 367

    def getTypeId(self):
        return 367

    def initShortcutObject(self, param1=0):
        super().initShortcut(param1)
        return self

    def reset(self):
        super().reset()

    def serialize(self, param1):
        self.serializeAs_ShortcutObject(param1)

    def serializeAs_ShortcutObject(self, param1):
        super().serializeAs_Shortcut(param1)

    def deserialize(self, param1):
        self.deserializeAs_ShortcutObject(param1)

    def deserializeAs_ShortcutObject(self, param1):
        super().deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ShortcutObject(param1)

    def deserializeAsyncAs_ShortcutObject(self, param1):
        super().deserializeAsync(param1)


class ShortcutSmiley(Shortcut):
    protocolId = 388

    def __init__(self):
        super().__init__()
        self.smileyId = 0

    def getTypeId(self):
        return 388

    def initShortcutSmiley(self, param1=0, param2=0):
        super().initShortcut(param1)
        self.smileyId = param2
        return self

    def reset(self):
        super().reset()
        self.smileyId = 0

    def serialize(self, param1):
        self.serializeAs_ShortcutSmiley(param1)

    def serializeAs_ShortcutSmiley(self, param1):
        super().serializeAs_Shortcut(param1)
        if self.smileyId < 0:
            raise RuntimeError("Forbidden value (" + str(self.smileyId) + ") on element smileyId.")
        param1.write_var_short(self.smileyId)

    def deserialize(self, param1):
        self.deserializeAs_ShortcutSmiley(param1)

    def deserializeAs_ShortcutSmiley(self, param1):
        super().deserialize(param1)
        self._smileyIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ShortcutSmiley(param1)

    def deserializeAsyncAs_ShortcutSmiley(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._smileyIdFunc)

    def _smileyIdFunc(self, param1):
        self.smileyId = param1.read_var_uh_short()
        if self.smileyId < 0:
            raise RuntimeError("Forbidden value (" + str(self.smileyId) + ") on element of ShortcutSmiley.smileyId.")


class ShortcutSpell(Shortcut):
    protocolId = 368

    def __init__(self):
        super().__init__()
        self.spellId = 0

    def getTypeId(self):
        return 368

    def initShortcutSpell(self, param1=0, param2=0):
        super().initShortcut(param1)
        self.spellId = param2
        return self

    def reset(self):
        super().reset()
        self.spellId = 0

    def serialize(self, param1):
        self.serializeAs_ShortcutSpell(param1)

    def serializeAs_ShortcutSpell(self, param1):
        super().serializeAs_Shortcut(param1)
        if self.spellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element spellId.")
        param1.write_var_short(self.spellId)

    def deserialize(self, param1):
        self.deserializeAs_ShortcutSpell(param1)

    def deserializeAs_ShortcutSpell(self, param1):
        super().deserialize(param1)
        self._spellIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ShortcutSpell(param1)

    def deserializeAsyncAs_ShortcutSpell(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._spellIdFunc)

    def _spellIdFunc(self, param1):
        self.spellId = param1.read_var_uh_short()
        if self.spellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of ShortcutSpell.spellId.")


class GuildInAllianceVersatileInformations(GuildVersatileInformations):
    protocolId = 437

    def __init__(self):
        super().__init__()
        self.allianceId = 0

    def getTypeId(self):
        return 437

    def initGuildInAllianceVersatileInformations(self, param1=0, param2=0, param3=0, param4=0, param5=0):
        super().initGuildVersatileInformations(param1,param2,param3,param4)
        self.allianceId = param5
        return self

    def reset(self):
        super().reset()
        self.allianceId = 0

    def serialize(self, param1):
        self.serializeAs_GuildInAllianceVersatileInformations(param1)

    def serializeAs_GuildInAllianceVersatileInformations(self, param1):
        super().serializeAs_GuildVersatileInformations(param1)
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element allianceId.")
        param1.write_var_int(self.allianceId)

    def deserialize(self, param1):
        self.deserializeAs_GuildInAllianceVersatileInformations(param1)

    def deserializeAs_GuildInAllianceVersatileInformations(self, param1):
        super().deserialize(param1)
        self._allianceIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GuildInAllianceVersatileInformations(param1)

    def deserializeAsyncAs_GuildInAllianceVersatileInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._allianceIdFunc)

    def _allianceIdFunc(self, param1):
        self.allianceId = param1.read_var_uh_int()
        if self.allianceId < 0:
            raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element of GuildInAllianceVersatileInformations.allianceId.")


class VersionExtended(Version):
    protocolId = 393

    def __init__(self):
        super().__init__()
        self.install = 0
        self.technology = 0

    def getTypeId(self):
        return 393

    def initVersionExtended(self, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0, param8=0):
        super().initVersion(param1,param2,param3,param4,param5,param6)
        self.install = param7
        self.technology = param8
        return self

    def reset(self):
        super().reset()
        self.install = 0
        self.technology = 0

    def serialize(self, param1):
        self.serializeAs_VersionExtended(param1)

    def serializeAs_VersionExtended(self, param1):
        super().serializeAs_Version(param1)
        param1.write_byte(self.install)
        param1.write_byte(self.technology)

    def deserialize(self, param1):
        self.deserializeAs_VersionExtended(param1)

    def deserializeAs_VersionExtended(self, param1):
        super().deserialize(param1)
        self._installFunc(param1)
        self._technologyFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_VersionExtended(param1)

    def deserializeAsyncAs_VersionExtended(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._installFunc)
        param1.add_child(self._technologyFunc)

    def _installFunc(self, param1):
        self.install = param1.read_byte()
        if self.install < 0:
            raise RuntimeError("Forbidden value (" + str(self.install) + ") on element of VersionExtended.install.")

    def _technologyFunc(self, param1):
        self.technology = param1.read_byte()
        if self.technology < 0:
            raise RuntimeError("Forbidden value (" + str(self.technology) + ") on element of VersionExtended.technology.")


class FightTemporaryBoostStateEffect(FightTemporaryBoostEffect):
    protocolId = 214

    def __init__(self):
        super().__init__()
        self.stateId = 0

    def getTypeId(self):
        return 214

    def initFightTemporaryBoostStateEffect(self, param1=0, param2=0, param3=0, param4=1, param5=0, param6=0, param7=0, param8=0, param9=0):
        super().initFightTemporaryBoostEffect(param1,param2,param3,param4,param5,param6,param7,param8)
        self.stateId = param9
        return self

    def reset(self):
        super().reset()
        self.stateId = 0

    def serialize(self, param1):
        self.serializeAs_FightTemporaryBoostStateEffect(param1)

    def serializeAs_FightTemporaryBoostStateEffect(self, param1):
        super().serializeAs_FightTemporaryBoostEffect(param1)
        param1.write_short(self.stateId)

    def deserialize(self, param1):
        self.deserializeAs_FightTemporaryBoostStateEffect(param1)

    def deserializeAs_FightTemporaryBoostStateEffect(self, param1):
        super().deserialize(param1)
        self._stateIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTemporaryBoostStateEffect(param1)

    def deserializeAsyncAs_FightTemporaryBoostStateEffect(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._stateIdFunc)

    def _stateIdFunc(self, param1):
        self.stateId = param1.read_short()


class FightTemporaryBoostWeaponDamagesEffect(FightTemporaryBoostEffect):
    protocolId = 211

    def __init__(self):
        super().__init__()
        self.weaponTypeId = 0

    def getTypeId(self):
        return 211

    def initFightTemporaryBoostWeaponDamagesEffect(self, param1=0, param2=0, param3=0, param4=1, param5=0, param6=0, param7=0, param8=0, param9=0):
        super().initFightTemporaryBoostEffect(param1,param2,param3,param4,param5,param6,param7,param8)
        self.weaponTypeId = param9
        return self

    def reset(self):
        super().reset()
        self.weaponTypeId = 0

    def serialize(self, param1):
        self.serializeAs_FightTemporaryBoostWeaponDamagesEffect(param1)

    def serializeAs_FightTemporaryBoostWeaponDamagesEffect(self, param1):
        super().serializeAs_FightTemporaryBoostEffect(param1)
        param1.write_short(self.weaponTypeId)

    def deserialize(self, param1):
        self.deserializeAs_FightTemporaryBoostWeaponDamagesEffect(param1)

    def deserializeAs_FightTemporaryBoostWeaponDamagesEffect(self, param1):
        super().deserialize(param1)
        self._weaponTypeIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTemporaryBoostWeaponDamagesEffect(param1)

    def deserializeAsyncAs_FightTemporaryBoostWeaponDamagesEffect(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._weaponTypeIdFunc)

    def _weaponTypeIdFunc(self, param1):
        self.weaponTypeId = param1.read_short()


class FightTemporarySpellBoostEffect(FightTemporaryBoostEffect):
    protocolId = 207

    def __init__(self):
        super().__init__()
        self.boostedSpellId = 0

    def getTypeId(self):
        return 207

    def initFightTemporarySpellBoostEffect(self, param1=0, param2=0, param3=0, param4=1, param5=0, param6=0, param7=0, param8=0, param9=0):
        super().initFightTemporaryBoostEffect(param1,param2,param3,param4,param5,param6,param7,param8)
        self.boostedSpellId = param9
        return self

    def reset(self):
        super().reset()
        self.boostedSpellId = 0

    def serialize(self, param1):
        self.serializeAs_FightTemporarySpellBoostEffect(param1)

    def serializeAs_FightTemporarySpellBoostEffect(self, param1):
        super().serializeAs_FightTemporaryBoostEffect(param1)
        if self.boostedSpellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.boostedSpellId) + ") on element boostedSpellId.")
        param1.write_var_short(self.boostedSpellId)

    def deserialize(self, param1):
        self.deserializeAs_FightTemporarySpellBoostEffect(param1)

    def deserializeAs_FightTemporarySpellBoostEffect(self, param1):
        super().deserialize(param1)
        self._boostedSpellIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTemporarySpellBoostEffect(param1)

    def deserializeAsyncAs_FightTemporarySpellBoostEffect(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._boostedSpellIdFunc)

    def _boostedSpellIdFunc(self, param1):
        self.boostedSpellId = param1.read_var_uh_short()
        if self.boostedSpellId < 0:
            raise RuntimeError("Forbidden value (" + str(self.boostedSpellId) + ") on element of FightTemporarySpellBoostEffect.boostedSpellId.")


class CharacterMinimalInformations(CharacterBasicMinimalInformations):
    protocolId = 110

    def __init__(self):
        super().__init__()
        self.level = 0

    def getTypeId(self):
        return 110

    def initCharacterMinimalInformations(self, param1=0, param2="", param3=0):
        super().initCharacterBasicMinimalInformations(param1,param2)
        self.level = param3
        return self

    def reset(self):
        super().reset()
        self.level = 0

    def serialize(self, param1):
        self.serializeAs_CharacterMinimalInformations(param1)

    def serializeAs_CharacterMinimalInformations(self, param1):
        super().serializeAs_CharacterBasicMinimalInformations(param1)
        if self.level < 1 or self.level > 206:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)

    def deserialize(self, param1):
        self.deserializeAs_CharacterMinimalInformations(param1)

    def deserializeAs_CharacterMinimalInformations(self, param1):
        super().deserialize(param1)
        self._levelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterMinimalInformations(param1)

    def deserializeAsyncAs_CharacterMinimalInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._levelFunc)

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 1 or self.level > 206:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of CharacterMinimalInformations.level.")


class CharacterToRecolorInformation(AbstractCharacterToRefurbishInformation):
    protocolId = 212

    def getTypeId(self):
        return 212

    def initCharacterToRecolorInformation(self, param1=0, param2=[], param3=0):
        super().initAbstractCharacterToRefurbishInformation(param1,param2,param3)
        return self

    def reset(self):
        super().reset()

    def serialize(self, param1):
        self.serializeAs_CharacterToRecolorInformation(param1)

    def serializeAs_CharacterToRecolorInformation(self, param1):
        super().serializeAs_AbstractCharacterToRefurbishInformation(param1)

    def deserialize(self, param1):
        self.deserializeAs_CharacterToRecolorInformation(param1)

    def deserializeAs_CharacterToRecolorInformation(self, param1):
        super().deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterToRecolorInformation(param1)

    def deserializeAsyncAs_CharacterToRecolorInformation(self, param1):
        super().deserializeAsync(param1)


class CharacterToRelookInformation(AbstractCharacterToRefurbishInformation):
    protocolId = 399

    def getTypeId(self):
        return 399

    def initCharacterToRelookInformation(self, param1=0, param2=[], param3=0):
        super().initAbstractCharacterToRefurbishInformation(param1,param2,param3)
        return self

    def reset(self):
        super().reset()

    def serialize(self, param1):
        self.serializeAs_CharacterToRelookInformation(param1)

    def serializeAs_CharacterToRelookInformation(self, param1):
        super().serializeAs_AbstractCharacterToRefurbishInformation(param1)

    def deserialize(self, param1):
        self.deserializeAs_CharacterToRelookInformation(param1)

    def deserializeAs_CharacterToRelookInformation(self, param1):
        super().deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterToRelookInformation(param1)

    def deserializeAsyncAs_CharacterToRelookInformation(self, param1):
        super().deserializeAsync(param1)


class CharacterToRemodelInformations(CharacterRemodelingInformation):
    protocolId = 477

    def __init__(self):
        super().__init__()
        self.possibleChangeMask = 0
        self.mandatoryChangeMask = 0

    def getTypeId(self):
        return 477

    def initCharacterToRemodelInformations(self, param1=0, param2="", param3=0, param4=False, param5=0, param6=[], param7=0, param8=0):
        super().initCharacterRemodelingInformation(param1,param2,param3,param4,param5,param6)
        self.possibleChangeMask = param7
        self.mandatoryChangeMask = param8
        return self

    def reset(self):
        super().reset()
        self.possibleChangeMask = 0
        self.mandatoryChangeMask = 0

    def serialize(self, param1):
        self.serializeAs_CharacterToRemodelInformations(param1)

    def serializeAs_CharacterToRemodelInformations(self, param1):
        super().serializeAs_CharacterRemodelingInformation(param1)
        if self.possibleChangeMask < 0:
            raise RuntimeError("Forbidden value (" + str(self.possibleChangeMask) + ") on element possibleChangeMask.")
        param1.write_byte(self.possibleChangeMask)
        if self.mandatoryChangeMask < 0:
            raise RuntimeError("Forbidden value (" + str(self.mandatoryChangeMask) + ") on element mandatoryChangeMask.")
        param1.write_byte(self.mandatoryChangeMask)

    def deserialize(self, param1):
        self.deserializeAs_CharacterToRemodelInformations(param1)

    def deserializeAs_CharacterToRemodelInformations(self, param1):
        super().deserialize(param1)
        self._possibleChangeMaskFunc(param1)
        self._mandatoryChangeMaskFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterToRemodelInformations(param1)

    def deserializeAsyncAs_CharacterToRemodelInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._possibleChangeMaskFunc)
        param1.add_child(self._mandatoryChangeMaskFunc)

    def _possibleChangeMaskFunc(self, param1):
        self.possibleChangeMask = param1.read_byte()
        if self.possibleChangeMask < 0:
            raise RuntimeError("Forbidden value (" + str(self.possibleChangeMask) + ") on element of CharacterToRemodelInformations.possibleChangeMask.")

    def _mandatoryChangeMaskFunc(self, param1):
        self.mandatoryChangeMask = param1.read_byte()
        if self.mandatoryChangeMask < 0:
            raise RuntimeError("Forbidden value (" + str(self.mandatoryChangeMask) + ") on element of CharacterToRemodelInformations.mandatoryChangeMask.")


class GameRolePlayTaxCollectorInformations(GameRolePlayActorInformations):
    protocolId = 148

    def __init__(self):
        super().__init__()
        self.identification = TaxCollectorStaticInformations()
        self.guildLevel = 0
        self.taxCollectorAttack = 0
        self._identificationtree = FuncTree()

    def getTypeId(self):
        return 148

    def initGameRolePlayTaxCollectorInformations(self, param1=0, param2=None, param3=None, param4=None, param5=0, param6=0):
        super().initGameRolePlayActorInformations(param1,param2,param3)
        self.identification = param4
        self.guildLevel = param5
        self.taxCollectorAttack = param6
        return self

    def reset(self):
        super().reset()
        self.identification = TaxCollectorStaticInformations()
        self.taxCollectorAttack = 0

    def serialize(self, param1):
        self.serializeAs_GameRolePlayTaxCollectorInformations(param1)

    def serializeAs_GameRolePlayTaxCollectorInformations(self, param1):
        super().serializeAs_GameRolePlayActorInformations(param1)
        param1.write_short(self.identification.getTypeId())
        self.identification.serialize(param1)
        if self.guildLevel < 0 or self.guildLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.guildLevel) + ") on element guildLevel.")
        param1.write_byte(self.guildLevel)
        param1.write_int(self.taxCollectorAttack)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayTaxCollectorInformations(param1)

    def deserializeAs_GameRolePlayTaxCollectorInformations(self, param1):
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        self.identification = ProtocolTypeManager.get_instance(TaxCollectorStaticInformations,_loc2_)
        self.identification.deserialize(param1)
        self._guildLevelFunc(param1)
        self._taxCollectorAttackFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayTaxCollectorInformations(param1)

    def deserializeAsyncAs_GameRolePlayTaxCollectorInformations(self, param1):
        super().deserializeAsync(param1)
        self._identificationtree = param1.add_child(self._identificationtreeFunc)
        param1.add_child(self._guildLevelFunc)
        param1.add_child(self._taxCollectorAttackFunc)

    def _identificationtreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.identification = ProtocolTypeManager.get_instance(TaxCollectorStaticInformations,_loc2_)
        self.identification.deserializeAsync(self._identificationtree)

    def _guildLevelFunc(self, param1):
        self.guildLevel = param1.read_unsigned_byte()
        if self.guildLevel < 0 or self.guildLevel > 255:
            raise RuntimeError("Forbidden value (" + str(self.guildLevel) + ") on element of GameRolePlayTaxCollectorInformations.guildLevel.")

    def _taxCollectorAttackFunc(self, param1):
        self.taxCollectorAttack = param1.read_int()


class MapCoordinatesExtended(MapCoordinatesAndId):
    protocolId = 176

    def __init__(self):
        super().__init__()
        self.subAreaId = 0

    def getTypeId(self):
        return 176

    def initMapCoordinatesExtended(self, param1=0, param2=0, param3=0, param4=0):
        super().initMapCoordinatesAndId(param1,param2,param3)
        self.subAreaId = param4
        return self

    def reset(self):
        super().reset()
        self.subAreaId = 0

    def serialize(self, param1):
        self.serializeAs_MapCoordinatesExtended(param1)

    def serializeAs_MapCoordinatesExtended(self, param1):
        super().serializeAs_MapCoordinatesAndId(param1)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)

    def deserialize(self, param1):
        self.deserializeAs_MapCoordinatesExtended(param1)

    def deserializeAs_MapCoordinatesExtended(self, param1):
        super().deserialize(param1)
        self._subAreaIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_MapCoordinatesExtended(param1)

    def deserializeAsyncAs_MapCoordinatesExtended(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._subAreaIdFunc)

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of MapCoordinatesExtended.subAreaId.")


class FightAllianceTeamInformations(FightTeamInformations):
    protocolId = 439

    def __init__(self):
        super().__init__()
        self.relation = 0

    def getTypeId(self):
        return 439

    def initFightAllianceTeamInformations(self, param1=2, param2=0, param3=0, param4=0, param5=0, param6=[], param7=0):
        super().initFightTeamInformations(param1,param2,param3,param4,param5,param6)
        self.relation = param7
        return self

    def reset(self):
        super().reset()
        self.relation = 0

    def serialize(self, param1):
        self.serializeAs_FightAllianceTeamInformations(param1)

    def serializeAs_FightAllianceTeamInformations(self, param1):
        super().serializeAs_FightTeamInformations(param1)
        param1.write_byte(self.relation)

    def deserialize(self, param1):
        self.deserializeAs_FightAllianceTeamInformations(param1)

    def deserializeAs_FightAllianceTeamInformations(self, param1):
        super().deserialize(param1)
        self._relationFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightAllianceTeamInformations(param1)

    def deserializeAsyncAs_FightAllianceTeamInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._relationFunc)

    def _relationFunc(self, param1):
        self.relation = param1.read_byte()
        if self.relation < 0:
            raise RuntimeError("Forbidden value (" + str(self.relation) + ") on element of FightAllianceTeamInformations.relation.")


class FightResultMutantListEntry(FightResultFighterListEntry):
    protocolId = 216

    def __init__(self):
        super().__init__()
        self.level = 0

    def getTypeId(self):
        return 216

    def initFightResultMutantListEntry(self, param1=0, param2=0, param3=None, param4=0, param5=False, param6=0):
        super().initFightResultFighterListEntry(param1,param2,param3,param4,param5)
        self.level = param6
        return self

    def reset(self):
        super().reset()
        self.level = 0

    def serialize(self, param1):
        self.serializeAs_FightResultMutantListEntry(param1)

    def serializeAs_FightResultMutantListEntry(self, param1):
        super().serializeAs_FightResultFighterListEntry(param1)
        if self.level < 0:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_var_short(self.level)

    def deserialize(self, param1):
        self.deserializeAs_FightResultMutantListEntry(param1)

    def deserializeAs_FightResultMutantListEntry(self, param1):
        super().deserialize(param1)
        self._levelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightResultMutantListEntry(param1)

    def deserializeAsyncAs_FightResultMutantListEntry(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._levelFunc)

    def _levelFunc(self, param1):
        self.level = param1.read_var_uh_short()
        if self.level < 0:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightResultMutantListEntry.level.")


class FightResultPlayerListEntry(FightResultFighterListEntry):
    protocolId = 24

    def __init__(self):
        super().__init__()
        self.level = 0
        self.additional = []
        self._additionaltree = FuncTree()

    def getTypeId(self):
        return 24

    def initFightResultPlayerListEntry(self, param1=0, param2=0, param3=None, param4=0, param5=False, param6=0, param7=[]):
        super().initFightResultFighterListEntry(param1,param2,param3,param4,param5)
        self.level = param6
        self.additional = param7
        return self

    def reset(self):
        super().reset()
        self.level = 0
        self.additional = []

    def serialize(self, param1):
        self.serializeAs_FightResultPlayerListEntry(param1)

    def serializeAs_FightResultPlayerListEntry(self, param1):
        super().serializeAs_FightResultFighterListEntry(param1)
        if self.level < 1 or self.level > 206:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)
        param1.write_short(len(self.additional))
        _loc2_ = 0
        while _loc2_ < len(self.additional):
            param1.write_short(as_parent(self.additional[_loc2_], FightResultAdditionalData).getTypeId())
            as_parent(self.additional[_loc2_], FightResultAdditionalData).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_FightResultPlayerListEntry(param1)

    def deserializeAs_FightResultPlayerListEntry(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._levelFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(FightResultAdditionalData,_loc4_)
            _loc5_.deserialize(param1)
            self.additional.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightResultPlayerListEntry(param1)

    def deserializeAsyncAs_FightResultPlayerListEntry(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._levelFunc)
        self._additionaltree = param1.add_child(self._additionaltreeFunc)

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 1 or self.level > 206:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightResultPlayerListEntry.level.")

    def _additionaltreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._additionaltree.add_child(self._additionalFunc)
            _loc3_ += 1

    def _additionalFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(FightResultAdditionalData,_loc2_)
        _loc3_.deserialize(param1)
        self.additional.append(_loc3_)


class FightResultTaxCollectorListEntry(FightResultFighterListEntry):
    protocolId = 84

    def __init__(self):
        super().__init__()
        self.level = 0
        self.guildInfo = BasicGuildInformations()
        self.experienceForGuild = 0
        self._guildInfotree = FuncTree()

    def getTypeId(self):
        return 84

    def initFightResultTaxCollectorListEntry(self, param1=0, param2=0, param3=None, param4=0, param5=False, param6=0, param7=None, param8=0):
        super().initFightResultFighterListEntry(param1,param2,param3,param4,param5)
        self.level = param6
        self.guildInfo = param7
        self.experienceForGuild = param8
        return self

    def reset(self):
        super().reset()
        self.level = 0
        self.guildInfo = BasicGuildInformations()

    def serialize(self, param1):
        self.serializeAs_FightResultTaxCollectorListEntry(param1)

    def serializeAs_FightResultTaxCollectorListEntry(self, param1):
        super().serializeAs_FightResultFighterListEntry(param1)
        if self.level < 1 or self.level > 200:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)
        self.guildInfo.serializeAs_BasicGuildInformations(param1)
        param1.write_int(self.experienceForGuild)

    def deserialize(self, param1):
        self.deserializeAs_FightResultTaxCollectorListEntry(param1)

    def deserializeAs_FightResultTaxCollectorListEntry(self, param1):
        super().deserialize(param1)
        self._levelFunc(param1)
        self.guildInfo = BasicGuildInformations()
        self.guildInfo.deserialize(param1)
        self._experienceForGuildFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightResultTaxCollectorListEntry(param1)

    def deserializeAsyncAs_FightResultTaxCollectorListEntry(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._levelFunc)
        self._guildInfotree = param1.add_child(self._guildInfotreeFunc)
        param1.add_child(self._experienceForGuildFunc)

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 1 or self.level > 200:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightResultTaxCollectorListEntry.level.")

    def _guildInfotreeFunc(self, param1):
        self.guildInfo = BasicGuildInformations()
        self.guildInfo.deserializeAsync(self._guildInfotree)

    def _experienceForGuildFunc(self, param1):
        self.experienceForGuild = param1.read_int()


class FightTeamMemberWithAllianceCharacterInformations(FightTeamMemberCharacterInformations):
    protocolId = 426

    def __init__(self):
        super().__init__()
        self.allianceInfos = BasicAllianceInformations()
        self._allianceInfostree = FuncTree()

    def getTypeId(self):
        return 426

    def initFightTeamMemberWithAllianceCharacterInformations(self, param1=0, param2="", param3=0, param4=None):
        super().initFightTeamMemberCharacterInformations(param1,param2,param3)
        self.allianceInfos = param4
        return self

    def reset(self):
        super().reset()
        self.allianceInfos = BasicAllianceInformations()

    def serialize(self, param1):
        self.serializeAs_FightTeamMemberWithAllianceCharacterInformations(param1)

    def serializeAs_FightTeamMemberWithAllianceCharacterInformations(self, param1):
        super().serializeAs_FightTeamMemberCharacterInformations(param1)
        self.allianceInfos.serializeAs_BasicAllianceInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_FightTeamMemberWithAllianceCharacterInformations(param1)

    def deserializeAs_FightTeamMemberWithAllianceCharacterInformations(self, param1):
        super().deserialize(param1)
        self.allianceInfos = BasicAllianceInformations()
        self.allianceInfos.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FightTeamMemberWithAllianceCharacterInformations(param1)

    def deserializeAsyncAs_FightTeamMemberWithAllianceCharacterInformations(self, param1):
        super().deserializeAsync(param1)
        self._allianceInfostree = param1.add_child(self._allianceInfostreeFunc)

    def _allianceInfostreeFunc(self, param1):
        self.allianceInfos = BasicAllianceInformations()
        self.allianceInfos.deserializeAsync(self._allianceInfostree)


class GameFightAIInformations(GameFightFighterInformations):
    protocolId = 151

    def getTypeId(self):
        return 151

    def initGameFightAIInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[]):
        super().initGameFightFighterInformations(param1,param2,param3,param4,param5,param6,param7,param8)
        return self

    def reset(self):
        super().reset()

    def serialize(self, param1):
        self.serializeAs_GameFightAIInformations(param1)

    def serializeAs_GameFightAIInformations(self, param1):
        super().serializeAs_GameFightFighterInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameFightAIInformations(param1)

    def deserializeAs_GameFightAIInformations(self, param1):
        super().deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightAIInformations(param1)

    def deserializeAsyncAs_GameFightAIInformations(self, param1):
        super().deserializeAsync(param1)


class GameFightCompanionInformations(GameFightFighterInformations):
    protocolId = 450

    def __init__(self):
        super().__init__()
        self.companionGenericId = 0
        self.level = 0
        self.masterId = 0

    def getTypeId(self):
        return 450

    def initGameFightCompanionInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[], param9=0, param10=0, param11=0):
        super().initGameFightFighterInformations(param1,param2,param3,param4,param5,param6,param7,param8)
        self.companionGenericId = param9
        self.level = param10
        self.masterId = param11
        return self

    def reset(self):
        super().reset()
        self.companionGenericId = 0
        self.level = 0
        self.masterId = 0

    def serialize(self, param1):
        self.serializeAs_GameFightCompanionInformations(param1)

    def serializeAs_GameFightCompanionInformations(self, param1):
        super().serializeAs_GameFightFighterInformations(param1)
        if self.companionGenericId < 0:
            raise RuntimeError("Forbidden value (" + str(self.companionGenericId) + ") on element companionGenericId.")
        param1.write_byte(self.companionGenericId)
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)
        if self.masterId < -9007199254740990 or self.masterId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element masterId.")
        param1.write_double(self.masterId)

    def deserialize(self, param1):
        self.deserializeAs_GameFightCompanionInformations(param1)

    def deserializeAs_GameFightCompanionInformations(self, param1):
        super().deserialize(param1)
        self._companionGenericIdFunc(param1)
        self._levelFunc(param1)
        self._masterIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightCompanionInformations(param1)

    def deserializeAsyncAs_GameFightCompanionInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._companionGenericIdFunc)
        param1.add_child(self._levelFunc)
        param1.add_child(self._masterIdFunc)

    def _companionGenericIdFunc(self, param1):
        self.companionGenericId = param1.read_byte()
        if self.companionGenericId < 0:
            raise RuntimeError("Forbidden value (" + str(self.companionGenericId) + ") on element of GameFightCompanionInformations.companionGenericId.")

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of GameFightCompanionInformations.level.")

    def _masterIdFunc(self, param1):
        self.masterId = param1.read_double()
        if self.masterId < -9007199254740990 or self.masterId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.masterId) + ") on element of GameFightCompanionInformations.masterId.")


class GameFightFighterNamedInformations(GameFightFighterInformations):
    protocolId = 158

    def __init__(self):
        super().__init__()
        self.name = ""
        self.status = PlayerStatus()
        self._statustree = FuncTree()

    def getTypeId(self):
        return 158

    def initGameFightFighterNamedInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[], param9="", param10=None):
        super().initGameFightFighterInformations(param1,param2,param3,param4,param5,param6,param7,param8)
        self.name = param9
        self.status = param10
        return self

    def reset(self):
        super().reset()
        self.name = ""
        self.status = PlayerStatus()

    def serialize(self, param1):
        self.serializeAs_GameFightFighterNamedInformations(param1)

    def serializeAs_GameFightFighterNamedInformations(self, param1):
        super().serializeAs_GameFightFighterInformations(param1)
        param1.write_utf(self.name)
        self.status.serializeAs_PlayerStatus(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameFightFighterNamedInformations(param1)

    def deserializeAs_GameFightFighterNamedInformations(self, param1):
        super().deserialize(param1)
        self._nameFunc(param1)
        self.status = PlayerStatus()
        self.status.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightFighterNamedInformations(param1)

    def deserializeAsyncAs_GameFightFighterNamedInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nameFunc)
        self._statustree = param1.add_child(self._statustreeFunc)

    def _nameFunc(self, param1):
        self.name = param1.read_utf()

    def _statustreeFunc(self, param1):
        self.status = PlayerStatus()
        self.status.deserializeAsync(self._statustree)


class BasicNamedAllianceInformations(BasicAllianceInformations):
    protocolId = 418

    def __init__(self):
        super().__init__()
        self.allianceName = ""

    def getTypeId(self):
        return 418

    def initBasicNamedAllianceInformations(self, param1=0, param2="", param3=""):
        super().initBasicAllianceInformations(param1,param2)
        self.allianceName = param3
        return self

    def reset(self):
        super().reset()
        self.allianceName = ""

    def serialize(self, param1):
        self.serializeAs_BasicNamedAllianceInformations(param1)

    def serializeAs_BasicNamedAllianceInformations(self, param1):
        super().serializeAs_BasicAllianceInformations(param1)
        param1.write_utf(self.allianceName)

    def deserialize(self, param1):
        self.deserializeAs_BasicNamedAllianceInformations(param1)

    def deserializeAs_BasicNamedAllianceInformations(self, param1):
        super().deserialize(param1)
        self._allianceNameFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_BasicNamedAllianceInformations(param1)

    def deserializeAsyncAs_BasicNamedAllianceInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._allianceNameFunc)

    def _allianceNameFunc(self, param1):
        self.allianceName = param1.read_utf()


class GameRolePlayGroupMonsterInformations(GameRolePlayActorInformations):
    protocolId = 160

    def __init__(self):
        super().__init__()
        self.staticInfos = GroupMonsterStaticInformations()
        self.creationTime = 0
        self.ageBonusRate = 0
        self.lootShare = 0
        self.alignmentSide = 0
        self.keyRingBonus = False
        self.hasHardcoreDrop = False
        self.hasAVARewardToken = False
        self._staticInfostree = FuncTree()

    def getTypeId(self):
        return 160

    def initGameRolePlayGroupMonsterInformations(self, param1=0, param2=None, param3=None, param4=None, param5=0, param6=0, param7=0, param8=0, param9=False, param10=False, param11=False):
        super().initGameRolePlayActorInformations(param1,param2,param3)
        self.staticInfos = param4
        self.creationTime = param5
        self.ageBonusRate = param6
        self.lootShare = param7
        self.alignmentSide = param8
        self.keyRingBonus = param9
        self.hasHardcoreDrop = param10
        self.hasAVARewardToken = param11
        return self

    def reset(self):
        super().reset()
        self.staticInfos = GroupMonsterStaticInformations()
        self.ageBonusRate = 0
        self.lootShare = 0
        self.alignmentSide = 0
        self.keyRingBonus = False
        self.hasHardcoreDrop = False
        self.hasAVARewardToken = False

    def serialize(self, param1):
        self.serializeAs_GameRolePlayGroupMonsterInformations(param1)

    def serializeAs_GameRolePlayGroupMonsterInformations(self, param1):
        super().serializeAs_GameRolePlayActorInformations(param1)
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.keyRingBonus)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.hasHardcoreDrop)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,2,self.hasAVARewardToken)
        param1.write_byte(_loc2_)
        param1.write_short(self.staticInfos.getTypeId())
        self.staticInfos.serialize(param1)
        if self.creationTime < 0 or self.creationTime > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.creationTime) + ") on element creationTime.")
        param1.write_double(self.creationTime)
        if self.ageBonusRate < 0:
            raise RuntimeError("Forbidden value (" + str(self.ageBonusRate) + ") on element ageBonusRate.")
        param1.write_int(self.ageBonusRate)
        if self.lootShare < -1 or self.lootShare > 8:
            raise RuntimeError("Forbidden value (" + str(self.lootShare) + ") on element lootShare.")
        param1.write_byte(self.lootShare)
        param1.write_byte(self.alignmentSide)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayGroupMonsterInformations(param1)

    def deserializeAs_GameRolePlayGroupMonsterInformations(self, param1):
        super().deserialize(param1)
        self.deserializeByteBoxes(param1)
        _loc2_ = param1.read_unsigned_short()
        self.staticInfos = ProtocolTypeManager.get_instance(GroupMonsterStaticInformations,_loc2_)
        self.staticInfos.deserialize(param1)
        self._creationTimeFunc(param1)
        self._ageBonusRateFunc(param1)
        self._lootShareFunc(param1)
        self._alignmentSideFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayGroupMonsterInformations(param1)

    def deserializeAsyncAs_GameRolePlayGroupMonsterInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self.deserializeByteBoxes)
        self._staticInfostree = param1.add_child(self._staticInfostreeFunc)
        param1.add_child(self._creationTimeFunc)
        param1.add_child(self._ageBonusRateFunc)
        param1.add_child(self._lootShareFunc)
        param1.add_child(self._alignmentSideFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.keyRingBonus = BooleanByteWrapper.get_flag(_loc2_,0)
        self.hasHardcoreDrop = BooleanByteWrapper.get_flag(_loc2_,1)
        self.hasAVARewardToken = BooleanByteWrapper.get_flag(_loc2_,2)

    def _staticInfostreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.staticInfos = ProtocolTypeManager.get_instance(GroupMonsterStaticInformations,_loc2_)
        self.staticInfos.deserializeAsync(self._staticInfostree)

    def _creationTimeFunc(self, param1):
        self.creationTime = param1.read_double()
        if self.creationTime < 0 or self.creationTime > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.creationTime) + ") on element of GameRolePlayGroupMonsterInformations.creationTime.")

    def _ageBonusRateFunc(self, param1):
        self.ageBonusRate = param1.read_int()
        if self.ageBonusRate < 0:
            raise RuntimeError("Forbidden value (" + str(self.ageBonusRate) + ") on element of GameRolePlayGroupMonsterInformations.ageBonusRate.")

    def _lootShareFunc(self, param1):
        self.lootShare = param1.read_byte()
        if self.lootShare < -1 or self.lootShare > 8:
            raise RuntimeError("Forbidden value (" + str(self.lootShare) + ") on element of GameRolePlayGroupMonsterInformations.lootShare.")

    def _alignmentSideFunc(self, param1):
        self.alignmentSide = param1.read_byte()


class GameRolePlayNamedActorInformations(GameRolePlayActorInformations):
    protocolId = 154

    def __init__(self):
        super().__init__()
        self.name = ""

    def getTypeId(self):
        return 154

    def initGameRolePlayNamedActorInformations(self, param1=0, param2=None, param3=None, param4=""):
        super().initGameRolePlayActorInformations(param1,param2,param3)
        self.name = param4
        return self

    def reset(self):
        super().reset()
        self.name = ""

    def serialize(self, param1):
        self.serializeAs_GameRolePlayNamedActorInformations(param1)

    def serializeAs_GameRolePlayNamedActorInformations(self, param1):
        super().serializeAs_GameRolePlayActorInformations(param1)
        param1.write_utf(self.name)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayNamedActorInformations(param1)

    def deserializeAs_GameRolePlayNamedActorInformations(self, param1):
        super().deserialize(param1)
        self._nameFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayNamedActorInformations(param1)

    def deserializeAsyncAs_GameRolePlayNamedActorInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nameFunc)

    def _nameFunc(self, param1):
        self.name = param1.read_utf()


class GameRolePlayNpcInformations(GameRolePlayActorInformations):
    protocolId = 156

    def __init__(self):
        super().__init__()
        self.npcId = 0
        self.sex = False
        self.specialArtworkId = 0

    def getTypeId(self):
        return 156

    def initGameRolePlayNpcInformations(self, param1=0, param2=None, param3=None, param4=0, param5=False, param6=0):
        super().initGameRolePlayActorInformations(param1,param2,param3)
        self.npcId = param4
        self.sex = param5
        self.specialArtworkId = param6
        return self

    def reset(self):
        super().reset()
        self.npcId = 0
        self.sex = False
        self.specialArtworkId = 0

    def serialize(self, param1):
        self.serializeAs_GameRolePlayNpcInformations(param1)

    def serializeAs_GameRolePlayNpcInformations(self, param1):
        super().serializeAs_GameRolePlayActorInformations(param1)
        if self.npcId < 0:
            raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element npcId.")
        param1.write_var_short(self.npcId)
        param1.write_boolean(self.sex)
        if self.specialArtworkId < 0:
            raise RuntimeError("Forbidden value (" + str(self.specialArtworkId) + ") on element specialArtworkId.")
        param1.write_var_short(self.specialArtworkId)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayNpcInformations(param1)

    def deserializeAs_GameRolePlayNpcInformations(self, param1):
        super().deserialize(param1)
        self._npcIdFunc(param1)
        self._sexFunc(param1)
        self._specialArtworkIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayNpcInformations(param1)

    def deserializeAsyncAs_GameRolePlayNpcInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._npcIdFunc)
        param1.add_child(self._sexFunc)
        param1.add_child(self._specialArtworkIdFunc)

    def _npcIdFunc(self, param1):
        self.npcId = param1.read_var_uh_short()
        if self.npcId < 0:
            raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element of GameRolePlayNpcInformations.npcId.")

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()

    def _specialArtworkIdFunc(self, param1):
        self.specialArtworkId = param1.read_var_uh_short()
        if self.specialArtworkId < 0:
            raise RuntimeError("Forbidden value (" + str(self.specialArtworkId) + ") on element of GameRolePlayNpcInformations.specialArtworkId.")


class GameRolePlayPortalInformations(GameRolePlayActorInformations):
    protocolId = 467

    def __init__(self):
        super().__init__()
        self.portal = PortalInformation()
        self._portaltree = FuncTree()

    def getTypeId(self):
        return 467

    def initGameRolePlayPortalInformations(self, param1=0, param2=None, param3=None, param4=None):
        super().initGameRolePlayActorInformations(param1,param2,param3)
        self.portal = param4
        return self

    def reset(self):
        super().reset()
        self.portal = PortalInformation()

    def serialize(self, param1):
        self.serializeAs_GameRolePlayPortalInformations(param1)

    def serializeAs_GameRolePlayPortalInformations(self, param1):
        super().serializeAs_GameRolePlayActorInformations(param1)
        param1.write_short(self.portal.getTypeId())
        self.portal.serialize(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayPortalInformations(param1)

    def deserializeAs_GameRolePlayPortalInformations(self, param1):
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        self.portal = ProtocolTypeManager.get_instance(PortalInformation,_loc2_)
        self.portal.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayPortalInformations(param1)

    def deserializeAsyncAs_GameRolePlayPortalInformations(self, param1):
        super().deserializeAsync(param1)
        self._portaltree = param1.add_child(self._portaltreeFunc)

    def _portaltreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.portal = ProtocolTypeManager.get_instance(PortalInformation,_loc2_)
        self.portal.deserializeAsync(self._portaltree)


class GameRolePlayPrismInformations(GameRolePlayActorInformations):
    protocolId = 161

    def __init__(self):
        super().__init__()
        self.prism = PrismInformation()
        self._prismtree = FuncTree()

    def getTypeId(self):
        return 161

    def initGameRolePlayPrismInformations(self, param1=0, param2=None, param3=None, param4=None):
        super().initGameRolePlayActorInformations(param1,param2,param3)
        self.prism = param4
        return self

    def reset(self):
        super().reset()
        self.prism = PrismInformation()

    def serialize(self, param1):
        self.serializeAs_GameRolePlayPrismInformations(param1)

    def serializeAs_GameRolePlayPrismInformations(self, param1):
        super().serializeAs_GameRolePlayActorInformations(param1)
        param1.write_short(self.prism.getTypeId())
        self.prism.serialize(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayPrismInformations(param1)

    def deserializeAs_GameRolePlayPrismInformations(self, param1):
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        self.prism = ProtocolTypeManager.get_instance(PrismInformation,_loc2_)
        self.prism.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayPrismInformations(param1)

    def deserializeAsyncAs_GameRolePlayPrismInformations(self, param1):
        super().deserializeAsync(param1)
        self._prismtree = param1.add_child(self._prismtreeFunc)

    def _prismtreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.prism = ProtocolTypeManager.get_instance(PrismInformation,_loc2_)
        self.prism.deserializeAsync(self._prismtree)


class GameRolePlayTreasureHintInformations(GameRolePlayActorInformations):
    protocolId = 471

    def __init__(self):
        super().__init__()
        self.npcId = 0

    def getTypeId(self):
        return 471

    def initGameRolePlayTreasureHintInformations(self, param1=0, param2=None, param3=None, param4=0):
        super().initGameRolePlayActorInformations(param1,param2,param3)
        self.npcId = param4
        return self

    def reset(self):
        super().reset()
        self.npcId = 0

    def serialize(self, param1):
        self.serializeAs_GameRolePlayTreasureHintInformations(param1)

    def serializeAs_GameRolePlayTreasureHintInformations(self, param1):
        super().serializeAs_GameRolePlayActorInformations(param1)
        if self.npcId < 0:
            raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element npcId.")
        param1.write_var_short(self.npcId)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayTreasureHintInformations(param1)

    def deserializeAs_GameRolePlayTreasureHintInformations(self, param1):
        super().deserialize(param1)
        self._npcIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayTreasureHintInformations(param1)

    def deserializeAsyncAs_GameRolePlayTreasureHintInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._npcIdFunc)

    def _npcIdFunc(self, param1):
        self.npcId = param1.read_var_uh_short()
        if self.npcId < 0:
            raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element of GameRolePlayTreasureHintInformations.npcId.")


class GuildInformations(BasicGuildInformations):
    protocolId = 127

    def __init__(self):
        super().__init__()
        self.guildEmblem = GuildEmblem()
        self._guildEmblemtree = FuncTree()

    def getTypeId(self):
        return 127

    def initGuildInformations(self, param1=0, param2="", param3=0, param4=None):
        super().initBasicGuildInformations(param1,param2,param3)
        self.guildEmblem = param4
        return self

    def reset(self):
        super().reset()
        self.guildEmblem = GuildEmblem()

    def serialize(self, param1):
        self.serializeAs_GuildInformations(param1)

    def serializeAs_GuildInformations(self, param1):
        super().serializeAs_BasicGuildInformations(param1)
        self.guildEmblem.serializeAs_GuildEmblem(param1)

    def deserialize(self, param1):
        self.deserializeAs_GuildInformations(param1)

    def deserializeAs_GuildInformations(self, param1):
        super().deserialize(param1)
        self.guildEmblem = GuildEmblem()
        self.guildEmblem.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GuildInformations(param1)

    def deserializeAsyncAs_GuildInformations(self, param1):
        super().deserializeAsync(param1)
        self._guildEmblemtree = param1.add_child(self._guildEmblemtreeFunc)

    def _guildEmblemtreeFunc(self, param1):
        self.guildEmblem = GuildEmblem()
        self.guildEmblem.deserializeAsync(self._guildEmblemtree)


class ObjectItemGenericQuantityPrice(ObjectItemGenericQuantity):
    protocolId = 494

    def __init__(self):
        super().__init__()
        self.price = 0

    def getTypeId(self):
        return 494

    def initObjectItemGenericQuantityPrice(self, param1=0, param2=0, param3=0):
        super().initObjectItemGenericQuantity(param1,param2)
        self.price = param3
        return self

    def reset(self):
        super().reset()
        self.price = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemGenericQuantityPrice(param1)

    def serializeAs_ObjectItemGenericQuantityPrice(self, param1):
        super().serializeAs_ObjectItemGenericQuantity(param1)
        if self.price < 0 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element price.")
        param1.write_var_long(self.price)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemGenericQuantityPrice(param1)

    def deserializeAs_ObjectItemGenericQuantityPrice(self, param1):
        super().deserialize(param1)
        self._priceFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemGenericQuantityPrice(param1)

    def deserializeAsyncAs_ObjectItemGenericQuantityPrice(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._priceFunc)

    def _priceFunc(self, param1):
        self.price = param1.read_var_uh_long()
        if self.price < 0 or self.price > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of ObjectItemGenericQuantityPrice.price.")


class ObjectItemInformationWithQuantity(ObjectItemMinimalInformation):
    protocolId = 387

    def __init__(self):
        super().__init__()
        self.quantity = 0

    def getTypeId(self):
        return 387

    def initObjectItemInformationWithQuantity(self, param1=0, param2=[], param3=0):
        super().initObjectItemMinimalInformation(param1,param2)
        self.quantity = param3
        return self

    def reset(self):
        super().reset()
        self.quantity = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemInformationWithQuantity(param1)

    def serializeAs_ObjectItemInformationWithQuantity(self, param1):
        super().serializeAs_ObjectItemMinimalInformation(param1)
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element quantity.")
        param1.write_var_int(self.quantity)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemInformationWithQuantity(param1)

    def deserializeAs_ObjectItemInformationWithQuantity(self, param1):
        super().deserialize(param1)
        self._quantityFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemInformationWithQuantity(param1)

    def deserializeAsyncAs_ObjectItemInformationWithQuantity(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._quantityFunc)

    def _quantityFunc(self, param1):
        self.quantity = param1.read_var_uh_int()
        if self.quantity < 0:
            raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItemInformationWithQuantity.quantity.")


class ObjectItemToSellInBid(ObjectItemToSell):
    protocolId = 164

    def __init__(self):
        super().__init__()
        self.unsoldDelay = 0

    def getTypeId(self):
        return 164

    def initObjectItemToSellInBid(self, param1=0, param2=[], param3=0, param4=0, param5=0, param6=0):
        super().initObjectItemToSell(param1,param2,param3,param4,param5)
        self.unsoldDelay = param6
        return self

    def reset(self):
        super().reset()
        self.unsoldDelay = 0

    def serialize(self, param1):
        self.serializeAs_ObjectItemToSellInBid(param1)

    def serializeAs_ObjectItemToSellInBid(self, param1):
        super().serializeAs_ObjectItemToSell(param1)
        if self.unsoldDelay < 0:
            raise RuntimeError("Forbidden value (" + str(self.unsoldDelay) + ") on element unsoldDelay.")
        param1.write_int(self.unsoldDelay)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemToSellInBid(param1)

    def deserializeAs_ObjectItemToSellInBid(self, param1):
        super().deserialize(param1)
        self._unsoldDelayFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemToSellInBid(param1)

    def deserializeAsyncAs_ObjectItemToSellInBid(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._unsoldDelayFunc)

    def _unsoldDelayFunc(self, param1):
        self.unsoldDelay = param1.read_int()
        if self.unsoldDelay < 0:
            raise RuntimeError("Forbidden value (" + str(self.unsoldDelay) + ") on element of ObjectItemToSellInBid.unsoldDelay.")


class ObjectItemToSellInNpcShop(ObjectItemMinimalInformation):
    protocolId = 352

    def __init__(self):
        super().__init__()
        self.objectPrice = 0
        self.buyCriterion = ""

    def getTypeId(self):
        return 352

    def initObjectItemToSellInNpcShop(self, param1=0, param2=[], param3=0, param4=""):
        super().initObjectItemMinimalInformation(param1,param2)
        self.objectPrice = param3
        self.buyCriterion = param4
        return self

    def reset(self):
        super().reset()
        self.objectPrice = 0
        self.buyCriterion = ""

    def serialize(self, param1):
        self.serializeAs_ObjectItemToSellInNpcShop(param1)

    def serializeAs_ObjectItemToSellInNpcShop(self, param1):
        super().serializeAs_ObjectItemMinimalInformation(param1)
        if self.objectPrice < 0 or self.objectPrice > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.objectPrice) + ") on element objectPrice.")
        param1.write_var_long(self.objectPrice)
        param1.write_utf(self.buyCriterion)

    def deserialize(self, param1):
        self.deserializeAs_ObjectItemToSellInNpcShop(param1)

    def deserializeAs_ObjectItemToSellInNpcShop(self, param1):
        super().deserialize(param1)
        self._objectPriceFunc(param1)
        self._buyCriterionFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectItemToSellInNpcShop(param1)

    def deserializeAsyncAs_ObjectItemToSellInNpcShop(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._objectPriceFunc)
        param1.add_child(self._buyCriterionFunc)

    def _objectPriceFunc(self, param1):
        self.objectPrice = param1.read_var_uh_long()
        if self.objectPrice < 0 or self.objectPrice > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.objectPrice) + ") on element of ObjectItemToSellInNpcShop.objectPrice.")

    def _buyCriterionFunc(self, param1):
        self.buyCriterion = param1.read_utf()


class ObjectEffectLadder(ObjectEffectCreature):
    protocolId = 81

    def __init__(self):
        super().__init__()
        self.monsterCount = 0

    def getTypeId(self):
        return 81

    def initObjectEffectLadder(self, param1=0, param2=0, param3=0):
        super().initObjectEffectCreature(param1,param2)
        self.monsterCount = param3
        return self

    def reset(self):
        super().reset()
        self.monsterCount = 0

    def serialize(self, param1):
        self.serializeAs_ObjectEffectLadder(param1)

    def serializeAs_ObjectEffectLadder(self, param1):
        super().serializeAs_ObjectEffectCreature(param1)
        if self.monsterCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.monsterCount) + ") on element monsterCount.")
        param1.write_var_int(self.monsterCount)

    def deserialize(self, param1):
        self.deserializeAs_ObjectEffectLadder(param1)

    def deserializeAs_ObjectEffectLadder(self, param1):
        super().deserialize(param1)
        self._monsterCountFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ObjectEffectLadder(param1)

    def deserializeAsyncAs_ObjectEffectLadder(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._monsterCountFunc)

    def _monsterCountFunc(self, param1):
        self.monsterCount = param1.read_var_uh_int()
        if self.monsterCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.monsterCount) + ") on element of ObjectEffectLadder.monsterCount.")


class FriendOnlineInformations(FriendInformations):
    protocolId = 92

    def __init__(self):
        super().__init__()
        self.playerId = 0
        self.playerName = ""
        self.level = 0
        self.alignmentSide = 0
        self.breed = 0
        self.sex = False
        self.guildInfo = GuildInformations()
        self.moodSmileyId = 0
        self.status = PlayerStatus()
        self.havenBagShared = False
        self._guildInfotree = FuncTree()
        self._statustree = FuncTree()

    def getTypeId(self):
        return 92

    def initFriendOnlineInformations(self, param1=0, param2="", param3=99, param4=0, param5=0, param6=0, param7="", param8=0, param9=0, param10=0, param11=False, param12=None, param13=0, param14=None, param15=False):
        super().initFriendInformations(param1,param2,param3,param4,param5)
        self.playerId = param6
        self.playerName = param7
        self.level = param8
        self.alignmentSide = param9
        self.breed = param10
        self.sex = param11
        self.guildInfo = param12
        self.moodSmileyId = param13
        self.status = param14
        self.havenBagShared = param15
        return self

    def reset(self):
        super().reset()
        self.playerId = 0
        self.playerName = ""
        self.level = 0
        self.alignmentSide = 0
        self.breed = 0
        self.sex = False
        self.guildInfo = GuildInformations()
        self.status = PlayerStatus()

    def serialize(self, param1):
        self.serializeAs_FriendOnlineInformations(param1)

    def serializeAs_FriendOnlineInformations(self, param1):
        super().serializeAs_FriendInformations(param1)
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.sex)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.havenBagShared)
        param1.write_byte(_loc2_)
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element playerId.")
        param1.write_var_long(self.playerId)
        param1.write_utf(self.playerName)
        if self.level < 0 or self.level > 206:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)
        param1.write_byte(self.alignmentSide)
        param1.write_byte(self.breed)
        self.guildInfo.serializeAs_GuildInformations(param1)
        if self.moodSmileyId < 0:
            raise RuntimeError("Forbidden value (" + str(self.moodSmileyId) + ") on element moodSmileyId.")
        param1.write_var_short(self.moodSmileyId)
        param1.write_short(self.status.getTypeId())
        self.status.serialize(param1)

    def deserialize(self, param1):
        self.deserializeAs_FriendOnlineInformations(param1)

    def deserializeAs_FriendOnlineInformations(self, param1):
        super().deserialize(param1)
        self.deserializeByteBoxes(param1)
        self._playerIdFunc(param1)
        self._playerNameFunc(param1)
        self._levelFunc(param1)
        self._alignmentSideFunc(param1)
        self._breedFunc(param1)
        self.guildInfo = GuildInformations()
        self.guildInfo.deserialize(param1)
        self._moodSmileyIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_FriendOnlineInformations(param1)

    def deserializeAsyncAs_FriendOnlineInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self.deserializeByteBoxes)
        param1.add_child(self._playerIdFunc)
        param1.add_child(self._playerNameFunc)
        param1.add_child(self._levelFunc)
        param1.add_child(self._alignmentSideFunc)
        param1.add_child(self._breedFunc)
        self._guildInfotree = param1.add_child(self._guildInfotreeFunc)
        param1.add_child(self._moodSmileyIdFunc)
        self._statustree = param1.add_child(self._statustreeFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.sex = BooleanByteWrapper.get_flag(_loc2_,0)
        self.havenBagShared = BooleanByteWrapper.get_flag(_loc2_,1)

    def _playerIdFunc(self, param1):
        self.playerId = param1.read_var_uh_long()
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of FriendOnlineInformations.playerId.")

    def _playerNameFunc(self, param1):
        self.playerName = param1.read_utf()

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 0 or self.level > 206:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FriendOnlineInformations.level.")

    def _alignmentSideFunc(self, param1):
        self.alignmentSide = param1.read_byte()

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()
        if self.breed < PlayableBreedEnum.Feca or self.breed > PlayableBreedEnum.Ouginak:
            raise RuntimeError("Forbidden value (" + str(self.breed) + ") on element of FriendOnlineInformations.breed.")

    def _guildInfotreeFunc(self, param1):
        self.guildInfo = GuildInformations()
        self.guildInfo.deserializeAsync(self._guildInfotree)

    def _moodSmileyIdFunc(self, param1):
        self.moodSmileyId = param1.read_var_uh_short()
        if self.moodSmileyId < 0:
            raise RuntimeError("Forbidden value (" + str(self.moodSmileyId) + ") on element of FriendOnlineInformations.moodSmileyId.")

    def _statustreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserializeAsync(self._statustree)


class IgnoredOnlineInformations(IgnoredInformations):
    protocolId = 105

    def __init__(self):
        super().__init__()
        self.playerId = 0
        self.playerName = ""
        self.breed = 0
        self.sex = False

    def getTypeId(self):
        return 105

    def initIgnoredOnlineInformations(self, param1=0, param2="", param3=0, param4="", param5=0, param6=False):
        super().initIgnoredInformations(param1,param2)
        self.playerId = param3
        self.playerName = param4
        self.breed = param5
        self.sex = param6
        return self

    def reset(self):
        super().reset()
        self.playerId = 0
        self.playerName = ""
        self.breed = 0
        self.sex = False

    def serialize(self, param1):
        self.serializeAs_IgnoredOnlineInformations(param1)

    def serializeAs_IgnoredOnlineInformations(self, param1):
        super().serializeAs_IgnoredInformations(param1)
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element playerId.")
        param1.write_var_long(self.playerId)
        param1.write_utf(self.playerName)
        param1.write_byte(self.breed)
        param1.write_boolean(self.sex)

    def deserialize(self, param1):
        self.deserializeAs_IgnoredOnlineInformations(param1)

    def deserializeAs_IgnoredOnlineInformations(self, param1):
        super().deserialize(param1)
        self._playerIdFunc(param1)
        self._playerNameFunc(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_IgnoredOnlineInformations(param1)

    def deserializeAsyncAs_IgnoredOnlineInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._playerIdFunc)
        param1.add_child(self._playerNameFunc)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)

    def _playerIdFunc(self, param1):
        self.playerId = param1.read_var_uh_long()
        if self.playerId < 0 or self.playerId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of IgnoredOnlineInformations.playerId.")

    def _playerNameFunc(self, param1):
        self.playerName = param1.read_utf()

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()
        if self.breed < PlayableBreedEnum.Feca or self.breed > PlayableBreedEnum.Ouginak:
            raise RuntimeError("Forbidden value (" + str(self.breed) + ") on element of IgnoredOnlineInformations.breed.")

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()


class SkillActionDescriptionCollect(SkillActionDescriptionTimed):
    protocolId = 99

    def __init__(self):
        super().__init__()
        self.min = 0
        self.max = 0

    def getTypeId(self):
        return 99

    def initSkillActionDescriptionCollect(self, param1=0, param2=0, param3=0, param4=0):
        super().initSkillActionDescriptionTimed(param1,param2)
        self.min = param3
        self.max = param4
        return self

    def reset(self):
        super().reset()
        self.min = 0
        self.max = 0

    def serialize(self, param1):
        self.serializeAs_SkillActionDescriptionCollect(param1)

    def serializeAs_SkillActionDescriptionCollect(self, param1):
        super().serializeAs_SkillActionDescriptionTimed(param1)
        if self.min < 0:
            raise RuntimeError("Forbidden value (" + str(self.min) + ") on element min.")
        param1.write_var_short(self.min)
        if self.max < 0:
            raise RuntimeError("Forbidden value (" + str(self.max) + ") on element max.")
        param1.write_var_short(self.max)

    def deserialize(self, param1):
        self.deserializeAs_SkillActionDescriptionCollect(param1)

    def deserializeAs_SkillActionDescriptionCollect(self, param1):
        super().deserialize(param1)
        self._minFunc(param1)
        self._maxFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_SkillActionDescriptionCollect(param1)

    def deserializeAsyncAs_SkillActionDescriptionCollect(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._minFunc)
        param1.add_child(self._maxFunc)

    def _minFunc(self, param1):
        self.min = param1.read_var_uh_short()
        if self.min < 0:
            raise RuntimeError("Forbidden value (" + str(self.min) + ") on element of SkillActionDescriptionCollect.min.")

    def _maxFunc(self, param1):
        self.max = param1.read_var_uh_short()
        if self.max < 0:
            raise RuntimeError("Forbidden value (" + str(self.max) + ") on element of SkillActionDescriptionCollect.max.")


class ShortcutObjectIdolsPreset(ShortcutObject):
    protocolId = 492

    def __init__(self):
        super().__init__()
        self.presetId = 0

    def getTypeId(self):
        return 492

    def initShortcutObjectIdolsPreset(self, param1=0, param2=0):
        super().initShortcutObject(param1)
        self.presetId = param2
        return self

    def reset(self):
        super().reset()
        self.presetId = 0

    def serialize(self, param1):
        self.serializeAs_ShortcutObjectIdolsPreset(param1)

    def serializeAs_ShortcutObjectIdolsPreset(self, param1):
        super().serializeAs_ShortcutObject(param1)
        if self.presetId < 0:
            raise RuntimeError("Forbidden value (" + str(self.presetId) + ") on element presetId.")
        param1.write_byte(self.presetId)

    def deserialize(self, param1):
        self.deserializeAs_ShortcutObjectIdolsPreset(param1)

    def deserializeAs_ShortcutObjectIdolsPreset(self, param1):
        super().deserialize(param1)
        self._presetIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ShortcutObjectIdolsPreset(param1)

    def deserializeAsyncAs_ShortcutObjectIdolsPreset(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._presetIdFunc)

    def _presetIdFunc(self, param1):
        self.presetId = param1.read_byte()
        if self.presetId < 0:
            raise RuntimeError("Forbidden value (" + str(self.presetId) + ") on element of ShortcutObjectIdolsPreset.presetId.")


class ShortcutObjectItem(ShortcutObject):
    protocolId = 371

    def __init__(self):
        super().__init__()
        self.itemUID = 0
        self.itemGID = 0

    def getTypeId(self):
        return 371

    def initShortcutObjectItem(self, param1=0, param2=0, param3=0):
        super().initShortcutObject(param1)
        self.itemUID = param2
        self.itemGID = param3
        return self

    def reset(self):
        super().reset()
        self.itemUID = 0
        self.itemGID = 0

    def serialize(self, param1):
        self.serializeAs_ShortcutObjectItem(param1)

    def serializeAs_ShortcutObjectItem(self, param1):
        super().serializeAs_ShortcutObject(param1)
        param1.write_int(self.itemUID)
        param1.write_int(self.itemGID)

    def deserialize(self, param1):
        self.deserializeAs_ShortcutObjectItem(param1)

    def deserializeAs_ShortcutObjectItem(self, param1):
        super().deserialize(param1)
        self._itemUIDFunc(param1)
        self._itemGIDFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ShortcutObjectItem(param1)

    def deserializeAsyncAs_ShortcutObjectItem(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._itemUIDFunc)
        param1.add_child(self._itemGIDFunc)

    def _itemUIDFunc(self, param1):
        self.itemUID = param1.read_int()

    def _itemGIDFunc(self, param1):
        self.itemGID = param1.read_int()


class ShortcutObjectPreset(ShortcutObject):
    protocolId = 370

    def __init__(self):
        super().__init__()
        self.presetId = 0

    def getTypeId(self):
        return 370

    def initShortcutObjectPreset(self, param1=0, param2=0):
        super().initShortcutObject(param1)
        self.presetId = param2
        return self

    def reset(self):
        super().reset()
        self.presetId = 0

    def serialize(self, param1):
        self.serializeAs_ShortcutObjectPreset(param1)

    def serializeAs_ShortcutObjectPreset(self, param1):
        super().serializeAs_ShortcutObject(param1)
        if self.presetId < 0:
            raise RuntimeError("Forbidden value (" + str(self.presetId) + ") on element presetId.")
        param1.write_byte(self.presetId)

    def deserialize(self, param1):
        self.deserializeAs_ShortcutObjectPreset(param1)

    def deserializeAs_ShortcutObjectPreset(self, param1):
        super().deserialize(param1)
        self._presetIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_ShortcutObjectPreset(param1)

    def deserializeAsyncAs_ShortcutObjectPreset(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._presetIdFunc)

    def _presetIdFunc(self, param1):
        self.presetId = param1.read_byte()
        if self.presetId < 0:
            raise RuntimeError("Forbidden value (" + str(self.presetId) + ") on element of ShortcutObjectPreset.presetId.")


class CharacterMinimalPlusLookInformations(CharacterMinimalInformations):
    protocolId = 163

    def __init__(self):
        super().__init__()
        self.entityLook = EntityLook()
        self._entityLooktree = FuncTree()

    def getTypeId(self):
        return 163

    def initCharacterMinimalPlusLookInformations(self, param1=0, param2="", param3=0, param4=None):
        super().initCharacterMinimalInformations(param1,param2,param3)
        self.entityLook = param4
        return self

    def reset(self):
        super().reset()
        self.entityLook = EntityLook()

    def serialize(self, param1):
        self.serializeAs_CharacterMinimalPlusLookInformations(param1)

    def serializeAs_CharacterMinimalPlusLookInformations(self, param1):
        super().serializeAs_CharacterMinimalInformations(param1)
        self.entityLook.serializeAs_EntityLook(param1)

    def deserialize(self, param1):
        self.deserializeAs_CharacterMinimalPlusLookInformations(param1)

    def deserializeAs_CharacterMinimalPlusLookInformations(self, param1):
        super().deserialize(param1)
        self.entityLook = EntityLook()
        self.entityLook.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterMinimalPlusLookInformations(param1)

    def deserializeAsyncAs_CharacterMinimalPlusLookInformations(self, param1):
        super().deserializeAsync(param1)
        self._entityLooktree = param1.add_child(self._entityLooktreeFunc)

    def _entityLooktreeFunc(self, param1):
        self.entityLook = EntityLook()
        self.entityLook.deserializeAsync(self._entityLooktree)


class GameFightCharacterInformations(GameFightFighterNamedInformations):
    protocolId = 46

    def __init__(self):
        super().__init__()
        self.level = 0
        self.alignmentInfos = ActorAlignmentInformations()
        self.breed = 0
        self.sex = False
        self._alignmentInfostree = FuncTree()

    def getTypeId(self):
        return 46

    def initGameFightCharacterInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[], param9="", param10=None, param11=0, param12=None, param13=0, param14=False):
        super().initGameFightFighterNamedInformations(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10)
        self.level = param11
        self.alignmentInfos = param12
        self.breed = param13
        self.sex = param14
        return self

    def reset(self):
        super().reset()
        self.level = 0
        self.alignmentInfos = ActorAlignmentInformations()
        self.sex = False

    def serialize(self, param1):
        self.serializeAs_GameFightCharacterInformations(param1)

    def serializeAs_GameFightCharacterInformations(self, param1):
        super().serializeAs_GameFightFighterNamedInformations(param1)
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)
        self.alignmentInfos.serializeAs_ActorAlignmentInformations(param1)
        param1.write_byte(self.breed)
        param1.write_boolean(self.sex)

    def deserialize(self, param1):
        self.deserializeAs_GameFightCharacterInformations(param1)

    def deserializeAs_GameFightCharacterInformations(self, param1):
        super().deserialize(param1)
        self._levelFunc(param1)
        self.alignmentInfos = ActorAlignmentInformations()
        self.alignmentInfos.deserialize(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightCharacterInformations(param1)

    def deserializeAsyncAs_GameFightCharacterInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._levelFunc)
        self._alignmentInfostree = param1.add_child(self._alignmentInfostreeFunc)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of GameFightCharacterInformations.level.")

    def _alignmentInfostreeFunc(self, param1):
        self.alignmentInfos = ActorAlignmentInformations()
        self.alignmentInfos.deserializeAsync(self._alignmentInfostree)

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()


class GameFightMonsterInformations(GameFightAIInformations):
    protocolId = 29

    def __init__(self):
        super().__init__()
        self.creatureGenericId = 0
        self.creatureGrade = 0

    def getTypeId(self):
        return 29

    def initGameFightMonsterInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[], param9=0, param10=0):
        super().initGameFightAIInformations(param1,param2,param3,param4,param5,param6,param7,param8)
        self.creatureGenericId = param9
        self.creatureGrade = param10
        return self

    def reset(self):
        super().reset()
        self.creatureGenericId = 0
        self.creatureGrade = 0

    def serialize(self, param1):
        self.serializeAs_GameFightMonsterInformations(param1)

    def serializeAs_GameFightMonsterInformations(self, param1):
        super().serializeAs_GameFightAIInformations(param1)
        if self.creatureGenericId < 0:
            raise RuntimeError("Forbidden value (" + str(self.creatureGenericId) + ") on element creatureGenericId.")
        param1.write_var_short(self.creatureGenericId)
        if self.creatureGrade < 0:
            raise RuntimeError("Forbidden value (" + str(self.creatureGrade) + ") on element creatureGrade.")
        param1.write_byte(self.creatureGrade)

    def deserialize(self, param1):
        self.deserializeAs_GameFightMonsterInformations(param1)

    def deserializeAs_GameFightMonsterInformations(self, param1):
        super().deserialize(param1)
        self._creatureGenericIdFunc(param1)
        self._creatureGradeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightMonsterInformations(param1)

    def deserializeAsyncAs_GameFightMonsterInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._creatureGenericIdFunc)
        param1.add_child(self._creatureGradeFunc)

    def _creatureGenericIdFunc(self, param1):
        self.creatureGenericId = param1.read_var_uh_short()
        if self.creatureGenericId < 0:
            raise RuntimeError("Forbidden value (" + str(self.creatureGenericId) + ") on element of GameFightMonsterInformations.creatureGenericId.")

    def _creatureGradeFunc(self, param1):
        self.creatureGrade = param1.read_byte()
        if self.creatureGrade < 0:
            raise RuntimeError("Forbidden value (" + str(self.creatureGrade) + ") on element of GameFightMonsterInformations.creatureGrade.")


class GameFightMutantInformations(GameFightFighterNamedInformations):
    protocolId = 50

    def __init__(self):
        super().__init__()
        self.powerLevel = 0

    def getTypeId(self):
        return 50

    def initGameFightMutantInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[], param9="", param10=None, param11=0):
        super().initGameFightFighterNamedInformations(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10)
        self.powerLevel = param11
        return self

    def reset(self):
        super().reset()
        self.powerLevel = 0

    def serialize(self, param1):
        self.serializeAs_GameFightMutantInformations(param1)

    def serializeAs_GameFightMutantInformations(self, param1):
        super().serializeAs_GameFightFighterNamedInformations(param1)
        if self.powerLevel < 0:
            raise RuntimeError("Forbidden value (" + str(self.powerLevel) + ") on element powerLevel.")
        param1.write_byte(self.powerLevel)

    def deserialize(self, param1):
        self.deserializeAs_GameFightMutantInformations(param1)

    def deserializeAs_GameFightMutantInformations(self, param1):
        super().deserialize(param1)
        self._powerLevelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightMutantInformations(param1)

    def deserializeAsyncAs_GameFightMutantInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._powerLevelFunc)

    def _powerLevelFunc(self, param1):
        self.powerLevel = param1.read_byte()
        if self.powerLevel < 0:
            raise RuntimeError("Forbidden value (" + str(self.powerLevel) + ") on element of GameFightMutantInformations.powerLevel.")


class GameFightTaxCollectorInformations(GameFightAIInformations):
    protocolId = 48

    def __init__(self):
        super().__init__()
        self.firstNameId = 0
        self.lastNameId = 0
        self.level = 0

    def getTypeId(self):
        return 48

    def initGameFightTaxCollectorInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[], param9=0, param10=0, param11=0):
        super().initGameFightAIInformations(param1,param2,param3,param4,param5,param6,param7,param8)
        self.firstNameId = param9
        self.lastNameId = param10
        self.level = param11
        return self

    def reset(self):
        super().reset()
        self.firstNameId = 0
        self.lastNameId = 0
        self.level = 0

    def serialize(self, param1):
        self.serializeAs_GameFightTaxCollectorInformations(param1)

    def serializeAs_GameFightTaxCollectorInformations(self, param1):
        super().serializeAs_GameFightAIInformations(param1)
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element firstNameId.")
        param1.write_var_short(self.firstNameId)
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element lastNameId.")
        param1.write_var_short(self.lastNameId)
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)

    def deserialize(self, param1):
        self.deserializeAs_GameFightTaxCollectorInformations(param1)

    def deserializeAs_GameFightTaxCollectorInformations(self, param1):
        super().deserialize(param1)
        self._firstNameIdFunc(param1)
        self._lastNameIdFunc(param1)
        self._levelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightTaxCollectorInformations(param1)

    def deserializeAsyncAs_GameFightTaxCollectorInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._firstNameIdFunc)
        param1.add_child(self._lastNameIdFunc)
        param1.add_child(self._levelFunc)

    def _firstNameIdFunc(self, param1):
        self.firstNameId = param1.read_var_uh_short()
        if self.firstNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of GameFightTaxCollectorInformations.firstNameId.")

    def _lastNameIdFunc(self, param1):
        self.lastNameId = param1.read_var_uh_short()
        if self.lastNameId < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of GameFightTaxCollectorInformations.lastNameId.")

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of GameFightTaxCollectorInformations.level.")


class AllianceInformations(BasicNamedAllianceInformations):
    protocolId = 417

    def __init__(self):
        super().__init__()
        self.allianceEmblem = GuildEmblem()
        self._allianceEmblemtree = FuncTree()

    def getTypeId(self):
        return 417

    def initAllianceInformations(self, param1=0, param2="", param3="", param4=None):
        super().initBasicNamedAllianceInformations(param1,param2,param3)
        self.allianceEmblem = param4
        return self

    def reset(self):
        super().reset()
        self.allianceEmblem = GuildEmblem()

    def serialize(self, param1):
        self.serializeAs_AllianceInformations(param1)

    def serializeAs_AllianceInformations(self, param1):
        super().serializeAs_BasicNamedAllianceInformations(param1)
        self.allianceEmblem.serializeAs_GuildEmblem(param1)

    def deserialize(self, param1):
        self.deserializeAs_AllianceInformations(param1)

    def deserializeAs_AllianceInformations(self, param1):
        super().deserialize(param1)
        self.allianceEmblem = GuildEmblem()
        self.allianceEmblem.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AllianceInformations(param1)

    def deserializeAsyncAs_AllianceInformations(self, param1):
        super().deserializeAsync(param1)
        self._allianceEmblemtree = param1.add_child(self._allianceEmblemtreeFunc)

    def _allianceEmblemtreeFunc(self, param1):
        self.allianceEmblem = GuildEmblem()
        self.allianceEmblem.deserializeAsync(self._allianceEmblemtree)


class GameRolePlayGroupMonsterWaveInformations(GameRolePlayGroupMonsterInformations):
    protocolId = 464

    def __init__(self):
        super().__init__()
        self.nbWaves = 0
        self.alternatives = []
        self._alternativestree = FuncTree()

    def getTypeId(self):
        return 464

    def initGameRolePlayGroupMonsterWaveInformations(self, param1=0, param2=None, param3=None, param4=None, param5=0, param6=0, param7=0, param8=0, param9=False, param10=False, param11=False, param12=0, param13=[]):
        super().initGameRolePlayGroupMonsterInformations(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11)
        self.nbWaves = param12
        self.alternatives = param13
        return self

    def reset(self):
        super().reset()
        self.nbWaves = 0
        self.alternatives = []

    def serialize(self, param1):
        self.serializeAs_GameRolePlayGroupMonsterWaveInformations(param1)

    def serializeAs_GameRolePlayGroupMonsterWaveInformations(self, param1):
        super().serializeAs_GameRolePlayGroupMonsterInformations(param1)
        if self.nbWaves < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbWaves) + ") on element nbWaves.")
        param1.write_byte(self.nbWaves)
        param1.write_short(len(self.alternatives))
        _loc2_ = 0
        while _loc2_ < len(self.alternatives):
            param1.write_short(as_parent(self.alternatives[_loc2_], GroupMonsterStaticInformations).getTypeId())
            as_parent(self.alternatives[_loc2_], GroupMonsterStaticInformations).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayGroupMonsterWaveInformations(param1)

    def deserializeAs_GameRolePlayGroupMonsterWaveInformations(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._nbWavesFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(GroupMonsterStaticInformations,_loc4_)
            _loc5_.deserialize(param1)
            self.alternatives.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayGroupMonsterWaveInformations(param1)

    def deserializeAsyncAs_GameRolePlayGroupMonsterWaveInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nbWavesFunc)
        self._alternativestree = param1.add_child(self._alternativestreeFunc)

    def _nbWavesFunc(self, param1):
        self.nbWaves = param1.read_byte()
        if self.nbWaves < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbWaves) + ") on element of GameRolePlayGroupMonsterWaveInformations.nbWaves.")

    def _alternativestreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._alternativestree.add_child(self._alternativesFunc)
            _loc3_ += 1

    def _alternativesFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(GroupMonsterStaticInformations,_loc2_)
        _loc3_.deserialize(param1)
        self.alternatives.append(_loc3_)


class GameRolePlayHumanoidInformations(GameRolePlayNamedActorInformations):
    protocolId = 159

    def __init__(self):
        super().__init__()
        self.humanoidInfo = HumanInformations()
        self.accountId = 0
        self._humanoidInfotree = FuncTree()

    def getTypeId(self):
        return 159

    def initGameRolePlayHumanoidInformations(self, param1=0, param2=None, param3=None, param4="", param5=None, param6=0):
        super().initGameRolePlayNamedActorInformations(param1,param2,param3,param4)
        self.humanoidInfo = param5
        self.accountId = param6
        return self

    def reset(self):
        super().reset()
        self.humanoidInfo = HumanInformations()

    def serialize(self, param1):
        self.serializeAs_GameRolePlayHumanoidInformations(param1)

    def serializeAs_GameRolePlayHumanoidInformations(self, param1):
        super().serializeAs_GameRolePlayNamedActorInformations(param1)
        param1.write_short(self.humanoidInfo.getTypeId())
        self.humanoidInfo.serialize(param1)
        if self.accountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element accountId.")
        param1.write_int(self.accountId)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayHumanoidInformations(param1)

    def deserializeAs_GameRolePlayHumanoidInformations(self, param1):
        super().deserialize(param1)
        _loc2_ = param1.read_unsigned_short()
        self.humanoidInfo = ProtocolTypeManager.get_instance(HumanInformations,_loc2_)
        self.humanoidInfo.deserialize(param1)
        self._accountIdFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayHumanoidInformations(param1)

    def deserializeAsyncAs_GameRolePlayHumanoidInformations(self, param1):
        super().deserializeAsync(param1)
        self._humanoidInfotree = param1.add_child(self._humanoidInfotreeFunc)
        param1.add_child(self._accountIdFunc)

    def _humanoidInfotreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.humanoidInfo = ProtocolTypeManager.get_instance(HumanInformations,_loc2_)
        self.humanoidInfo.deserializeAsync(self._humanoidInfotree)

    def _accountIdFunc(self, param1):
        self.accountId = param1.read_int()
        if self.accountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of GameRolePlayHumanoidInformations.accountId.")


class GameRolePlayMerchantInformations(GameRolePlayNamedActorInformations):
    protocolId = 129

    def __init__(self):
        super().__init__()
        self.sellType = 0
        self.options = []
        self._optionstree = FuncTree()

    def getTypeId(self):
        return 129

    def initGameRolePlayMerchantInformations(self, param1=0, param2=None, param3=None, param4="", param5=0, param6=[]):
        super().initGameRolePlayNamedActorInformations(param1,param2,param3,param4)
        self.sellType = param5
        self.options = param6
        return self

    def reset(self):
        super().reset()
        self.sellType = 0
        self.options = []

    def serialize(self, param1):
        self.serializeAs_GameRolePlayMerchantInformations(param1)

    def serializeAs_GameRolePlayMerchantInformations(self, param1):
        super().serializeAs_GameRolePlayNamedActorInformations(param1)
        if self.sellType < 0:
            raise RuntimeError("Forbidden value (" + str(self.sellType) + ") on element sellType.")
        param1.write_byte(self.sellType)
        param1.write_short(len(self.options))
        _loc2_ = 0
        while _loc2_ < len(self.options):
            param1.write_short(as_parent(self.options[_loc2_], HumanOption).getTypeId())
            as_parent(self.options[_loc2_], HumanOption).serialize(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayMerchantInformations(param1)

    def deserializeAs_GameRolePlayMerchantInformations(self, param1):
        _loc4_ = 0
        _loc5_ = None
        super().deserialize(param1)
        self._sellTypeFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = param1.read_unsigned_short()
            _loc5_ = ProtocolTypeManager.get_instance(HumanOption,_loc4_)
            _loc5_.deserialize(param1)
            self.options.append(_loc5_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayMerchantInformations(param1)

    def deserializeAsyncAs_GameRolePlayMerchantInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._sellTypeFunc)
        self._optionstree = param1.add_child(self._optionstreeFunc)

    def _sellTypeFunc(self, param1):
        self.sellType = param1.read_byte()
        if self.sellType < 0:
            raise RuntimeError("Forbidden value (" + str(self.sellType) + ") on element of GameRolePlayMerchantInformations.sellType.")

    def _optionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._optionstree.add_child(self._optionsFunc)
            _loc3_ += 1

    def _optionsFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = ProtocolTypeManager.get_instance(HumanOption,_loc2_)
        _loc3_.deserialize(param1)
        self.options.append(_loc3_)


class GameRolePlayMountInformations(GameRolePlayNamedActorInformations):
    protocolId = 180

    def __init__(self):
        super().__init__()
        self.ownerName = ""
        self.level = 0

    def getTypeId(self):
        return 180

    def initGameRolePlayMountInformations(self, param1=0, param2=None, param3=None, param4="", param5="", param6=0):
        super().initGameRolePlayNamedActorInformations(param1,param2,param3,param4)
        self.ownerName = param5
        self.level = param6
        return self

    def reset(self):
        super().reset()
        self.ownerName = ""
        self.level = 0

    def serialize(self, param1):
        self.serializeAs_GameRolePlayMountInformations(param1)

    def serializeAs_GameRolePlayMountInformations(self, param1):
        super().serializeAs_GameRolePlayNamedActorInformations(param1)
        param1.write_utf(self.ownerName)
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element level.")
        param1.write_byte(self.level)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayMountInformations(param1)

    def deserializeAs_GameRolePlayMountInformations(self, param1):
        super().deserialize(param1)
        self._ownerNameFunc(param1)
        self._levelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayMountInformations(param1)

    def deserializeAsyncAs_GameRolePlayMountInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._ownerNameFunc)
        param1.add_child(self._levelFunc)

    def _ownerNameFunc(self, param1):
        self.ownerName = param1.read_utf()

    def _levelFunc(self, param1):
        self.level = param1.read_unsigned_byte()
        if self.level < 0 or self.level > 255:
            raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of GameRolePlayMountInformations.level.")


class GameRolePlayNpcWithQuestInformations(GameRolePlayNpcInformations):
    protocolId = 383

    def __init__(self):
        super().__init__()
        self.questFlag = GameRolePlayNpcQuestFlag()
        self._questFlagtree = FuncTree()

    def getTypeId(self):
        return 383

    def initGameRolePlayNpcWithQuestInformations(self, param1=0, param2=None, param3=None, param4=0, param5=False, param6=0, param7=None):
        super().initGameRolePlayNpcInformations(param1,param2,param3,param4,param5,param6)
        self.questFlag = param7
        return self

    def reset(self):
        super().reset()
        self.questFlag = GameRolePlayNpcQuestFlag()

    def serialize(self, param1):
        self.serializeAs_GameRolePlayNpcWithQuestInformations(param1)

    def serializeAs_GameRolePlayNpcWithQuestInformations(self, param1):
        super().serializeAs_GameRolePlayNpcInformations(param1)
        self.questFlag.serializeAs_GameRolePlayNpcQuestFlag(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayNpcWithQuestInformations(param1)

    def deserializeAs_GameRolePlayNpcWithQuestInformations(self, param1):
        super().deserialize(param1)
        self.questFlag = GameRolePlayNpcQuestFlag()
        self.questFlag.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayNpcWithQuestInformations(param1)

    def deserializeAsyncAs_GameRolePlayNpcWithQuestInformations(self, param1):
        super().deserializeAsync(param1)
        self._questFlagtree = param1.add_child(self._questFlagtreeFunc)

    def _questFlagtreeFunc(self, param1):
        self.questFlag = GameRolePlayNpcQuestFlag()
        self.questFlag.deserializeAsync(self._questFlagtree)


class GuildInAllianceInformations(GuildInformations):
    protocolId = 420

    def __init__(self):
        super().__init__()
        self.nbMembers = 0

    def getTypeId(self):
        return 420

    def initGuildInAllianceInformations(self, param1=0, param2="", param3=0, param4=None, param5=0):
        super().initGuildInformations(param1,param2,param3,param4)
        self.nbMembers = param5
        return self

    def reset(self):
        super().reset()
        self.nbMembers = 0

    def serialize(self, param1):
        self.serializeAs_GuildInAllianceInformations(param1)

    def serializeAs_GuildInAllianceInformations(self, param1):
        super().serializeAs_GuildInformations(param1)
        if self.nbMembers < 1 or self.nbMembers > 240:
            raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element nbMembers.")
        param1.write_byte(self.nbMembers)

    def deserialize(self, param1):
        self.deserializeAs_GuildInAllianceInformations(param1)

    def deserializeAs_GuildInAllianceInformations(self, param1):
        super().deserialize(param1)
        self._nbMembersFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GuildInAllianceInformations(param1)

    def deserializeAsyncAs_GuildInAllianceInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._nbMembersFunc)

    def _nbMembersFunc(self, param1):
        self.nbMembers = param1.read_unsigned_byte()
        if self.nbMembers < 1 or self.nbMembers > 240:
            raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element of GuildInAllianceInformations.nbMembers.")


class GuildMember(CharacterMinimalInformations):
    protocolId = 88

    def __init__(self):
        super().__init__()
        self.breed = 0
        self.sex = False
        self.rank = 0
        self.givenExperience = 0
        self.experienceGivenPercent = 0
        self.rights = 0
        self.connected = 99
        self.alignmentSide = 0
        self.hoursSinceLastConnection = 0
        self.moodSmileyId = 0
        self.accountId = 0
        self.achievementPoints = 0
        self.status = PlayerStatus()
        self.havenBagShared = False
        self._statustree = FuncTree()

    def getTypeId(self):
        return 88

    def initGuildMember(self, param1=0, param2="", param3=0, param4=0, param5=False, param6=0, param7=0, param8=0, param9=0, param10=99, param11=0, param12=0, param13=0, param14=0, param15=0, param16=None, param17=False):
        super().initCharacterMinimalInformations(param1,param2,param3)
        self.breed = param4
        self.sex = param5
        self.rank = param6
        self.givenExperience = param7
        self.experienceGivenPercent = param8
        self.rights = param9
        self.connected = param10
        self.alignmentSide = param11
        self.hoursSinceLastConnection = param12
        self.moodSmileyId = param13
        self.accountId = param14
        self.achievementPoints = param15
        self.status = param16
        self.havenBagShared = param17
        return self

    def reset(self):
        super().reset()
        self.breed = 0
        self.sex = False
        self.rank = 0
        self.givenExperience = 0
        self.experienceGivenPercent = 0
        self.rights = 0
        self.connected = 99
        self.alignmentSide = 0
        self.hoursSinceLastConnection = 0
        self.moodSmileyId = 0
        self.accountId = 0
        self.achievementPoints = 0
        self.status = PlayerStatus()

    def serialize(self, param1):
        self.serializeAs_GuildMember(param1)

    def serializeAs_GuildMember(self, param1):
        super().serializeAs_CharacterMinimalInformations(param1)
        _loc2_ = 0
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,0,self.sex)
        _loc2_ = BooleanByteWrapper.set_flag(_loc2_,1,self.havenBagShared)
        param1.write_byte(_loc2_)
        param1.write_byte(self.breed)
        if self.rank < 0:
            raise RuntimeError("Forbidden value (" + str(self.rank) + ") on element rank.")
        param1.write_var_short(self.rank)
        if self.givenExperience < 0 or self.givenExperience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.givenExperience) + ") on element givenExperience.")
        param1.write_var_long(self.givenExperience)
        if self.experienceGivenPercent < 0 or self.experienceGivenPercent > 100:
            raise RuntimeError("Forbidden value (" + str(self.experienceGivenPercent) + ") on element experienceGivenPercent.")
        param1.write_byte(self.experienceGivenPercent)
        if self.rights < 0:
            raise RuntimeError("Forbidden value (" + str(self.rights) + ") on element rights.")
        param1.write_var_int(self.rights)
        param1.write_byte(self.connected)
        param1.write_byte(self.alignmentSide)
        if self.hoursSinceLastConnection < 0 or self.hoursSinceLastConnection > 65535:
            raise RuntimeError("Forbidden value (" + str(self.hoursSinceLastConnection) + ") on element hoursSinceLastConnection.")
        param1.write_short(self.hoursSinceLastConnection)
        if self.moodSmileyId < 0:
            raise RuntimeError("Forbidden value (" + str(self.moodSmileyId) + ") on element moodSmileyId.")
        param1.write_var_short(self.moodSmileyId)
        if self.accountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element accountId.")
        param1.write_int(self.accountId)
        param1.write_int(self.achievementPoints)
        param1.write_short(self.status.getTypeId())
        self.status.serialize(param1)

    def deserialize(self, param1):
        self.deserializeAs_GuildMember(param1)

    def deserializeAs_GuildMember(self, param1):
        super().deserialize(param1)
        self.deserializeByteBoxes(param1)
        self._breedFunc(param1)
        self._rankFunc(param1)
        self._givenExperienceFunc(param1)
        self._experienceGivenPercentFunc(param1)
        self._rightsFunc(param1)
        self._connectedFunc(param1)
        self._alignmentSideFunc(param1)
        self._hoursSinceLastConnectionFunc(param1)
        self._moodSmileyIdFunc(param1)
        self._accountIdFunc(param1)
        self._achievementPointsFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GuildMember(param1)

    def deserializeAsyncAs_GuildMember(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self.deserializeByteBoxes)
        param1.add_child(self._breedFunc)
        param1.add_child(self._rankFunc)
        param1.add_child(self._givenExperienceFunc)
        param1.add_child(self._experienceGivenPercentFunc)
        param1.add_child(self._rightsFunc)
        param1.add_child(self._connectedFunc)
        param1.add_child(self._alignmentSideFunc)
        param1.add_child(self._hoursSinceLastConnectionFunc)
        param1.add_child(self._moodSmileyIdFunc)
        param1.add_child(self._accountIdFunc)
        param1.add_child(self._achievementPointsFunc)
        self._statustree = param1.add_child(self._statustreeFunc)

    def deserializeByteBoxes(self, param1):
        _loc2_ = param1.read_byte()
        self.sex = BooleanByteWrapper.get_flag(_loc2_,0)
        self.havenBagShared = BooleanByteWrapper.get_flag(_loc2_,1)

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()

    def _rankFunc(self, param1):
        self.rank = param1.read_var_uh_short()
        if self.rank < 0:
            raise RuntimeError("Forbidden value (" + str(self.rank) + ") on element of GuildMember.rank.")

    def _givenExperienceFunc(self, param1):
        self.givenExperience = param1.read_var_uh_long()
        if self.givenExperience < 0 or self.givenExperience > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.givenExperience) + ") on element of GuildMember.givenExperience.")

    def _experienceGivenPercentFunc(self, param1):
        self.experienceGivenPercent = param1.read_byte()
        if self.experienceGivenPercent < 0 or self.experienceGivenPercent > 100:
            raise RuntimeError("Forbidden value (" + str(self.experienceGivenPercent) + ") on element of GuildMember.experienceGivenPercent.")

    def _rightsFunc(self, param1):
        self.rights = param1.read_var_uh_int()
        if self.rights < 0:
            raise RuntimeError("Forbidden value (" + str(self.rights) + ") on element of GuildMember.rights.")

    def _connectedFunc(self, param1):
        self.connected = param1.read_byte()
        if self.connected < 0:
            raise RuntimeError("Forbidden value (" + str(self.connected) + ") on element of GuildMember.connected.")

    def _alignmentSideFunc(self, param1):
        self.alignmentSide = param1.read_byte()

    def _hoursSinceLastConnectionFunc(self, param1):
        self.hoursSinceLastConnection = param1.read_unsigned_short()
        if self.hoursSinceLastConnection < 0 or self.hoursSinceLastConnection > 65535:
            raise RuntimeError("Forbidden value (" + str(self.hoursSinceLastConnection) + ") on element of GuildMember.hoursSinceLastConnection.")

    def _moodSmileyIdFunc(self, param1):
        self.moodSmileyId = param1.read_var_uh_short()
        if self.moodSmileyId < 0:
            raise RuntimeError("Forbidden value (" + str(self.moodSmileyId) + ") on element of GuildMember.moodSmileyId.")

    def _accountIdFunc(self, param1):
        self.accountId = param1.read_int()
        if self.accountId < 0:
            raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of GuildMember.accountId.")

    def _achievementPointsFunc(self, param1):
        self.achievementPoints = param1.read_int()

    def _statustreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserializeAsync(self._statustree)


class AlliancedGuildFactSheetInformations(GuildInformations):
    protocolId = 422

    def __init__(self):
        super().__init__()
        self.allianceInfos = BasicNamedAllianceInformations()
        self._allianceInfostree = FuncTree()

    def getTypeId(self):
        return 422

    def initAlliancedGuildFactSheetInformations(self, param1=0, param2="", param3=0, param4=None, param5=None):
        super().initGuildInformations(param1,param2,param3,param4)
        self.allianceInfos = param5
        return self

    def reset(self):
        super().reset()
        self.allianceInfos = BasicNamedAllianceInformations()

    def serialize(self, param1):
        self.serializeAs_AlliancedGuildFactSheetInformations(param1)

    def serializeAs_AlliancedGuildFactSheetInformations(self, param1):
        super().serializeAs_GuildInformations(param1)
        self.allianceInfos.serializeAs_BasicNamedAllianceInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_AlliancedGuildFactSheetInformations(param1)

    def deserializeAs_AlliancedGuildFactSheetInformations(self, param1):
        super().deserialize(param1)
        self.allianceInfos = BasicNamedAllianceInformations()
        self.allianceInfos.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AlliancedGuildFactSheetInformations(param1)

    def deserializeAsyncAs_AlliancedGuildFactSheetInformations(self, param1):
        super().deserializeAsync(param1)
        self._allianceInfostree = param1.add_child(self._allianceInfostreeFunc)

    def _allianceInfostreeFunc(self, param1):
        self.allianceInfos = BasicNamedAllianceInformations()
        self.allianceInfos.deserializeAsync(self._allianceInfostree)


class GuildFactSheetInformations(GuildInformations):
    protocolId = 424

    def __init__(self):
        super().__init__()
        self.leaderId = 0
        self.nbMembers = 0

    def getTypeId(self):
        return 424

    def initGuildFactSheetInformations(self, param1=0, param2="", param3=0, param4=None, param5=0, param6=0):
        super().initGuildInformations(param1,param2,param3,param4)
        self.leaderId = param5
        self.nbMembers = param6
        return self

    def reset(self):
        super().reset()
        self.leaderId = 0
        self.nbMembers = 0

    def serialize(self, param1):
        self.serializeAs_GuildFactSheetInformations(param1)

    def serializeAs_GuildFactSheetInformations(self, param1):
        super().serializeAs_GuildInformations(param1)
        if self.leaderId < 0 or self.leaderId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.leaderId) + ") on element leaderId.")
        param1.write_var_long(self.leaderId)
        if self.nbMembers < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element nbMembers.")
        param1.write_var_short(self.nbMembers)

    def deserialize(self, param1):
        self.deserializeAs_GuildFactSheetInformations(param1)

    def deserializeAs_GuildFactSheetInformations(self, param1):
        super().deserialize(param1)
        self._leaderIdFunc(param1)
        self._nbMembersFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GuildFactSheetInformations(param1)

    def deserializeAsyncAs_GuildFactSheetInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._leaderIdFunc)
        param1.add_child(self._nbMembersFunc)

    def _leaderIdFunc(self, param1):
        self.leaderId = param1.read_var_uh_long()
        if self.leaderId < 0 or self.leaderId > 9007199254740990:
            raise RuntimeError("Forbidden value (" + str(self.leaderId) + ") on element of GuildFactSheetInformations.leaderId.")

    def _nbMembersFunc(self, param1):
        self.nbMembers = param1.read_var_uh_short()
        if self.nbMembers < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbMembers) + ") on element of GuildFactSheetInformations.nbMembers.")


class CharacterMinimalGuildInformations(CharacterMinimalPlusLookInformations):
    protocolId = 445

    def __init__(self):
        super().__init__()
        self.guild = BasicGuildInformations()
        self._guildtree = FuncTree()

    def getTypeId(self):
        return 445

    def initCharacterMinimalGuildInformations(self, param1=0, param2="", param3=0, param4=None, param5=None):
        super().initCharacterMinimalPlusLookInformations(param1,param2,param3,param4)
        self.guild = param5
        return self

    def reset(self):
        super().reset()
        self.guild = BasicGuildInformations()

    def serialize(self, param1):
        self.serializeAs_CharacterMinimalGuildInformations(param1)

    def serializeAs_CharacterMinimalGuildInformations(self, param1):
        super().serializeAs_CharacterMinimalPlusLookInformations(param1)
        self.guild.serializeAs_BasicGuildInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_CharacterMinimalGuildInformations(param1)

    def deserializeAs_CharacterMinimalGuildInformations(self, param1):
        super().deserialize(param1)
        self.guild = BasicGuildInformations()
        self.guild.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterMinimalGuildInformations(param1)

    def deserializeAsyncAs_CharacterMinimalGuildInformations(self, param1):
        super().deserializeAsync(param1)
        self._guildtree = param1.add_child(self._guildtreeFunc)

    def _guildtreeFunc(self, param1):
        self.guild = BasicGuildInformations()
        self.guild.deserializeAsync(self._guildtree)


class CharacterMinimalPlusLookAndGradeInformations(CharacterMinimalPlusLookInformations):
    protocolId = 193

    def __init__(self):
        super().__init__()
        self.grade = 0

    def getTypeId(self):
        return 193

    def initCharacterMinimalPlusLookAndGradeInformations(self, param1=0, param2="", param3=0, param4=None, param5=0):
        super().initCharacterMinimalPlusLookInformations(param1,param2,param3,param4)
        self.grade = param5
        return self

    def reset(self):
        super().reset()
        self.grade = 0

    def serialize(self, param1):
        self.serializeAs_CharacterMinimalPlusLookAndGradeInformations(param1)

    def serializeAs_CharacterMinimalPlusLookAndGradeInformations(self, param1):
        super().serializeAs_CharacterMinimalPlusLookInformations(param1)
        if self.grade < 0:
            raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element grade.")
        param1.write_var_int(self.grade)

    def deserialize(self, param1):
        self.deserializeAs_CharacterMinimalPlusLookAndGradeInformations(param1)

    def deserializeAs_CharacterMinimalPlusLookAndGradeInformations(self, param1):
        super().deserialize(param1)
        self._gradeFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterMinimalPlusLookAndGradeInformations(param1)

    def deserializeAsyncAs_CharacterMinimalPlusLookAndGradeInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._gradeFunc)

    def _gradeFunc(self, param1):
        self.grade = param1.read_var_uh_int()
        if self.grade < 0:
            raise RuntimeError("Forbidden value (" + str(self.grade) + ") on element of CharacterMinimalPlusLookAndGradeInformations.grade.")


class CharacterBaseInformations(CharacterMinimalPlusLookInformations):
    protocolId = 45

    def __init__(self):
        super().__init__()
        self.breed = 0
        self.sex = False

    def getTypeId(self):
        return 45

    def initCharacterBaseInformations(self, param1=0, param2="", param3=0, param4=None, param5=0, param6=False):
        super().initCharacterMinimalPlusLookInformations(param1,param2,param3,param4)
        self.breed = param5
        self.sex = param6
        return self

    def reset(self):
        super().reset()
        self.breed = 0
        self.sex = False

    def serialize(self, param1):
        self.serializeAs_CharacterBaseInformations(param1)

    def serializeAs_CharacterBaseInformations(self, param1):
        super().serializeAs_CharacterMinimalPlusLookInformations(param1)
        param1.write_byte(self.breed)
        param1.write_boolean(self.sex)

    def deserialize(self, param1):
        self.deserializeAs_CharacterBaseInformations(param1)

    def deserializeAs_CharacterBaseInformations(self, param1):
        super().deserialize(param1)
        self._breedFunc(param1)
        self._sexFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterBaseInformations(param1)

    def deserializeAsyncAs_CharacterBaseInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._breedFunc)
        param1.add_child(self._sexFunc)

    def _breedFunc(self, param1):
        self.breed = param1.read_byte()

    def _sexFunc(self, param1):
        self.sex = param1.read_boolean()


class GameFightMonsterWithAlignmentInformations(GameFightMonsterInformations):
    protocolId = 203

    def __init__(self):
        super().__init__()
        self.alignmentInfos = ActorAlignmentInformations()
        self._alignmentInfostree = FuncTree()

    def getTypeId(self):
        return 203

    def initGameFightMonsterWithAlignmentInformations(self, param1=0, param2=None, param3=None, param4=2, param5=0, param6=False, param7=None, param8=[], param9=0, param10=0, param11=None):
        super().initGameFightMonsterInformations(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10)
        self.alignmentInfos = param11
        return self

    def reset(self):
        super().reset()
        self.alignmentInfos = ActorAlignmentInformations()

    def serialize(self, param1):
        self.serializeAs_GameFightMonsterWithAlignmentInformations(param1)

    def serializeAs_GameFightMonsterWithAlignmentInformations(self, param1):
        super().serializeAs_GameFightMonsterInformations(param1)
        self.alignmentInfos.serializeAs_ActorAlignmentInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameFightMonsterWithAlignmentInformations(param1)

    def deserializeAs_GameFightMonsterWithAlignmentInformations(self, param1):
        super().deserialize(param1)
        self.alignmentInfos = ActorAlignmentInformations()
        self.alignmentInfos.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameFightMonsterWithAlignmentInformations(param1)

    def deserializeAsyncAs_GameFightMonsterWithAlignmentInformations(self, param1):
        super().deserializeAsync(param1)
        self._alignmentInfostree = param1.add_child(self._alignmentInfostreeFunc)

    def _alignmentInfostreeFunc(self, param1):
        self.alignmentInfos = ActorAlignmentInformations()
        self.alignmentInfos.deserializeAsync(self._alignmentInfostree)


class GameRolePlayCharacterInformations(GameRolePlayHumanoidInformations):
    protocolId = 36

    def __init__(self):
        super().__init__()
        self.alignmentInfos = ActorAlignmentInformations()
        self._alignmentInfostree = FuncTree()

    def getTypeId(self):
        return 36

    def initGameRolePlayCharacterInformations(self, param1=0, param2=None, param3=None, param4="", param5=None, param6=0, param7=None):
        super().initGameRolePlayHumanoidInformations(param1,param2,param3,param4,param5,param6)
        self.alignmentInfos = param7
        return self

    def reset(self):
        super().reset()
        self.alignmentInfos = ActorAlignmentInformations()

    def serialize(self, param1):
        self.serializeAs_GameRolePlayCharacterInformations(param1)

    def serializeAs_GameRolePlayCharacterInformations(self, param1):
        super().serializeAs_GameRolePlayHumanoidInformations(param1)
        self.alignmentInfos.serializeAs_ActorAlignmentInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayCharacterInformations(param1)

    def deserializeAs_GameRolePlayCharacterInformations(self, param1):
        super().deserialize(param1)
        self.alignmentInfos = ActorAlignmentInformations()
        self.alignmentInfos.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayCharacterInformations(param1)

    def deserializeAsyncAs_GameRolePlayCharacterInformations(self, param1):
        super().deserializeAsync(param1)
        self._alignmentInfostree = param1.add_child(self._alignmentInfostreeFunc)

    def _alignmentInfostreeFunc(self, param1):
        self.alignmentInfos = ActorAlignmentInformations()
        self.alignmentInfos.deserializeAsync(self._alignmentInfostree)


class GameRolePlayMutantInformations(GameRolePlayHumanoidInformations):
    protocolId = 3

    def __init__(self):
        super().__init__()
        self.monsterId = 0
        self.powerLevel = 0

    def getTypeId(self):
        return 3

    def initGameRolePlayMutantInformations(self, param1=0, param2=None, param3=None, param4="", param5=None, param6=0, param7=0, param8=0):
        super().initGameRolePlayHumanoidInformations(param1,param2,param3,param4,param5,param6)
        self.monsterId = param7
        self.powerLevel = param8
        return self

    def reset(self):
        super().reset()
        self.monsterId = 0
        self.powerLevel = 0

    def serialize(self, param1):
        self.serializeAs_GameRolePlayMutantInformations(param1)

    def serializeAs_GameRolePlayMutantInformations(self, param1):
        super().serializeAs_GameRolePlayHumanoidInformations(param1)
        if self.monsterId < 0:
            raise RuntimeError("Forbidden value (" + str(self.monsterId) + ") on element monsterId.")
        param1.write_var_short(self.monsterId)
        param1.write_byte(self.powerLevel)

    def deserialize(self, param1):
        self.deserializeAs_GameRolePlayMutantInformations(param1)

    def deserializeAs_GameRolePlayMutantInformations(self, param1):
        super().deserialize(param1)
        self._monsterIdFunc(param1)
        self._powerLevelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GameRolePlayMutantInformations(param1)

    def deserializeAsyncAs_GameRolePlayMutantInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._monsterIdFunc)
        param1.add_child(self._powerLevelFunc)

    def _monsterIdFunc(self, param1):
        self.monsterId = param1.read_var_uh_short()
        if self.monsterId < 0:
            raise RuntimeError("Forbidden value (" + str(self.monsterId) + ") on element of GameRolePlayMutantInformations.monsterId.")

    def _powerLevelFunc(self, param1):
        self.powerLevel = param1.read_byte()


class AllianceFactSheetInformations(AllianceInformations):
    protocolId = 421

    def __init__(self):
        super().__init__()
        self.creationDate = 0

    def getTypeId(self):
        return 421

    def initAllianceFactSheetInformations(self, param1=0, param2="", param3="", param4=None, param5=0):
        super().initAllianceInformations(param1,param2,param3,param4)
        self.creationDate = param5
        return self

    def reset(self):
        super().reset()
        self.creationDate = 0

    def serialize(self, param1):
        self.serializeAs_AllianceFactSheetInformations(param1)

    def serializeAs_AllianceFactSheetInformations(self, param1):
        super().serializeAs_AllianceInformations(param1)
        if self.creationDate < 0:
            raise RuntimeError("Forbidden value (" + str(self.creationDate) + ") on element creationDate.")
        param1.write_int(self.creationDate)

    def deserialize(self, param1):
        self.deserializeAs_AllianceFactSheetInformations(param1)

    def deserializeAs_AllianceFactSheetInformations(self, param1):
        super().deserialize(param1)
        self._creationDateFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_AllianceFactSheetInformations(param1)

    def deserializeAsyncAs_AllianceFactSheetInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._creationDateFunc)

    def _creationDateFunc(self, param1):
        self.creationDate = param1.read_int()
        if self.creationDate < 0:
            raise RuntimeError("Forbidden value (" + str(self.creationDate) + ") on element of AllianceFactSheetInformations.creationDate.")


class GuildInsiderFactSheetInformations(GuildFactSheetInformations):
    protocolId = 423

    def __init__(self):
        super().__init__()
        self.leaderName = ""
        self.nbConnectedMembers = 0
        self.nbTaxCollectors = 0
        self.lastActivity = 0

    def getTypeId(self):
        return 423

    def initGuildInsiderFactSheetInformations(self, param1=0, param2="", param3=0, param4=None, param5=0, param6=0, param7="", param8=0, param9=0, param10=0):
        super().initGuildFactSheetInformations(param1,param2,param3,param4,param5,param6)
        self.leaderName = param7
        self.nbConnectedMembers = param8
        self.nbTaxCollectors = param9
        self.lastActivity = param10
        return self

    def reset(self):
        super().reset()
        self.leaderName = ""
        self.nbConnectedMembers = 0
        self.nbTaxCollectors = 0
        self.lastActivity = 0

    def serialize(self, param1):
        self.serializeAs_GuildInsiderFactSheetInformations(param1)

    def serializeAs_GuildInsiderFactSheetInformations(self, param1):
        super().serializeAs_GuildFactSheetInformations(param1)
        param1.write_utf(self.leaderName)
        if self.nbConnectedMembers < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbConnectedMembers) + ") on element nbConnectedMembers.")
        param1.write_var_short(self.nbConnectedMembers)
        if self.nbTaxCollectors < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbTaxCollectors) + ") on element nbTaxCollectors.")
        param1.write_byte(self.nbTaxCollectors)
        if self.lastActivity < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastActivity) + ") on element lastActivity.")
        param1.write_int(self.lastActivity)

    def deserialize(self, param1):
        self.deserializeAs_GuildInsiderFactSheetInformations(param1)

    def deserializeAs_GuildInsiderFactSheetInformations(self, param1):
        super().deserialize(param1)
        self._leaderNameFunc(param1)
        self._nbConnectedMembersFunc(param1)
        self._nbTaxCollectorsFunc(param1)
        self._lastActivityFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_GuildInsiderFactSheetInformations(param1)

    def deserializeAsyncAs_GuildInsiderFactSheetInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._leaderNameFunc)
        param1.add_child(self._nbConnectedMembersFunc)
        param1.add_child(self._nbTaxCollectorsFunc)
        param1.add_child(self._lastActivityFunc)

    def _leaderNameFunc(self, param1):
        self.leaderName = param1.read_utf()

    def _nbConnectedMembersFunc(self, param1):
        self.nbConnectedMembers = param1.read_var_uh_short()
        if self.nbConnectedMembers < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbConnectedMembers) + ") on element of GuildInsiderFactSheetInformations.nbConnectedMembers.")

    def _nbTaxCollectorsFunc(self, param1):
        self.nbTaxCollectors = param1.read_byte()
        if self.nbTaxCollectors < 0:
            raise RuntimeError("Forbidden value (" + str(self.nbTaxCollectors) + ") on element of GuildInsiderFactSheetInformations.nbTaxCollectors.")

    def _lastActivityFunc(self, param1):
        self.lastActivity = param1.read_int()
        if self.lastActivity < 0:
            raise RuntimeError("Forbidden value (" + str(self.lastActivity) + ") on element of GuildInsiderFactSheetInformations.lastActivity.")


class CharacterMinimalAllianceInformations(CharacterMinimalGuildInformations):
    protocolId = 444

    def __init__(self):
        super().__init__()
        self.alliance = BasicAllianceInformations()
        self._alliancetree = FuncTree()

    def getTypeId(self):
        return 444

    def initCharacterMinimalAllianceInformations(self, param1=0, param2="", param3=0, param4=None, param5=None, param6=None):
        super().initCharacterMinimalGuildInformations(param1,param2,param3,param4,param5)
        self.alliance = param6
        return self

    def reset(self):
        super().reset()
        self.alliance = BasicAllianceInformations()

    def serialize(self, param1):
        self.serializeAs_CharacterMinimalAllianceInformations(param1)

    def serializeAs_CharacterMinimalAllianceInformations(self, param1):
        super().serializeAs_CharacterMinimalGuildInformations(param1)
        self.alliance.serializeAs_BasicAllianceInformations(param1)

    def deserialize(self, param1):
        self.deserializeAs_CharacterMinimalAllianceInformations(param1)

    def deserializeAs_CharacterMinimalAllianceInformations(self, param1):
        super().deserialize(param1)
        self.alliance = BasicAllianceInformations()
        self.alliance.deserialize(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterMinimalAllianceInformations(param1)

    def deserializeAsyncAs_CharacterMinimalAllianceInformations(self, param1):
        super().deserializeAsync(param1)
        self._alliancetree = param1.add_child(self._alliancetreeFunc)

    def _alliancetreeFunc(self, param1):
        self.alliance = BasicAllianceInformations()
        self.alliance.deserializeAsync(self._alliancetree)


class CharacterHardcoreOrEpicInformations(CharacterBaseInformations):
    protocolId = 474

    def __init__(self):
        super().__init__()
        self.deathState = 0
        self.deathCount = 0
        self.deathMaxLevel = 0

    def getTypeId(self):
        return 474

    def initCharacterHardcoreOrEpicInformations(self, param1=0, param2="", param3=0, param4=None, param5=0, param6=False, param7=0, param8=0, param9=0):
        super().initCharacterBaseInformations(param1,param2,param3,param4,param5,param6)
        self.deathState = param7
        self.deathCount = param8
        self.deathMaxLevel = param9
        return self

    def reset(self):
        super().reset()
        self.deathState = 0
        self.deathCount = 0
        self.deathMaxLevel = 0

    def serialize(self, param1):
        self.serializeAs_CharacterHardcoreOrEpicInformations(param1)

    def serializeAs_CharacterHardcoreOrEpicInformations(self, param1):
        super().serializeAs_CharacterBaseInformations(param1)
        param1.write_byte(self.deathState)
        if self.deathCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.deathCount) + ") on element deathCount.")
        param1.write_var_short(self.deathCount)
        if self.deathMaxLevel < 1 or self.deathMaxLevel > 206:
            raise RuntimeError("Forbidden value (" + str(self.deathMaxLevel) + ") on element deathMaxLevel.")
        param1.write_byte(self.deathMaxLevel)

    def deserialize(self, param1):
        self.deserializeAs_CharacterHardcoreOrEpicInformations(param1)

    def deserializeAs_CharacterHardcoreOrEpicInformations(self, param1):
        super().deserialize(param1)
        self._deathStateFunc(param1)
        self._deathCountFunc(param1)
        self._deathMaxLevelFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_CharacterHardcoreOrEpicInformations(param1)

    def deserializeAsyncAs_CharacterHardcoreOrEpicInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._deathStateFunc)
        param1.add_child(self._deathCountFunc)
        param1.add_child(self._deathMaxLevelFunc)

    def _deathStateFunc(self, param1):
        self.deathState = param1.read_byte()
        if self.deathState < 0:
            raise RuntimeError("Forbidden value (" + str(self.deathState) + ") on element of CharacterHardcoreOrEpicInformations.deathState.")

    def _deathCountFunc(self, param1):
        self.deathCount = param1.read_var_uh_short()
        if self.deathCount < 0:
            raise RuntimeError("Forbidden value (" + str(self.deathCount) + ") on element of CharacterHardcoreOrEpicInformations.deathCount.")

    def _deathMaxLevelFunc(self, param1):
        self.deathMaxLevel = param1.read_unsigned_byte()
        if self.deathMaxLevel < 1 or self.deathMaxLevel > 206:
            raise RuntimeError("Forbidden value (" + str(self.deathMaxLevel) + ") on element of CharacterHardcoreOrEpicInformations.deathMaxLevel.")


class PartyInvitationMemberInformations(CharacterBaseInformations):
    protocolId = 376

    def __init__(self):
        super().__init__()
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.companions = []
        self._companionstree = FuncTree()

    def getTypeId(self):
        return 376

    def initPartyInvitationMemberInformations(self, param1=0, param2="", param3=0, param4=None, param5=0, param6=False, param7=0, param8=0, param9=0, param10=0, param11=[]):
        super().initCharacterBaseInformations(param1,param2,param3,param4,param5,param6)
        self.worldX = param7
        self.worldY = param8
        self.mapId = param9
        self.subAreaId = param10
        self.companions = param11
        return self

    def reset(self):
        super().reset()
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.companions = []

    def serialize(self, param1):
        self.serializeAs_PartyInvitationMemberInformations(param1)

    def serializeAs_PartyInvitationMemberInformations(self, param1):
        super().serializeAs_CharacterBaseInformations(param1)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        param1.write_short(len(self.companions))
        _loc2_ = 0
        while _loc2_ < len(self.companions):
            as_parent(self.companions[_loc2_], PartyCompanionBaseInformations).serializeAs_PartyCompanionBaseInformations(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_PartyInvitationMemberInformations(param1)

    def deserializeAs_PartyInvitationMemberInformations(self, param1):
        _loc4_ = None
        super().deserialize(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            _loc4_ = PartyCompanionBaseInformations()
            _loc4_.deserialize(param1)
            self.companions.append(_loc4_)
            _loc3_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PartyInvitationMemberInformations(param1)

    def deserializeAsyncAs_PartyInvitationMemberInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)
        self._companionstree = param1.add_child(self._companionstreeFunc)

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PartyInvitationMemberInformations.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PartyInvitationMemberInformations.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PartyInvitationMemberInformations.subAreaId.")

    def _companionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._companionstree.add_child(self._companionsFunc)
            _loc3_ += 1

    def _companionsFunc(self, param1):
        _loc2_ = PartyCompanionBaseInformations()
        _loc2_.deserialize(param1)
        self.companions.append(_loc2_)


class PartyMemberInformations(CharacterBaseInformations):
    protocolId = 90

    def __init__(self):
        super().__init__()
        self.lifePoints = 0
        self.maxLifePoints = 0
        self.prospecting = 0
        self.regenRate = 0
        self.initiative = 0
        self.alignmentSide = 0
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.status = PlayerStatus()
        self.companions = []
        self._statustree = FuncTree()
        self._companionstree = FuncTree()

    def getTypeId(self):
        return 90

    def initPartyMemberInformations(self, param1=0, param2="", param3=0, param4=None, param5=0, param6=False, param7=0, param8=0, param9=0, param10=0, param11=0, param12=0, param13=0, param14=0, param15=0, param16=0, param17=None, param18=[]):
        super().initCharacterBaseInformations(param1,param2,param3,param4,param5,param6)
        self.lifePoints = param7
        self.maxLifePoints = param8
        self.prospecting = param9
        self.regenRate = param10
        self.initiative = param11
        self.alignmentSide = param12
        self.worldX = param13
        self.worldY = param14
        self.mapId = param15
        self.subAreaId = param16
        self.status = param17
        self.companions = param18
        return self

    def reset(self):
        super().reset()
        self.lifePoints = 0
        self.maxLifePoints = 0
        self.prospecting = 0
        self.regenRate = 0
        self.initiative = 0
        self.alignmentSide = 0
        self.worldX = 0
        self.worldY = 0
        self.mapId = 0
        self.subAreaId = 0
        self.status = PlayerStatus()

    def serialize(self, param1):
        self.serializeAs_PartyMemberInformations(param1)

    def serializeAs_PartyMemberInformations(self, param1):
        super().serializeAs_CharacterBaseInformations(param1)
        if self.lifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element lifePoints.")
        param1.write_var_int(self.lifePoints)
        if self.maxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element maxLifePoints.")
        param1.write_var_int(self.maxLifePoints)
        if self.prospecting < 0:
            raise RuntimeError("Forbidden value (" + str(self.prospecting) + ") on element prospecting.")
        param1.write_var_short(self.prospecting)
        if self.regenRate < 0 or self.regenRate > 255:
            raise RuntimeError("Forbidden value (" + str(self.regenRate) + ") on element regenRate.")
        param1.write_byte(self.regenRate)
        if self.initiative < 0:
            raise RuntimeError("Forbidden value (" + str(self.initiative) + ") on element initiative.")
        param1.write_var_short(self.initiative)
        param1.write_byte(self.alignmentSide)
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element worldX.")
        param1.write_short(self.worldX)
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element worldY.")
        param1.write_short(self.worldY)
        param1.write_int(self.mapId)
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element subAreaId.")
        param1.write_var_short(self.subAreaId)
        param1.write_short(self.status.getTypeId())
        self.status.serialize(param1)
        param1.write_short(len(self.companions))
        _loc2_ = 0
        while _loc2_ < len(self.companions):
            as_parent(self.companions[_loc2_], PartyCompanionMemberInformations).serializeAs_PartyCompanionMemberInformations(param1)
            _loc2_ += 1

    def deserialize(self, param1):
        self.deserializeAs_PartyMemberInformations(param1)

    def deserializeAs_PartyMemberInformations(self, param1):
        _loc5_ = None
        super().deserialize(param1)
        self._lifePointsFunc(param1)
        self._maxLifePointsFunc(param1)
        self._prospectingFunc(param1)
        self._regenRateFunc(param1)
        self._initiativeFunc(param1)
        self._alignmentSideFunc(param1)
        self._worldXFunc(param1)
        self._worldYFunc(param1)
        self._mapIdFunc(param1)
        self._subAreaIdFunc(param1)
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserialize(param1)
        _loc3_ = param1.read_unsigned_short()
        _loc4_ = 0
        while _loc4_ < _loc3_:
            _loc5_ = PartyCompanionMemberInformations()
            _loc5_.deserialize(param1)
            self.companions.append(_loc5_)
            _loc4_ += 1

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PartyMemberInformations(param1)

    def deserializeAsyncAs_PartyMemberInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._lifePointsFunc)
        param1.add_child(self._maxLifePointsFunc)
        param1.add_child(self._prospectingFunc)
        param1.add_child(self._regenRateFunc)
        param1.add_child(self._initiativeFunc)
        param1.add_child(self._alignmentSideFunc)
        param1.add_child(self._worldXFunc)
        param1.add_child(self._worldYFunc)
        param1.add_child(self._mapIdFunc)
        param1.add_child(self._subAreaIdFunc)
        self._statustree = param1.add_child(self._statustreeFunc)
        self._companionstree = param1.add_child(self._companionstreeFunc)

    def _lifePointsFunc(self, param1):
        self.lifePoints = param1.read_var_uh_int()
        if self.lifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element of PartyMemberInformations.lifePoints.")

    def _maxLifePointsFunc(self, param1):
        self.maxLifePoints = param1.read_var_uh_int()
        if self.maxLifePoints < 0:
            raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element of PartyMemberInformations.maxLifePoints.")

    def _prospectingFunc(self, param1):
        self.prospecting = param1.read_var_uh_short()
        if self.prospecting < 0:
            raise RuntimeError("Forbidden value (" + str(self.prospecting) + ") on element of PartyMemberInformations.prospecting.")

    def _regenRateFunc(self, param1):
        self.regenRate = param1.read_unsigned_byte()
        if self.regenRate < 0 or self.regenRate > 255:
            raise RuntimeError("Forbidden value (" + str(self.regenRate) + ") on element of PartyMemberInformations.regenRate.")

    def _initiativeFunc(self, param1):
        self.initiative = param1.read_var_uh_short()
        if self.initiative < 0:
            raise RuntimeError("Forbidden value (" + str(self.initiative) + ") on element of PartyMemberInformations.initiative.")

    def _alignmentSideFunc(self, param1):
        self.alignmentSide = param1.read_byte()

    def _worldXFunc(self, param1):
        self.worldX = param1.read_short()
        if self.worldX < -255 or self.worldX > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PartyMemberInformations.worldX.")

    def _worldYFunc(self, param1):
        self.worldY = param1.read_short()
        if self.worldY < -255 or self.worldY > 255:
            raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PartyMemberInformations.worldY.")

    def _mapIdFunc(self, param1):
        self.mapId = param1.read_int()

    def _subAreaIdFunc(self, param1):
        self.subAreaId = param1.read_var_uh_short()
        if self.subAreaId < 0:
            raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PartyMemberInformations.subAreaId.")

    def _statustreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        self.status = ProtocolTypeManager.get_instance(PlayerStatus,_loc2_)
        self.status.deserializeAsync(self._statustree)

    def _companionstreeFunc(self, param1):
        _loc2_ = param1.read_unsigned_short()
        _loc3_ = 0
        while _loc3_ < _loc2_:
            self._companionstree.add_child(self._companionsFunc)
            _loc3_ += 1

    def _companionsFunc(self, param1):
        _loc2_ = PartyCompanionMemberInformations()
        _loc2_.deserialize(param1)
        self.companions.append(_loc2_)


class PartyMemberArenaInformations(PartyMemberInformations):
    protocolId = 391

    def __init__(self):
        super().__init__()
        self.rank = 0

    def getTypeId(self):
        return 391

    def initPartyMemberArenaInformations(self, param1=0, param2="", param3=0, param4=None, param5=0, param6=False, param7=0, param8=0, param9=0, param10=0, param11=0, param12=0, param13=0, param14=0, param15=0, param16=0, param17=None, param18=[], param19=0):
        super().initPartyMemberInformations(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12,param13,param14,param15,param16,param17,param18)
        self.rank = param19
        return self

    def reset(self):
        super().reset()
        self.rank = 0

    def serialize(self, param1):
        self.serializeAs_PartyMemberArenaInformations(param1)

    def serializeAs_PartyMemberArenaInformations(self, param1):
        super().serializeAs_PartyMemberInformations(param1)
        if self.rank < 0 or self.rank > 20000:
            raise RuntimeError("Forbidden value (" + str(self.rank) + ") on element rank.")
        param1.write_var_short(self.rank)

    def deserialize(self, param1):
        self.deserializeAs_PartyMemberArenaInformations(param1)

    def deserializeAs_PartyMemberArenaInformations(self, param1):
        super().deserialize(param1)
        self._rankFunc(param1)

    def deserializeAsync(self, param1):
        self.deserializeAsyncAs_PartyMemberArenaInformations(param1)

    def deserializeAsyncAs_PartyMemberArenaInformations(self, param1):
        super().deserializeAsync(param1)
        param1.add_child(self._rankFunc)

    def _rankFunc(self, param1):
        self.rank = param1.read_var_uh_short()
        if self.rank < 0 or self.rank > 20000:
            raise RuntimeError("Forbidden value (" + str(self.rank) + ") on element of PartyMemberArenaInformations.rank.")


