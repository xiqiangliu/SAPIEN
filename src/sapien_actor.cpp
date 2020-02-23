#include "sapien_actor.h"
#include "renderer/render_interface.h"
#include "sapien_scene.h"
#include <spdlog/spdlog.h>

namespace sapien {

SActor::SActor(PxRigidBody *actor, physx_id_t id, SScene *scene,
               std::vector<Renderer::IPxrRigidbody *> renderBodies,
               std::vector<Renderer::IPxrRigidbody *> collisionBodies)
    : SActorDynamicBase(id, scene, renderBodies, collisionBodies), mActor(actor) {}

PxRigidBody *SActor::getPxActor() { return mActor; }

void SActor::destroy() { mParentScene->removeActor(this); }

EActorType SActor::getType() const {
  return mActor->getRigidBodyFlags().isSet(PxRigidBodyFlag::eKINEMATIC) ? EActorType::KINEMATIC
                                                                        : EActorType::DYNAMIC;
}

void SActor::setPose(PxTransform const &pose) { getPxActor()->setGlobalPose(pose); }

void SActor::setVelocity(PxVec3 const &v) { getPxActor()->setLinearVelocity(v); }
void SActor::setAngularVelocity(PxVec3 const &v) { getPxActor()->setAngularVelocity(v); }

std::vector<PxReal> SActor::packData() {
  std::vector<PxReal> data;
  auto pose = getPose();
  data.push_back(pose.p.x);
  data.push_back(pose.p.y);
  data.push_back(pose.p.z);
  data.push_back(pose.q.x);
  data.push_back(pose.q.y);
  data.push_back(pose.q.z);
  data.push_back(pose.q.w);

  auto lv = getVelocity();
  auto av = getAngularVelocity();
  data.push_back(lv.x);
  data.push_back(lv.y);
  data.push_back(lv.z);
  data.push_back(av.x);
  data.push_back(av.y);
  data.push_back(av.z);

  return data;
}

void SActor::unpackData(std::vector<PxReal> const &data) {
  if (data.size() != 13) {
    spdlog::error("Failed to unpack actor: {} numbers expected but {} provided", 13, data.size());
    return;
  }
  getPxActor()->setGlobalPose({{data[0], data[1], data[2]}, {data[3], data[4], data[5], data[6]}});
  getPxActor()->setLinearVelocity({data[7], data[8], data[9]});
  getPxActor()->setAngularVelocity({data[10], data[11], data[12]});
}

SActorStatic::SActorStatic(PxRigidStatic *actor, physx_id_t id, SScene *scene,
                           std::vector<Renderer::IPxrRigidbody *> renderBodies,
                           std::vector<Renderer::IPxrRigidbody *> collisionBodies)
    : SActorBase(id, scene, renderBodies, collisionBodies), mActor(actor) {}

PxRigidActor *SActorStatic::getPxActor() { return mActor; }

void SActorStatic::destroy() { mParentScene->removeActor(this); }

void SActorStatic::setPose(PxTransform const &pose) { getPxActor()->setGlobalPose(pose); }

std::vector<PxReal> SActorStatic::packData() {
  std::vector<PxReal> data;
  auto pose = getPose();
  data.push_back(pose.p.x);
  data.push_back(pose.p.y);
  data.push_back(pose.p.z);
  data.push_back(pose.q.x);
  data.push_back(pose.q.y);
  data.push_back(pose.q.z);
  data.push_back(pose.q.w);

  return data;
}

void SActorStatic::unpackData(std::vector<PxReal> const &data) {
  if (data.size() != 7) {
    spdlog::error("Failed to unpack actor: {} numbers expected but {} provided", 13, data.size());
    return;
  }
  getPxActor()->setGlobalPose({{data[0], data[1], data[2]}, {data[3], data[4], data[5], data[6]}});
}

} // namespace sapien
