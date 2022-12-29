#SPDX-FileCopyrightText:2022 Tarou Sato<s21c1023nb@s.chibakoudai.jp>
##SPDX-License-Identifier:BSD-3-Clause#SPDX-FileCopyrightText:2022 Tarou Sato<s21c1023nb@s.chibakoudai.jp>
#SPDX-License-Identifier:BSD-3-Clause

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():

        talker = launch_ros.actions.Node(
                package='moc',
                executable='talker',
                )
        listener = launch_ros.actions.Node(
                package='moc',
                executable='listener',
                output='screen'
               )       
        return launch.LaunchDescription([talker, listener])
