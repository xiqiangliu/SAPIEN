//
// Created by sim on 10/12/19.
//

#pragma once

#include "device/movo_device_control.h"
#include "device/joystick_ps3.h"
namespace sapien::robot {


class MOVOPS3 : public MOVO{
  std::unique_ptr<PS3> input;

public:
  explicit MOVOPS3(ControllerManger *manger);
  ~MOVOPS3();
  void step() override;
};
} // namespace sapien::robot
