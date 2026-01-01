##########################################################################
# Copyright 2025 Vladislav Riabov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##########################################################################

import argparse
import ai

def main():

    parser = argparse.ArgumentParser(
        description="Explain a source file using an LLM"
    )
    parser.add_argument(
        "path",
        help="Path to the file to explain",
    )

    args = parser.parse_args()

    print("AI Code Advisor")
    ai.explain(args.path)

if __name__ == "__main__":
    main()