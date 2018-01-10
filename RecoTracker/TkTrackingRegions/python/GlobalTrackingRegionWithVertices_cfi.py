import FWCore.ParameterSet.Config as cms

RegionPSetWithVerticesBlock = cms.PSet(
    RegionPSet = cms.PSet(
        precise = cms.bool(True),
        useMultipleScattering = cms.bool(False),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        useFixedError = cms.bool(True),
        originRadius = cms.double(0.2),
        sigmaZVertex = cms.double(3.0),
        fixedError = cms.double(0.2),
        VertexCollection = cms.InputTag("firstStepPrimaryVertices"),
        ptMin = cms.double(0.9),
        useFoundVertices = cms.bool(True),
        useFakeVertices = cms.bool(False),
        maxNVertices = cms.int32(-1),
        nSigmaZ = cms.double(4.0)
    )
)
from Configuration.Eras.Modifier_trackingLowPU_cff import trackingLowPU
trackingLowPU.toModify(RegionPSetWithVerticesBlock,
    RegionPSet = dict(VertexCollection = "pixelVertices")
)
