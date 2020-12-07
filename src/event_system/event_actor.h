#pragma once
#include "event.h"

namespace sapien {

class SActorBase;

struct EventActorPreDestroy : public Event {
  SActorBase *actor;
};

struct EventActorStep : public Event {
  SActorBase *actor;
  float time;
};

struct EventActorContact : public Event {
public:
  SActorBase *self;
  SActorBase *other;
  class SContact const *contact;
};

struct EventActorTrigger : public Event {
public:
  SActorBase *triggerActor;
  SActorBase *otherActor;
  class STrigger const *trigger;
};

} // namespace sapien
