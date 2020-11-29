import { spawn, SpawnOptions } from "child_process";
import * as child_process from "child_process";
import { createInterface, ReadLine } from "readline";

export type BinaryProcessRun = {
  proc: child_process.ChildProcess;
  readLine: ReadLine;
};

export function runProcess(
  command: string,
  args?: ReadonlyArray<string>,
  options?: SpawnOptions
): BinaryProcessRun {
  // @ts-ignore
  const proc = spawn(command, args, options);

  const readLine = createInterface({
    // @ts-ignore
    input: proc.stdout,
    // @ts-ignore
    output: proc.stdin,
  });

  return { proc, readLine };
}
