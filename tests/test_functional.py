import json
import subprocess


def test_it_should_output_json():
    proc = subprocess.Popen(
        "python src/git_hours/main.py", shell=True, stdout=subprocess.PIPE
    )
    work = json.load(proc.stdout)
    assert work["total"]["hours"] > 0
    assert work["total"]["commits"] > 0


# describe('git-hours', () => {
#
#   // it('Should analyse since today', (done) => {
#   //   exec('node ./src/index.js --since today', (err, stdout) => {
#   //     assert.ifError(err);
#   //     const work = JSON.parse(stdout);
#   //     assert.strictEqual(typeof work.total.hours, 'number');
#   //     done();
#   //   });
#   // });
#   //
#   // it('Should analyse since yesterday', (done) => {
#   //   exec('node ./src/index.js --since yesterday', (err, stdout) => {
#   //     assert.ifError(err);
#   //     const work = JSON.parse(stdout);
#   //     assert.strictEqual(typeof work.total.hours, 'number');
#   //     done();
#   //   });
#   // });
#   //
#   // it('Should analyse since last week', (done) => {
#   //   exec('node ./src/index.js --since lastweek', (err, stdout) => {
#   //     assert.ifError(err);
#   //     const work = JSON.parse(stdout);
#   //     assert.strictEqual(typeof work.total.hours, 'number');
#   //     done();
#   //   });
#   // });
#   //
#   // it('Should analyse since a specific date', (done) => {
#   //   exec('node ./src/index.js --since 2015-01-01', (err, stdout) => {
#   //     assert.ifError(err);
#   //     const work = JSON.parse(stdout);
#   //     assert.notEqual(work.total.hours, 0);
#   //     done();
#   //   });
#   // });
#   //
#   // it('Should analyse as without param', (done) => {
#   //   exec('node ./src/index.js --since always', (err, stdout) => {
#   //     assert.ifError(err);
#   //     const work = JSON.parse(stdout);
#   //     assert.equal(work.total.hours, totalHoursCount);
#   //     done();
#   //   });
#   // });
#
# });
