import fetchBinaryPath from "./fetchBinaryPath";
import { BinaryProcessRun, runProcess } from "./runProcess";

export default function runBinary(
  additionalArgs: string[] = [],
  inheritStdio = false
): BinaryProcessRun {
  const command = fetchBinaryPath();

  const args: string[] = [
    "--client=vscode",
    "--no-lsp=true",
    "--client-metadata",
    ...additionalArgs,
  ].filter((i): i is string => i !== null);

  return runProcess(command, args, {
    stdio: inheritStdio ? "inherit" : "pipe",
  });
}
