import FWCore.ParameterSet.Config as cms

dimuonsOneTrackFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("userDataDimuonsOneTrack"),
    minNumber = cms.uint32(1)
)


